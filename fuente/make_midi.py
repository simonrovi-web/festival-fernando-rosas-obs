#!/usr/bin/env python3
"""PANEL_MIDI del Festival Fernando Rosas: parte del panel probado del kit Abastible y cambia canal, marca, escenas y acciones."""
import re
s = open('/home/claude/abastible/midi_template.html').read()
def R(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (a[:70], c); s = s.replace(a, b)
for a, b in [('ABAS_', 'FFR_'), ('ABAS ', 'FFR '), ("'abas-cmd'", "'ffr-cmd'"), ('abas-midi', 'ffr-midi'), ('abastible.cl', 'foji.cl'), ('ABASTIBLE', 'FFR'), ('Abastible', 'Festival Fernando Rosas')]:
    s = s.replace(a, b)
R(':root{--red:#FE5000;--red2:#FF7A33;--ink:#F3F5FB;--mute:#9AA3C7;--line:rgba(255,255,255,.12);--card:#0B1442;--bg:#050A2C;',
  ':root{--red:#E9A23B;--red2:#F8D068;--ink:#F6F0E6;--mute:#C9B99E;--line:rgba(255,255,255,.12);--card:#221A12;--bg:#0E0A07;')
s = s.replace('"Ubuntu Sans"', '"Montserrat"')
s = s.replace("['prev','◀ Bloque anterior'],['next','Bloque siguiente ▶']", "['prev','◀ Obra anterior'],['next','Obra siguiente ▶']")
s = s.replace("prev:'◀ BLOQUE',next:'BLOQUE ▶'", "prev:'◀ OBRA',next:'OBRA ▶'")
s = s.replace("['lt_cur','👤 Lower third del orador actual']", "['lt_cur','🎼 Lower third de la obra actual']").replace("lt_cur:'👤 ORADOR'", "lt_cur:'🎼 OBRA'")
s = s.replace("['tgl_tema','Mostrar/ocultar tema']", "['tgl_tema','Mostrar/ocultar orquesta en pantalla']").replace("tgl_tema:'TEMA'", "tgl_tema:'ORQUESTA'")
s = s.replace("['reel','▶ Resumen del bloque']", "['reel','▶ Resumen de la obra']")
i = s.index("['hst_go','🎬 Con la animación elegida']"); j = s.index("]]]", i)
s = s[:i] + "['hst_go','🎬 Con la animación elegida'],['hst_telon','Telón'],['hst_destello','Destello'],['hst_franjas','Franjas'],['hst_marco','Marco']]]" + s[j + 3:]
s = s.replace("hst_ola:'TRANSICIÓN HTML',hst_burbuja:'TRANSICIÓN HTML',hst_capsulas:'TRANSICIÓN HTML',hst_llama:'TRANSICIÓN HTML',hst_anillos:'TRANSICIÓN HTML',hst_mosaico:'TRANSICIÓN HTML'",
              "hst_telon:'TRANSICIÓN HTML',hst_destello:'TRANSICIÓN HTML',hst_franjas:'TRANSICIÓN HTML',hst_marco:'TRANSICIÓN HTML'")
s = s.replace("hst_ola:'🎬 OLA',hst_burbuja:'🎬 BURBUJA',hst_capsulas:'🎬 CÁPSULAS',hst_llama:'🎬 LLAMA',hst_anillos:'🎬 ANILLOS',hst_mosaico:'🎬 MOSAICO'",
              "hst_telon:'🎬 TELÓN',hst_destello:'🎬 DESTELLO',hst_franjas:'🎬 FRANJAS',hst_marco:'🎬 MARCO'")
s = s.replace("case 'hst_ola':case 'hst_burbuja':case 'hst_capsulas':case 'hst_llama':case 'hst_anillos':case 'hst_mosaico':", "case 'hst_telon':case 'hst_destello':case 'hst_franjas':case 'hst_marco':")
s = s.replace("'hst_go','hst_mosaico'],", "'hst_go','hst_telon'],")
R("var TRD=['FFR Ola','FFR Ola Corta','FFR Burbuja','FFR Burbuja Corta','FFR Capsulas','FFR Llama','FFR Anillos','FFR Mosaico','Corte','Desvanecer']",
  "var TRD=['FFR Telon','FFR Telon Corta','FFR Destello','FFR Destello Corta','FFR Franjas','FFR Marco','Corte','Desvanecer']")
s = s.replace("['INICIO','ESTUDIO','ORADOR','AGENDA','PAUSA','REPLAY','FINAL']", "['INICIO','ESTUDIO','ORQUESTA','PROGRAMA','PAUSA','REPLAY','FINAL','PIP_PRESENTACION','PIP_ESQUINA']")
left = re.findall(r'.{25}(?:ola\b|burbuja|mosaico|Orador|ORADOR|charla).{25}', s)
s = s.replace('button.pri{background:var(--red);border-color:var(--red);color:var(--bg)}','button.pri{background:var(--red);border-color:var(--red);color:var(--bg)}')
s = s.replace('.ab.sel{background:var(--red);border-color:#fff;color:var(--bg)}','.ab.sel{background:var(--red);border-color:#fff;color:var(--bg)}')
s = s.replace('</style>', 'button.pri:hover{background:#D18E28;border-color:#D18E28;color:var(--bg)}\n</style>', 1)
print('restos:', len(left)); [print('  ', x) for x in left[:8]]
open('midi_template.html', 'w').write(s)
