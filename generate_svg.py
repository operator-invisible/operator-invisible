"""
build.py — Patch Sushmita's animated SVG template with Shivam's data + ASCII art
"""
from html import escape
from pathlib import Path

# ── Your ASCII art (the real one you pasted) ──────────────────
ASCII_ART = """###########################################*****###################**#**##################
#############################*##########*#**##********############***###*****#############
#############################***##******************************************##*######**###
#############################**######***********************************************#***##
############################***#****#***************************************************##
########################*******************#####****************************************##
###################******************####%%%%%%%%%###*********************************####
#################******************#%%%@@@@@@@@@@@@@@%%#******************************#**#
###############******************#%@@%##************#%@@%#**************************##**##
###############*****************#%%#*+===============+*#@@#************************#######
###############*****************#%***###*+====+*#####*++*%@#***********************####*##
##########**************************#####*++++*#####*****+#%#*****************#******#****
######***********************==**+##%%##**+===+**#%%%#*++++#%=:-+*************************
######********************+-::+++#****+**+===-=+**+++=+*+=++##+:..=***********************
###*********************+:.:-**+++=====++#%*+##+============+##+=:..=*********************
####*******************-.:---*++=======+*##++*#*============+##=---..-********************
####*****************+:.:--=+*+========+**++++**+===========+*#++=-:. :*******************
##*******************:..::.=+-+=====++****++++++++++========++=----:...+**************#***
#####****************:......:-+==++*****+++++++++*##*+=======-.........+***********#*#****
###******************:....:::=+=++++*+++++++++====+*++======+=:::......+******************
####*############***+....::::=++++++++++============+=======+=::::.....-******************
###############*****=...:::::==+++++++++==++++==============++::::::...:******************
**#############*****=..:::::-==++++++++++*****+++=========-=*+-:::::::..+*****************
**############******=..:::::--==+++++***********+++======---*+-::::::::.+*****************
*##############*****+...:::::--==++++***********+++=====---===-::::.....+*****##**###*****
################****+. ......:++==++++**********+++=====---=+=::::......+*****#**#*####***
#################****+=------+##+=++++****###****++=======-=**=:.::::-=+******############
####################*###########+++++****++++++++++========*###******###**################
################################*+++++++++=================*##############################
################################+++++++++++================*##############################
################################+++++++++=================+*#############################*
################################+++==============-========+############################***
###############################*++=========================*##########################****
###############################++==========================*#########################*****
##############################*++==========================+######################********
#############################*++============================+###*+++*######*##************
#####################+--:-==+++===========================+*=-=-:...:-+**##**###**********
##################*=:.....:-#%%#+==++==================+*%%@*-..........-=***####*********
#################=:...::=*%%@@@@%#*+++================*%%%%@@%*+=-:........:-=++*##*******
###########**+=-:..:-+*%@@@@@@@%%%%#*+==============+#%%%%%@@@@@@%#*+-::.........-********
***++++++=:...:-=+#%@@@@%%%%%%%%%%%%%#+============+#%#%%%%%%%%%%%%@@%%#*+=-::....::::::::
........::-=+*#%@@@@%%%%%#######%####%#+==========+#%##############%%%%%@@%%%#*++-::......"""

# ── Your profile data ─────────────────────────────────────────
USERNAME = "ProShivam"
PROMPT   = "proshivam@dev ~ % ./profile.sh --live"

# Info rows: (label_parts, value)
# label_parts is a list of alternating ("cc"|"key", text) segments
ROWS = [
    # header
    ("header", f"{USERNAME}"),
    ("head_sep", ""),
    # fields
    ("field", ("Subject",  "Shivam Patel")),
    ("field", ("Role",     "Cybersecurity Student · Ethical Hacker")),
    ("field", ("Origin",   "India")),
    ("field", ("Education","B.Tech Cybersecurity")),
    ("field", ("Status",   "Learning · Building · Hacking (Ethically)")),
    ("field", ("ToolChain","Kali Linux, Wireshark, Burp Suite, Git")),
    ("blank", ""),
    ("section", "Core Skills"),
    ("field", ("Core.Lang",       "Python, C, Bash, JavaScript")),
    ("field", ("Core.Offensive",  "Recon, OSINT, Exploitation, CTF")),
    ("field", ("Core.Defensive",  "SIEM, Log Analysis, Threat Intel")),
    ("field", ("Core.Tools",      "Nmap, Metasploit, SQLMap, Hydra")),
    ("blank", ""),
    ("section", "Contact"),
    ("field", ("Grid.Mail",     "shivam@example.com")),
    ("field", ("Grid.LinkedIn", "linkedin.com/in/proshivam")),
    ("field", ("Grid.Github",   "github.com/ProShivam")),
    ("blank", ""),
    ("section", "Live Stats"),
    ("plain", "See live GitHub stats badges below in README ↓"),
]

