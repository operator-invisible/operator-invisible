from html import escape
from pathlib import Path

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

USERNAME = "ProShivam"
PROMPT   = "proshivam@dev ~ % ./profile.sh --live"

ROWS = [
    ("header",  USERNAME),
    ("head_sep",""),
    ("field",   ("Subject",       "Shivam Patel")),
    ("field",   ("Role",          "Cybersecurity Student · Ethical Hacker")),
    ("field",   ("Origin",        "India")),
    ("field",   ("Education",     "B.Tech Cybersecurity")),
    ("field",   ("Status",        "Learning · Building · Hacking (Ethically)")),
    ("field",   ("ToolChain",     "Kali Linux, Wireshark, Burp Suite, Git")),
    ("blank",   ""),
    ("section", "Core Skills"),
    ("field",   ("Core.Lang",     "Python, C, Bash, JavaScript")),
    ("field",   ("Core.Offensive","Recon, OSINT, Exploitation, CTF")),
    ("field",   ("Core.Defensive","SIEM, Log Analysis, Threat Intel")),
    ("field",   ("Core.Tools",    "Nmap, Metasploit, SQLMap, Hydra")),
    ("blank",   ""),
    ("section", "Contact"),
    ("field",   ("Grid.Mail",     "shivam@example.com")),
    ("field",   ("Grid.LinkedIn", "linkedin.com/in/proshivam")),
    ("field",   ("Grid.Github",   "github.com/ProShivam")),
    ("blank",   ""),
    ("section", "Live Stats"),
    ("plain",   "See live GitHub stats badges below in README ↓"),
]

# ── Layout constants ──────────────────────────────────────────
SVG_W       = 1180
LEFT_X      = 14        # left panel rect x
LEFT_W      = 488       # left panel width   → right edge = 502
LEFT_TOP    = 64        # absolute top of left panel (26 rel + 38 transform)
LEFT_H      = 460       # left panel height  → bottom = 524
ART_X       = 19        # art start x (inside panel, with small padding)
ART_Y_REL   = 40        # art start y relative to <g transform="translate(0,38)">
FONT_SIZE   = 8.9       # px — fits 90 chars × 0.6 × 8 = 432px < 472px available
LINE_H      = 10.5       # px — 44 lines × 9.5 = 418px < 436px available
INFO_X      = 520       # right panel info column x
INFO_LINE_H = 22        # px between info rows

def dots(label):
    n = max(4, 30 - len(label))
    return " " + ("." * n) + " "

def split_key(label):
    parts = label.split(".")
    segs = []
    for i, p in enumerate(parts):
        segs.append(("key", p))
        if i < len(parts)-1:
            segs.append(("cc", "."))
    return segs

def build_info_rows(rows):
    clips, texts = [], []
    for i, row in enumerate(rows):
        y_top  = 26 + i * INFO_LINE_H
        y_text = y_top + 16
        delay  = round(0.75 + i * 0.115, 2)
        clips.append(
            f'<clipPath id="lc{i}"><rect x="{INFO_X}" y="{y_top:.2f}" width="0" height="24">'
            f'<animate attributeName="width" from="0" to="690" dur="0.38s" '
            f'begin="{delay}s" fill="freeze"/></rect></clipPath>'
        )
        kind = row[0]; data = row[1]
        if kind == "header":
            inner = (f'<tspan x="{INFO_X}" y="{y_text}" class="head">{escape(data)}</tspan>'
                     f'<tspan class="cc"> -{"—"*44}-—-</tspan>')
        elif kind in ("head_sep","blank"):
            inner = f'<tspan x="{INFO_X}" y="{y_text}" class="cc">. </tspan>'
        elif kind == "section":
            inner = (f'<tspan x="{INFO_X}" y="{y_text}" class="accent">- {escape(data)}</tspan>'
                     f'<tspan class="cc"> -{"—"*44}-—-</tspan>')
        elif kind == "field":
            label, value = data
            key_html = "".join(f'<tspan class="{k}">{escape(t)}</tspan>' for k,t in split_key(label))
            inner = (f'<tspan x="{INFO_X}" y="{y_text}" class="cc">. </tspan>'
                     + key_html
                     + f'<tspan class="cc">{escape(dots(label))}</tspan>'
                     + f'<tspan class="value">{escape(value)}</tspan>')
        else:
            inner = (f'<tspan x="{INFO_X}" y="{y_text}" class="cc">. </tspan>'
                     f'<tspan class="value">{escape(data)}</tspan>')
        texts.append(
            f'<g clip-path="url(#lc{i})"><text x="{INFO_X}" y="0" fill="#dbeafe">{inner}</text></g>'
        )
    return clips, texts

