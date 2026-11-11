#!/usr/bin/env python3
"""Adapta las fuentes del kit Titulación UCSH al XX Festival Fernando Rosas (FOJI 25 años), una sola vez.
Modelo de datos: un ítem por obra → t = orquesta, e = comuna y región, h = dirección, o = obra, c = compositor."""
import re
def R(s, a, b, n=1):
    c = s.count(a); assert c == n, (a[:90], c); return s.replace(a, b)
GLOBAL = [('Titulación UCSH', 'Festival Fernando Rosas'), ('#TitulaciónUCSH', '#FestivalFernandoRosas'), ('UCSH_', 'FFR_'), ('UCSH ', 'FFR '), ("'ucsh'", "'ffr'"), ('"ucsh"', '"ffr"'),
          ('ucsh-', 'ffr-'), ('ucsh.cl', 'foji.cl'), ('UCSH', 'FFR')]
def glob(s):
    for a, b in GLOBAL: s = s.replace(a, b)
    return s

s = glob(open('control_a.js').read())
i = s.index('var DEMO=['); j = s.index('var S=ls(', i)
s = s[:i] + """var DEMO=[{t:'Orquesta Juvenil de Ejemplo',e:'Comuna, Región',h:'Nombre Apellido',o:'Danzas eslavas op. 46 n.º 8',c:'Antonín Dvořák'},
 {t:'Orquesta Juvenil de Ejemplo',e:'Comuna, Región',h:'Nombre Apellido',o:'Obra chilena',c:'Compositor chileno'},
 {t:'Orquesta Infantil de Ejemplo',e:'Comuna, Región',h:'Nombre Apellido',o:'Sinfonía n.º 1, I. Allegro',c:'Ludwig van Beethoven'},
 {t:'Orquesta Infantil de Ejemplo',e:'Comuna, Región',h:'Nombre Apellido',o:'Libertango',c:'Astor Piazzolla'},
 {t:'OSNJ y Orquesta Filarmónica de Santiago',e:'Concierto de gala · 19:00',h:'Paolo Bortolameolli',o:'Obra del programa',c:'Compositor'}];
""" + s[j:]
s = R(s, "S.ev=S.ev||{nombre:'Ceremonia de Titulación 2026',lema:'Universidad Católica Silva Henríquez',fecha:'Fecha de la ceremonia',hora:'19:00',lugar:'Lugar de la ceremonia',dir:'Dirección, Santiago',web:'foji.cl',hashtag:'#FestivalFernandoRosas',kicker_ini:'Ceremonia de'};",
      "S.ev=S.ev||{nombre:'XX Festival Fernando Rosas',lema:'FOJI 25 años · Teatro Municipal de Santiago',fecha:'Viernes 27 de noviembre',hora:'15:00',lugar:'Teatro Municipal de Santiago',dir:'Agustinas 794, Santiago',web:'foji.cl',hashtag:'#FestivalFernandoRosas',kicker_ini:'XX'};")
s = R(s, "S.tema=S.tema||{k:'Carrera',t:'',sub:false};", "S.tema=S.tema||{k:'Orquesta',t:'',sub:true};")
s = R(s, "S.msgz=S.msgz||{label:'Felicitaciones',items:['Felicitaciones a todas y todos los titulados de la FFR','Envía tu saludo por el chat de la transmisión'],every:10};",
      "S.msgz=S.msgz||{label:'Saludos',items:['20 años del Festival Fernando Rosas y 25 años de FOJI','Envía tu saludo a las orquestas por el chat de la transmisión'],every:10};")
s = R(s, "S.ora=S.ora||{kicker:'Titulado'};", "S.ora=S.ora||{kicker:'Orquesta'};")
s = R(s, "tema:{kicker:T(S.tema.k)||'Carrera',titulo:tt,sub:''},", "tema:{kicker:T(S.tema.k)||'Orquesta',titulo:tt,sub:S.tema.sub&&!T(S.tema.t)?(T(curItem().e)):''},")
s = R(s, "$('air-blk').textContent='TITULADO '+(S.cur+1)+' DE '+S.ag.length;$('m_n').textContent='TITULADO '+(S.cur+1);$('m_t').textContent=(it.o||'—')+(it.t?' · '+it.t:'');",
      "$('air-blk').textContent='OBRA '+(S.cur+1)+' DE '+S.ag.length;$('m_n').textContent='OBRA '+(S.cur+1);$('m_t').textContent=(it.o||'—')+(it.t?' · '+it.t:'');")