MONO = "'Courier New', Consolas, monospace"

def dots(label):
    # Match original dot count style based on label length
    base = 32
    n = max(4, base - len(label))
    return " " + ("." * n) + " "

def split_key(label):
    """Split 'Core.Lang' into key+dot+key segments like original."""
    parts = label.split(".")
    segs = []
    for i, p in enumerate(parts):
        segs.append(("key", p))
        if i < len(parts) - 1:
            segs.append(("cc", "."))
    return segs

def build_info_rows(rows, start_y=26, line_h=22, x=520):
    """Build animated clip-path rows identical to original structure."""
    n = len(rows)
    clips = []
    texts = []

    for i, row in enumerate(rows):
        y_top  = start_y + i * line_h
        y_text = y_top + 16
        delay  = round(0.75 + i * 0.115, 2)

        # clip path
        clips.append(
            f'<clipPath id="lc{i}"><rect x="{x}" y="{y_top:.2f}" width="0" height="24">'
            f'<animate attributeName="width" from="0" to="690" dur="0.38s" '
            f'begin="{delay}s" fill="freeze"/></rect></clipPath>'
        )

        kind = row[0]
        data = row[1]

        if kind == "header":
            inner = (f'<tspan x="{x}" y="{y_text}" class="head">{escape(data)}</tspan>'
                     f'<tspan class="cc"> -{"—"*44}-—-</tspan>')
        elif kind == "head_sep":
            inner = f'<tspan x="{x}" y="{y_text}" class="cc">. </tspan>'
        elif kind == "blank":
            inner = f'<tspan x="{x}" y="{y_text}" class="cc">. </tspan>'
        elif kind == "section":
            inner = (f'<tspan x="{x}" y="{y_text}" class="accent">- {escape(data)}</tspan>'
                     f'<tspan class="cc"> -{"—"*44}-—-</tspan>')
        elif kind == "field":
            label, value = data
            key_segs = split_key(label)
            key_html = ""
            for seg_kind, seg_text in key_segs:
                key_html += f'<tspan class="{seg_kind}">{escape(seg_text)}</tspan>'
            d = dots(label)
            inner = (f'<tspan x="{x}" y="{y_text}" class="cc">. </tspan>'
                     + key_html
                     + f'<tspan class="cc">{escape(d)}</tspan>'
                     + f'<tspan class="value">{escape(value)}</tspan>')
        elif kind == "plain":
            inner = (f'<tspan x="{x}" y="{y_text}" class="cc">. </tspan>'
                     f'<tspan class="value">{escape(data)}</tspan>')
        else:
            inner = ""

        texts.append(
            f'<g clip-path="url(#lc{i})"><text x="{x}" y="0" fill="#dbeafe">{inner}</text></g>'
        )

    return clips, texts

def build_ascii_tspans(art, start_x=30, start_y=50, line_h=7.6):
    lines = art.strip().splitlines()
    tspans = []
    for i, line in enumerate(lines):
        y = round(start_y + i * line_h, 2)
        tspans.append(f'<tspan x="{start_x}" y="{y}" xml:space="preserve">{escape(line)}</tspan>')
    return tspans, round(start_y + len(lines) * line_h, 2)

