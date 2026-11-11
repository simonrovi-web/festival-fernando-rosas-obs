#!/usr/bin/env python3
"""Panel de muestra del Festival Fernando Rosas: adapta el builder Hallmark de Abastible (misma composición y JS) a la marca FOJI."""
import os, re, base64
SRC = os.path.dirname(os.path.abspath(__file__))
s = open('/home/claude/abastible/hm/build_hm.py').read()
def R(a, b, n=1):
    global s
    assert s.count(a) == n, (a, s.count(a)); s = s.replace(a, b)
R("H = os.path.dirname(os.path.abspath(__file__))", "H = %r" % SRC)
R("A = lambda n: os.path.join(H, 'assets', n)", "A = lambda n: os.path.join(H, 'mat_assets', n)\nP2 = lambda path: 'data:image/png;base64,' + base64.b64encode(open(os.path.join(H, path), 'rb').read()).decode()\nfrom PIL import Image as _I\nimport io as _io\ndef P3(path, w):\n    im = _I.open(os.path.join(H, path)); im.thumbnail((w, w)); b = _io.BytesIO(); im.save(b, 'PNG', optimize=True); return 'data:image/png;base64,' + base64.b64encode(b.getvalue()).decode()")
R("eng = open(os.path.join(H, '..', 'stinger_render.html')).read()", "eng = open(os.path.join(H, 'stinger_render.html')).read()")
R("var OR='#FE5000',OR2='#FF7A33',ORD='#E84800',AZ='#001489',AZ2='#003594',BL='#ffffff';", "var OR='#E9A23B',OR2='#F8D068',ORD='#C9872A',AZ='#1A130D',AZ2='#0B0907',BL='#ffffff';")
R("'--color-paper: oklch(98.2% 0.004 264); --color-paper-2: oklch(95.2% 0.008 264); --color-paper-3: oklch(92% 0.012 264);'", "'--color-paper: oklch(98% 0.008 80); --color-paper-2: oklch(95% 0.014 78); --color-paper-3: oklch(91.5% 0.02 76);'")
R("'--color-ink: oklch(20% 0.075 264); --color-ink-2: oklch(36% 0.06 264); --color-muted: oklch(50% 0.035 264);'", "'--color-ink: oklch(20% 0.02 60); --color-ink-2: oklch(34% 0.025 60); --color-muted: oklch(48% 0.025 65);'")
R("'--color-accent: oklch(30.2% 0.185 264.2); --color-accent-ink: oklch(98.2% 0.004 264); --color-focus: oklch(32% 0.2 264);'", "'--color-accent: #1A130D; --color-accent-ink: oklch(97% 0.012 80); --color-focus: #1A130D;'")
R("'--font-display: \"Ubuntu Sans\", system-ui, sans-serif; --font-body: \"Ubuntu Sans\", system-ui, sans-serif; --font-outlier: \"Titillium Web\", system-ui, sans-serif;'", "'--font-display: \"Playfair Display\", Georgia, serif; --font-body: \"Montserrat\", system-ui, sans-serif; --font-outlier: \"Montserrat\", system-ui, sans-serif;'")
R("'--radius-card: 14px;'", "'--radius-card: 4px;'")
R("--tracking-display: -0.025em; --display-weight: 800;", "--tracking-display: 0em; --display-weight: 700;")
R("""  /* the orange field carries the page (posture: committed); the blue is the signal */
  --color-field: oklch(66.9% 0.220 37.7); --color-field-2: oklch(62.4% 0.206 37.6); --color-field-ink: oklch(20% 0.075 264);
  --color-band: oklch(30.2% 0.185 264.2); --color-band-ink: oklch(98.2% 0.004 264); --color-band-2: oklch(84% 0.04 264);
  --color-scrim: oklch(16% 0.06 264 / 0.86); --color-frame: oklch(20% 0.075 264 / 0.22); --color-check-1: oklch(91% 0.01 264); --color-check-2: oklch(96% 0.006 264);""",
"""  /* the warm black of the theatre carries the page; the gold of the logo is the signal */
  --color-field: #1A130D; --color-field-2: #0B0907; --color-field-ink: oklch(97% 0.012 80);
  --color-band: #0B0907; --color-band-ink: oklch(96% 0.012 80); --color-band-2: oklch(82% 0.035 75);
  --color-scrim: oklch(12% 0.015 60 / 0.88); --color-frame: oklch(20% 0.02 60 / 0.22); --color-check-1: oklch(91% 0.012 75); --color-check-2: oklch(96% 0.008 75);""")