def build_ascii_tspans():
    lines = ASCII_ART.strip().splitlines()
    tspans = []
    for i, line in enumerate(lines):
        y = round(ART_Y_REL + i * LINE_H, 2)
        tspans.append(
            f'<tspan x="{ART_X}" y="{y}" xml:space="preserve">{escape(line)}</tspan>'
        )
    total_h = ART_Y_REL + len(lines) * LINE_H
    return tspans, total_h

def make_svg(theme):
    dark = theme == "dark"
    ascii_fill  = "url(#asciiGrad)" if dark else "#1e3a5f"
    val_color   = "#E5E7EB"         if dark else "#1e293b"
    cc_color    = "#475569"         if dark else "#64748b"
    head_color  = "#7C3AED"         if dark else "#4f46e5"
    key_color   = "#22D3EE"         if dark else "#0369a1"
    accent_c    = "#10B981"         if dark else "#059669"
    body_bg     = "url(#bgGlow)"    if dark else "#f0f4ff"
    panel_bg    = "#0B1120"         if dark else "#e2e8f0"
    title_bg    = "#0B1120"         if dark else "#dde4ee"
    scan_c      = "#22D3EE"         if dark else "#0ea5e9"
    bg_stops    = ('<stop offset="0%" stop-color="#0B1120"/><stop offset="100%" stop-color="#050816"/>'
                   if dark else
                   '<stop offset="0%" stop-color="#f0f4ff"/><stop offset="100%" stop-color="#e8edf8"/>')

    ascii_grad = ""
    if dark:
        ascii_grad = """<linearGradient id="asciiGrad" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" stop-color="#22D3EE"><animate attributeName="stop-color" values="#22D3EE;#7C3AED;#38BDF8;#22D3EE" dur="9s" repeatCount="indefinite"/></stop>
    <stop offset="100%" stop-color="#7C3AED"><animate attributeName="stop-color" values="#7C3AED;#38BDF8;#22D3EE;#7C3AED" dur="9s" repeatCount="indefinite"/></stop>
  </linearGradient>"""

    clips, texts = build_info_rows(ROWS)
    n = len(ROWS)
    art_tspans, art_h = build_ascii_tspans()
    SVG_H = max(610, int(art_h) + 100)
    cursor_y = 26 + (n-1) * INFO_LINE_H
    cursor_blink_begin = round(0.75 + n * 0.115, 2)

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{SVG_W}" height="{SVG_H}" viewBox="0 0 {SVG_W} {SVG_H}">
<defs>
  {ascii_grad}
  <linearGradient id="borderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" stop-color="#7C3AED"/><stop offset="50%" stop-color="#22D3EE"/><stop offset="100%" stop-color="#10B981"/>
  </linearGradient>
  <radialGradient id="bgGlow" cx="30%" cy="20%" r="80%">{bg_stops}</radialGradient>
  <linearGradient id="scanGrad" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%"   stop-color="{scan_c}" stop-opacity="0"/>
    <stop offset="45%"  stop-color="{scan_c}" stop-opacity="0.05"/>
    <stop offset="50%"  stop-color="{scan_c}" stop-opacity="0.65"/>
    <stop offset="55%"  stop-color="{scan_c}" stop-opacity="0.05"/>
    <stop offset="100%" stop-color="#7C3AED"   stop-opacity="0"/>
  </linearGradient>
  <pattern id="scanlines" width="4" height="4" patternUnits="userSpaceOnUse">
    <rect width="4" height="1" fill="#7DD3FC" opacity="0.05"/>
  </pattern>
  <filter id="softGlow" x="-50%" y="-50%" width="200%" height="200%">
    <feGaussianBlur stdDeviation="4" result="blur"/>
    <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  <mask id="revealMask" maskUnits="userSpaceOnUse" x="0" y="0" width="{SVG_W}" height="{SVG_H}">
    <rect x="0" y="0" width="{SVG_W}" height="0" fill="#fff">
      <animate attributeName="height" from="0" to="{SVG_H-80}" dur="2.6s" begin="0.2s" fill="freeze" calcMode="spline" keySplines="0.25 0.1 0.25 1"/>
    </rect>
  </mask>
  <!-- clip the ASCII art to stay inside left panel box -->
  <clipPath id="leftPanelClip">
    <rect x="{LEFT_X}" y="26" width="{LEFT_W}" height="{LEFT_H}"/>
  </clipPath>
  {"".join(clips)}
  <style>
    .ascii       {{ font-family: 'Courier New', Consolas, monospace; font-size: {FONT_SIZE}px; fill: {ascii_fill}; letter-spacing: -0.15px; }}
    .key         {{ font-family: 'Courier New', Consolas, monospace; font-size: 15px; fill: {key_color}; font-weight: bold; }}
    .value       {{ font-family: 'Courier New', Consolas, monospace; font-size: 15px; fill: {val_color}; }}
    .cc          {{ font-family: 'Courier New', Consolas, monospace; font-size: 15px; fill: {cc_color}; }}
    .head        {{ font-family: 'Courier New', Consolas, monospace; font-size: 17px; fill: {head_color}; font-weight: bold; }}
    .accent      {{ font-family: 'Courier New', Consolas, monospace; font-size: 15px; fill: {accent_c}; font-weight: bold; }}
    text, tspan  {{ white-space: pre; }}
    .term-label  {{ font-family: 'Courier New', Consolas, monospace; font-size: 12px; fill: #64748B; letter-spacing: 0.5px; }}
    .scan-label  {{ font-family: 'Courier New', Consolas, monospace; font-size: 10px; fill: #F87171; letter-spacing: 1px; }}
    .panel-title {{ font-family: 'Courier New', Consolas, monospace; font-size: 11px; fill: #38BDF8; letter-spacing: 2px; opacity: 0.7; }}
    .cursor-blink {{ fill: {key_color}; }}
  </style>
</defs>

<rect width="{SVG_W}" height="{SVG_H}" rx="18" fill="{body_bg}"/>
<rect width="{SVG_W}" height="{SVG_H}" rx="18" fill="url(#scanlines)"/>

<!-- Title bar -->
<g id="titlebar">
  <rect x="3" y="3" width="{SVG_W-6}" height="34" rx="16" fill="{title_bg}" fill-opacity="0.85"/>
  <circle cx="24" cy="20" r="5" fill="#EF4444"><animate attributeName="opacity" values="1;0.55;1" dur="4s" repeatCount="indefinite"/></circle>
  <circle cx="42" cy="20" r="5" fill="#F59E0B"><animate attributeName="opacity" values="1;0.55;1" dur="4s" begin="0.3s" repeatCount="indefinite"/></circle>
  <circle cx="60" cy="20" r="5" fill="#10B981"><animate attributeName="opacity" values="1;0.55;1" dur="4s" begin="0.6s" repeatCount="indefinite"/></circle>
  <text x="{SVG_W//2}" y="25" text-anchor="middle" class="term-label">{escape(PROMPT)}</text>
  <circle cx="{SVG_W-58}" cy="20" r="4" fill="#F87171">
    <animate attributeName="opacity" values="1;0.15;1" dur="1.1s" repeatCount="indefinite"/>
  </circle>
  <text x="{SVG_W-48}" y="24" class="scan-label">SCANNING</text>
</g>

<g transform="translate(0,38)">
  <!-- Left panel box -->
  <rect x="{LEFT_X}" y="26" width="{LEFT_W}" height="{LEFT_H}" rx="14"
        fill="{panel_bg}" fill-opacity="0.35" stroke="url(#borderGrad)" stroke-width="1" opacity="0.35"/>
  <!-- Right panel box -->
  <rect x="508" y="10" width="655" height="{LEFT_H+16}" rx="14"
        fill="{panel_bg}" fill-opacity="0.35" stroke="url(#borderGrad)" stroke-width="1" opacity="0.35"/>

  <text x="30"  y="24" class="panel-title">VISUAL.MAP</text>
  <text x="524" y="24" class="panel-title">SYSTEM.INFO</text>

  <!-- ASCII art clipped to left panel -->
  <g clip-path="url(#leftPanelClip)">
    <g mask="url(#revealMask)">
      <text x="{ART_X}" y="0" class="ascii">
{"".join(art_tspans)}
      </text>
    </g>
  </g>

  <!-- Info rows (right panel) -->
  {"".join(texts)}

  <!-- Blinking cursor -->
  <rect x="{INFO_X+2}" y="{cursor_y}.0" width="9" height="16" class="cursor-blink" opacity="0">
    <animate attributeName="opacity" values="0;0;1;0;1;0;1;0" keyTimes="0;0.01;0.02;0.3;0.5;0.7;0.85;1"
             dur="1.4s" begin="{cursor_blink_begin}s" repeatCount="indefinite"/>
  </rect>
</g>

<!-- Scanline sweep -->
<rect x="0" y="-70" width="{SVG_W}" height="70" fill="url(#scanGrad)" opacity="0.7" style="mix-blend-mode:screen">
  <animateTransform attributeName="transform" type="translate" from="0 -70" to="0 {SVG_H+70}" dur="4.2s" repeatCount="indefinite"/>
</rect>

<!-- Animated border -->
<rect x="3" y="3" width="{SVG_W-6}" height="{SVG_H-6}" rx="16" fill="none"
      stroke="url(#borderGrad)" stroke-width="2" opacity="0.8">
  <animate attributeName="opacity" values="0.5;0.95;0.5" dur="3.2s" repeatCount="indefinite"/>
</rect>
</svg>"""

Path("/home/claude/dark.svg").write_text(make_svg("dark"),  encoding="utf-8")
Path("/home/claude/light.svg").write_text(make_svg("light"), encoding="utf-8")
print("Done")