def make_svg(theme):
    is_dark = theme == "dark"
    bg_grad_stops = (
        ('<stop offset="0%" stop-color="#0B1120"/>'
         '<stop offset="100%" stop-color="#050816"/>') if is_dark else
        ('<stop offset="0%" stop-color="#f0f4ff"/>'
         '<stop offset="100%" stop-color="#e8edf8"/>')
    )
    ascii_color = "url(#asciiGrad)" if is_dark else "#1e3a5f"
    scan_fill   = "#7DD3FC" if is_dark else "#0369a1"
    scan_line_c = "#22D3EE" if is_dark else "#0ea5e9"
    border_op   = "0.8" if is_dark else "0.5"
    val_color   = "#E5E7EB" if is_dark else "#1e293b"
    cc_color    = "#475569" if is_dark else "#64748b"
    head_color  = "#7C3AED" if is_dark else "#4f46e5"
    key_color   = "#22D3EE" if is_dark else "#0369a1"
    accent_c    = "#10B981" if is_dark else "#059669"
    body_bg     = "url(#bgGlow)" if is_dark else "#f0f4ff"
    panel_bg    = "#0B1120" if is_dark else "#e2e8f0"
    titlebar_bg = "#0B1120" if is_dark else "#dde4ee"

    ascii_grad = ""
    if is_dark:
        ascii_grad = """
  <linearGradient id="asciiGrad" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" stop-color="#22D3EE">
      <animate attributeName="stop-color" values="#22D3EE;#7C3AED;#38BDF8;#22D3EE" dur="9s" repeatCount="indefinite"/>
    </stop>
    <stop offset="100%" stop-color="#7C3AED">
      <animate attributeName="stop-color" values="#7C3AED;#38BDF8;#22D3EE;#7C3AED" dur="9s" repeatCount="indefinite"/>
    </stop>
  </linearGradient>"""

    clips, texts = build_info_rows(ROWS)
    n = len(ROWS)
    ascii_tspans, art_bottom = build_ascii_tspans(ASCII_ART)

    # cursor blink y
    last_y = 26 + (n - 1) * 22 + 16
    cursor_y = 26 + (n - 1) * 22

    # reveal mask height
    reveal_h = max(520, int(art_bottom) + 40)
    H = reveal_h + 90  # total svg height

    clips_str  = "".join(clips)
    texts_str  = "\n".join(texts)
    ascii_str  = "\n".join(ascii_tspans)

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1180" height="{H}" viewBox="0 0 1180 {H}">
<defs>
{ascii_grad}
  <linearGradient id="borderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" stop-color="#7C3AED"/>
    <stop offset="50%" stop-color="#22D3EE"/>
    <stop offset="100%" stop-color="#10B981"/>
  </linearGradient>
  <radialGradient id="bgGlow" cx="30%" cy="20%" r="80%">
    {bg_grad_stops}
  </radialGradient>
  <linearGradient id="scanGrad" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%"   stop-color="{scan_line_c}" stop-opacity="0"/>
    <stop offset="45%"  stop-color="{scan_line_c}" stop-opacity="0.05"/>
    <stop offset="50%"  stop-color="{scan_line_c}" stop-opacity="0.65"/>
    <stop offset="55%"  stop-color="{scan_line_c}" stop-opacity="0.05"/>
    <stop offset="100%" stop-color="#7C3AED"        stop-opacity="0"/>
  </linearGradient>
  <pattern id="scanlines" width="4" height="4" patternUnits="userSpaceOnUse">
    <rect width="4" height="1" fill="{scan_fill}" opacity="0.05"/>
  </pattern>
  <filter id="softGlow" x="-50%" y="-50%" width="200%" height="200%">
    <feGaussianBlur stdDeviation="4" result="blur"/>
    <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  <mask id="revealMask" maskUnits="userSpaceOnUse" x="0" y="0" width="1180" height="{H}">
    <rect x="0" y="0" width="1180" height="0" fill="#fff">
      <animate attributeName="height" from="0" to="{reveal_h}" dur="2.6s" begin="0.2s" fill="freeze" calcMode="spline" keySplines="0.25 0.1 0.25 1"/>
    </rect>
  </mask>
  {clips_str}
  <style>
    .ascii  {{ font-family: 'Courier New', Consolas, monospace; font-size: 7.4px; fill: {ascii_color}; letter-spacing: -0.2px; }}
    .key    {{ font-family: 'Courier New', Consolas, monospace; font-size: 15px; fill: {key_color}; font-weight: bold; }}
    .value  {{ font-family: 'Courier New', Consolas, monospace; font-size: 15px; fill: {val_color}; }}
    .cc     {{ font-family: 'Courier New', Consolas, monospace; font-size: 15px; fill: {cc_color}; }}
    .head   {{ font-family: 'Courier New', Consolas, monospace; font-size: 17px; fill: {head_color}; font-weight: bold; }}
    .accent {{ font-family: 'Courier New', Consolas, monospace; font-size: 15px; fill: {accent_c}; font-weight: bold; }}
    text, tspan {{ white-space: pre; }}
    .term-label {{ font-family: 'Courier New', Consolas, monospace; font-size: 12px; fill: #64748B; letter-spacing: 0.5px; }}
    .scan-label {{ font-family: 'Courier New', Consolas, monospace; font-size: 10px; fill: #F87171; letter-spacing: 1px; }}
    .panel-title {{ font-family: 'Courier New', Consolas, monospace; font-size: 11px; fill: #38BDF8; letter-spacing: 2px; opacity: 0.7; }}
    .cursor-blink {{ fill: {key_color}; }}
  </style>
</defs>

<rect width="1180" height="{H}" rx="18" fill="{body_bg}"/>
<rect width="1180" height="{H}" rx="18" fill="url(#scanlines)"/>

<g id="titlebar">
  <rect x="3" y="3" width="1174" height="34" rx="16" fill="{titlebar_bg}" fill-opacity="0.85"/>
  <circle cx="24" cy="20" r="5" fill="#EF4444"><animate attributeName="opacity" values="1;0.55;1" dur="4s" repeatCount="indefinite"/></circle>
  <circle cx="42" cy="20" r="5" fill="#F59E0B"><animate attributeName="opacity" values="1;0.55;1" dur="4s" begin="0.3s" repeatCount="indefinite"/></circle>
  <circle cx="60" cy="20" r="5" fill="#10B981"><animate attributeName="opacity" values="1;0.55;1" dur="4s" begin="0.6s" repeatCount="indefinite"/></circle>
  <text x="590" y="25" text-anchor="middle" class="term-label">{escape(PROMPT)}</text>
  <circle cx="1122" cy="20" r="4" fill="#F87171">
    <animate attributeName="opacity" values="1;0.15;1" dur="1.1s" repeatCount="indefinite"/>
  </circle>
  <text x="1132" y="24" class="scan-label">SCANNING</text>
</g>

<g transform="translate(0,38)">
  <rect x="14"  y="26" width="488" height="{reveal_h - 60}" rx="14" fill="{panel_bg}" fill-opacity="0.35" stroke="url(#borderGrad)" stroke-width="1" opacity="0.35"/>
  <rect x="508" y="10" width="655" height="{reveal_h - 44}" rx="14" fill="{panel_bg}" fill-opacity="0.35" stroke="url(#borderGrad)" stroke-width="1" opacity="0.35"/>
  <text x="30"  y="24" class="panel-title">VISUAL.MAP</text>
  <text x="524" y="24" class="panel-title">SYSTEM.INFO</text>

  <g mask="url(#revealMask)">
  <text x="30" y="0" class="ascii">
{ascii_str}
  </text>
  </g>

  {texts_str}

  <rect x="522" y="{cursor_y}.0" width="9" height="16" class="cursor-blink" opacity="0">
    <animate attributeName="opacity" values="0;0;1;0;1;0;1;0" keyTimes="0;0.01;0.02;0.3;0.5;0.7;0.85;1" dur="1.4s" begin="{round(0.75 + n*0.115, 2)}s" repeatCount="indefinite"/>
  </rect>
</g>

<rect x="0" y="-70" width="1180" height="70" fill="url(#scanGrad)" opacity="0.7" style="mix-blend-mode:screen">
  <animateTransform attributeName="transform" type="translate" from="0 -70" to="0 {H+70}" dur="4.2s" repeatCount="indefinite"/>
</rect>

<rect x="3" y="3" width="1174" height="{H-6}" rx="16" fill="none" stroke="url(#borderGrad)" stroke-width="2" opacity="{border_op}">
  <animate attributeName="opacity" values="0.5;0.95;0.5" dur="3.2s" repeatCount="indefinite"/>
</rect>
</svg>"""

Path("/home/claude/dark.svg").write_text(make_svg("dark"),  encoding="utf-8")
Path("/home/claude/light.svg").write_text(make_svg("light"), encoding="utf-8")
print("Done — dark.svg and light.svg generated")