s = R(s, "var COLS=['t','o','c'];", "var COLS=['t','e','h','o','c'];")
s = R(s, "({t:'Carrera',o:'Nombre del titulado',c:'Distinción (opcional)'})[k]", "({t:'Orquesta',e:'Comuna, región',h:'Dirección',o:'Obra',c:'Compositor'})[k]")
s = R(s, "toast('Titulado '+(i+1)+': '+(it.o||''));", "toast('Obra '+(i+1)+': '+(it.o||''));")
s = R(s, "S.ag.push({t:l?l.t:'',o:'',c:''});", "S.ag.push({t:l?l.t:'',e:l?l.e:'',h:l?l.h:'',o:'',c:''});")
i = s.index(" var CA='',OUT=[],nb=true;"); j = s.index("S.ag=OUT.filter(function(x){return x.o});", i)
s = s[:i] + (" var G={t:'',e:'',h:''},OUT=[],nb=true;RAW.forEach(function(l){if(!l){nb=true;return}var p=l.split(/\\t|\\|/).map(function(x){return x.trim()});"
    "if(p.length>=5){nb=false;G={t:p[0]||G.t,e:p[1]||G.e,h:p[2]||G.h};OUT.push({t:G.t,e:G.e,h:G.h,o:p[3]||'',c:p[4]||''});return}"
    "if(nb||/:$/.test(p[0])&&p.length===1){G={t:p[0].replace(/:$/,'').trim(),e:p[1]||'',h:p[2]||''};nb=false;return}"
    "OUT.push({t:G.t,e:G.e,h:G.h,o:p[0]||'',c:p[1]||''})});") + s[j:]
s = R(s, "toast(S.ag.length+' titulados cargados en '+carreras().length+' carreras')};", "toast(S.ag.length+' obras cargadas de '+carreras().length+' orquestas')};")
s = R(s, "ltShow(p.n?{nombre:T(p.n),cargo:T(p.e),empresa:T(p.c)}:{nombre:T(p.o),cargo:T(p.t),empresa:T(p.c)})}",
      "ltShow(p.n?{nombre:T(p.n),cargo:T(p.c),empresa:T(p.e),tipo:'persona'}:{nombre:T(p.o),cargo:T(p.c),empresa:T(p.t),tipo:'obra'})}")
s = R(s, "if(!p||!T(p.o||p.n))return toast('Esa fila no tiene nombre');", "if(!p||!T(p.o||p.n))return toast('Esa fila no tiene obra');")
s = R(s, "var n=T(it.o);if(!n)return;var k=n+'|'+T(it.t);if(seen[k])return;seen[k]=1;L.push({n:n,c:T(it.c),e:T(it.t),src:'ag',i:i})",
      "var n=T(it.h);if(!n)return;var k=n+'|'+T(it.t);if(seen[k])return;seen[k]=1;L.push({n:n,c:'Dirección',e:T(it.t),src:'ag',i:i})")
open('control_a.js', 'w').write(s)
print('control_a restos', re.findall(r'.{20}(?:itulad|arrera|istinci).{20}', s)[:8])