R("--brand-orange: #FE5000; --brand-orange-2: #FF7A33; --brand-orange-3: #E84800; --brand-blue: #001489; --brand-blue-2: #003594; --brand-white: #FFFFFF; --brand-grey: #6A6A6A;",
  "--brand-orange: #E9A23B; --brand-orange-2: #F8D068; --brand-orange-3: #E9A23B; --brand-blue: #1A130D; --brand-blue-2: #0B0907; --brand-white: #FFFFFF; --brand-grey: #8C7E6A;\n  --brand-mist: #F8D068; --brand-red-hover: #D18E28; --brand-on-red: #0B0907;\n  --imp-1: #1A130D; --imp-2: #0B0907; --imp-3: #E9A23B; --imp-4: #F8D068; --imp-5: #7A1420; --imp-6: #F6F0E6;")
# comment header of the CSS
s = re.sub(r"\* paper: .*?v2\.0\.0 \*/", "* brand: FOJI 25 años (foji.cl) · display: Playfair Display 700 · body: Montserrat · posture: committed (the theatre's warm black carries the hero and the live-graphics band; the logo gold is the signal) · signature: the kit's own stingers passing the studio frame to the next screen · v1 */", s, flags=re.S)
R("/* the brand's own swatches", "/* the brand's own swatches")
# extra css for the typographic seal
R("assert 'tk(\\'--brand-orange\\')' in ENG", "assert 'tk(\\'--brand-orange\\')' in ENG\nENG = ENG.replace('color:#fff;white-space:nowrap;text-align:center', 'color:'+chr(39)+'+BL+'+chr(39)+';white-space:nowrap;text-align:center').replace('color:#C9D7EA', 'color:'+chr(39)+'+tk(\\'--brand-mist\\')+'+chr(39)+'')")
R("@media (max-width: 40rem) {", """.stingers--two { grid-template-columns: repeat(2, minmax(0, 1fr)); }
@media (max-width: 40rem) { .stingers--two { grid-template-columns: minmax(0, 1fr); } }
.spec .face { font-family: var(--font-display); font-weight: 700; letter-spacing: 0; }
.spec .face--alt { font-family: var(--font-body); font-weight: 500; }
.hero .btn { background: var(--brand-orange-3); border-color: var(--brand-orange-3); color: var(--brand-on-red); }
.hero .btn:hover { background: var(--brand-red-hover); border-color: var(--brand-red-hover); color: var(--brand-on-red); }
.hero .btn--quiet, .band .btn--quiet { background: transparent; color: var(--color-field-ink); border-color: var(--color-field-ink); }
.hero .btn--quiet:hover, .band .btn--quiet:hover { background: var(--color-field-2); }
.top a:focus-visible, .hero .btn:focus-visible, .band .btn:focus-visible { outline-color: var(--color-field-ink); }
@media (max-width: 40rem) {""")
# body
a = s.index("SCREENS = [('inicio'"); b = s.index("for k, v in rep.items():")
s = s[:a] + open(os.path.join(SRC, 'material_body.py')).read() + '\n' + s[b:]
# hero loop
R("names=['ESTUDIO','ORADOR','AGENDA'],des=[['ola','Ola'],['burbuja','Burbuja'],['mosaico','Mosaico']]", "names=['ESTUDIO','ORQUESTA','PROGRAMA'],des=[['telon','Telón'],['destello','Destello'],['marco','Marco']]")
R("// the six stingers", "// the four stingers")
R("<title>Material de transmisión · Abastible</title>", "<title>Material Festival Fernando Rosas</title>")
R("del evento Abastible en OBS.", "del XX Festival Fernando Rosas en OBS.")
R("open(os.path.join(H, 'index.html'), 'w').write(HTML)", "open(os.path.join(H, 'material_index.html'), 'w').write(HTML)")
exec(compile(s, 'build_material_gen', 'exec'))