h = glob(open('control_head.html').read())
h = R(h, ":root{--or:#F0B808;--or2:#FFD24D;--az:#004577;--az2:#0A5A92;", ":root{--or:#E9A23B;--or2:#F8D068;--az:#1A1612;--az2:#2A231C;")
h = h.replace('"Ubuntu"', '"Montserrat"')
h = R(h, 'button.pri:hover{background:#D9A400;border-color:#D9A400}', 'button.pri:hover{background:#D18E28;border-color:#D18E28}')
h = h.replace('/* FFR: la tabla de titulados necesita más ancho que el programa original */', '/* FFR: la tabla del programa necesita más ancho que el original */')
h = R(h, '<h2>Titulados por carrera <span class="sp"><span class="onair v" id="air-blk">TITULADO 1</span>', '<h2>Programa por orquesta <span class="sp"><span class="onair v" id="air-blk">OBRA 1</span>')
h = R(h, '<th>#</th><th>Carrera</th><th>Titulado</th><th>Distinción</th><th></th>', '<th>#</th><th>Orquesta</th><th>Comuna, región</th><th>Dirección</th><th>Obra</th><th>Compositor</th><th></th>')
h = R(h, '> Al pasar al siguiente titulado, mostrar su lower third</label>', '> Al pasar a la siguiente obra, mostrar su lower third</label>')
h = R(h, '> Al cambiar de carrera, actualizar la carrera en pantalla</label>', '> Al cambiar de orquesta, actualizar la orquesta en pantalla</label>')
h = R(h, '<summary>Pegar la lista de titulados (uno por línea, desde Excel o texto)</summary>', '<summary>Pegar el programa (una obra por línea, desde Excel o texto)</summary>')
i = h.index('<p class="hint" style="margin:6px 0">Formato: <kbd>Carrera'); j = h.index('</p>', i) + 4
h = h[:i] + '<p class="hint" style="margin:6px 0">Formato: <kbd>Orquesta | Comuna, región | Dirección | Obra | Compositor</kbd>, una obra por línea; también sirve copiar esas cinco columnas desde Excel. O por bloques: <kbd>Orquesta | Comuna, región | Dirección</kbd> en una línea, debajo sus obras como <kbd>Obra | Compositor</kbd>, y una línea en blanco antes de la orquesta siguiente.</p>' + h[j:]
h = re.sub(r'placeholder="Trabajo Social \| Nombre Apellido Apellido \| Distinción máxima"', 'placeholder="Orquesta Juvenil de Ejemplo | Comuna, Región | Nombre Apellido | Danzas eslavas op. 46 n.º 8 | Antonín Dvořák"', h)
h = R(h, '>Cargar titulados</button>', '>Cargar programa</button>')
h = R(h, '>↺ Lista de ejemplo</button>', '>↺ Programa de ejemplo</button>')
h = R(h, '>Titulado actual</button>', '>Obra actual</button>')
h = R(h, 'placeholder="Carrera o cargo"', 'placeholder="Compositor o cargo"')
h = R(h, 'placeholder="Distinción (opcional)"', 'placeholder="Orquesta (opcional)"')
h = R(h, '<h2>Carrera en pantalla ', '<h2>Orquesta en pantalla ')
h = h.replace('Etiqueta arriba a la izquierda con la carrera que se está titulando. Se actualiza sola al cambiar de carrera.', 'Etiqueta arriba a la izquierda con la orquesta que está tocando. Se actualiza sola al cambiar de orquesta.')
h = h.replace('Texto (vacío = carrera actual)', 'Texto (vacío = orquesta actual)').replace('placeholder="Carrera actua', 'placeholder="Orquesta actua')
h = R(h, '<input id="or_k" value="Titulado">', '<input id="or_k" value="Orquesta">')
h = R(h, 'Momentos por titulado', 'Momentos por obra')
h = R(h, 'con el número del titulado (FFR T003 …)', 'con el número de la obra (FFR T003 …)')
h = R(h, '▶ Resumen del titulado', '▶ Resumen de la obra')
h = R(h, '🗑 Borrar otros titulados', '🗑 Borrar otras obras')
open('control_head.html', 'w').write(h)
print('head restos', re.findall(r'.{20}(?:itulad|arrera|istinci|Ubuntu).{20}', h)[:8])

m = glob(open('make_control.py').read())
for a, b in [("['FFR Carrera en pantalla','FFR_Overlay_Tema']", "['FFR Orquesta en pantalla','FFR_Overlay_Tema']"),
             ("{scene:'CARRERA',src:[['FFR Carrera','FFR_Carrera']]}", "{scene:'ORQUESTA',src:[['FFR Orquesta','FFR_Orquesta']]}"),
             ("{scene:'NOMINA',src:[['FFR Nomina','FFR_Nomina']]}", "{scene:'PROGRAMA',src:[['FFR Programa','FFR_Programa']]}"),
             ("'FFR_Carrera','FFR_Nomina'", "'FFR_Orquesta','FFR_Programa'"),
             ("<b>TITULADO '+g.num", "<b>OBRA '+g.num"), ("' titulados)':''", "' obras)':''")]:
    m = R(m, a, b)
open('make_control.py', 'w').write(m)
t = glob(open('hst.js').read()); open('hst.js', 'w').write(t)
print('ok')
