s=open('build.py').read()
def R(a,b):
    global s
    c=s.count(a); assert c>=1,(a[:70],c); s=s.replace(a,b)
R('"""Gráficos de la Ceremonia de Titulación UCSH para OBS (carpeta out/): pantallas completas, overlays y PiP.\nDirección: académica solemne. Azul institucional y oro del logo de ucsh.cl, nombres en Cormorant Garamond, texto en Ubuntu (la letra del sitio)."""',
  '"""Gráficos del XX Festival Fernando Rosas (FOJI 25 años) para OBS (carpeta out/): pantallas completas, overlays y PiP.\nDirección: gala de teatro. Negro cálido y el dorado del logo FOJI 25 años, títulos en Playfair Display, texto en Montserrat (la letra de foji.cl)."""')
R("""    face('Cormorant Garamond', 'cormorant-garamond/files/cormorant-garamond-latin-600-normal.woff2', 600),
    face('Cormorant Garamond', 'cormorant-garamond/files/cormorant-garamond-latin-700-normal.woff2', 700),
    face('Ubuntu', 'ubuntu/files/ubuntu-latin-400-normal.woff2', 400),
    face('Ubuntu', 'ubuntu/files/ubuntu-latin-500-normal.woff2', 500),
    face('Ubuntu', 'ubuntu/files/ubuntu-latin-700-normal.woff2', 700),""",
"""    face('Playfair Display', 'playfair-display/files/playfair-display-latin-600-normal.woff2', 600),
    face('Playfair Display', 'playfair-display/files/playfair-display-latin-700-normal.woff2', 700),
    face('Montserrat', 'montserrat/files/montserrat-latin-400-normal.woff2', 400),
    face('Montserrat', 'montserrat/files/montserrat-latin-500-normal.woff2', 500),
    face('Montserrat', 'montserrat/files/montserrat-latin-700-normal.woff2', 700),""")
R("# Logo de ucsh.cl (1861×945, azul y oro) pasado a blanco y oro para los fondos azules.\nLOGO = png('../Logo_UCSH_blanco.png', 520)",
  "# Logo FOJI 25 años de foji.cl (blanco y dorado, 824×265), recortado.\nLOGO = png('../Logo_FOJI25.png', 560)")
R(":root{--nv:#004577;--nv2:#0A5A92;--dk:#012A4A;--dk2:#011C33;--au:#F0B808;--au2:#FFD24D;--au3:#C99A06;--cel:#14A2F1;",
  ":root{--nv:#2A1E14;--nv2:#3A2A1B;--dk:#120E0A;--dk2:#0B0907;--au:#E9A23B;--au2:#F8D068;--au3:#C9872A;--cel:#F8D068;")
R("--mu:#B9CCE0","--mu:#C9B99E")
R('"Ubuntu"','"Montserrat"'); R('"Cormorant Garamond"','"Playfair Display"')
R("radial-gradient(1400px 700px at 50% -10%,rgba(20,162,241,.28),transparent 64%),radial-gradient(900px 500px at 50% 118%,rgba(240,184,8,.10),transparent 70%),linear-gradient(180deg,#0A5A92 0%,#004577 36%,#012A4A 100%)",
  "radial-gradient(1100px 760px at 50% -18%,rgba(248,208,104,.26),transparent 62%),radial-gradient(1000px 520px at 50% 120%,rgba(122,20,32,.35),transparent 70%),linear-gradient(180deg,#2A1E14 0%,#17110C 42%,#0B0907 100%)")
R("radial-gradient(1400px 700px at 50% -10%,rgba(20,162,241,.28),transparent 64%),linear-gradient(180deg,#0A5A92 0%,#004577 36%,#012A4A 100%)",
  "radial-gradient(1100px 760px at 50% -18%,rgba(248,208,104,.22),transparent 62%),linear-gradient(180deg,#2A1E14 0%,#17110C 42%,#0B0907 100%)")
R("240,184,8","233,162,59"); R("1,28,51","14,10,7"); R("1,20,38","6,4,2"); R("0,69,119","42,30,20"); R("1,42,74","18,13,9")
R('<b data-ev="web">ucsh.cl</b><span data-ev="hashtag">#TitulaciónUCSH</span>','<b data-ev="web">foji.cl</b><span data-ev="hashtag">#FestivalFernandoRosas</span>')
R("'ucsh-live'","'ffr-live'"); R("'ucsh'","'ffr'")
R("P['UCSH_","P['FFR_"); R("'Titulación UCSH · ","'Festival Fernando Rosas · ")
R("Fecha de la ceremonia","Viernes 27 de noviembre"); R("Lugar de la ceremonia","Teatro Municipal de Santiago"); R("Dirección, Santiago","Agustinas 794, Santiago")
R('alt="Universidad Católica Silva Henríquez"','alt="FOJI 25 años"'); R('alt="UCSH"','alt="FOJI"'); R('#TitulaciónUCSH','#FestivalFernandoRosas')
R('<div class="kick" data-ev="kicker_ini">Ceremonia de</div><div class="k2">Titulación</div>','<div class="kick" data-ev="kicker_ini">XX</div><div class="k2">Festival Fernando Rosas</div>')
R('.k2{font-family:"Playfair Display";font-weight:600;font-size:210px;','.k2{font-family:"Playfair Display";font-weight:700;font-size:150px;')
R('<div class="lema" data-ev="lema" data-evshow="lema">Universidad Católica Silva Henríquez</div>','<div class="lema" data-ev="lema" data-evshow="lema">FOJI 25 años · Teatro Municipal de Santiago</div>')
R("Inicio 19:00 h","Inicio 15:00 h"); R('<b id="cd">19:00</b>','<b id="cd">15:00</b>')
R("# =========================================================== CARRERA (antes de llamar a sus titulados)","# =========================================================== ORQUESTA (antes de que toque)")
R("P['FFR_Carrera']","P['FFR_Orquesta']"); R("'Festival Fernando Rosas · Carrera'","'Festival Fernando Rosas · Orquesta'")
R('<div class="n" id="sn">Carrera 1 de 6</div><div class="kick">Titulación</div><div class="s" id="ss" data-fit="h" data-max="150" data-min="70">Nombre de la carrera</div>',
  '<div class="n" id="sn">Orquesta 1 de 7</div><div class="kick">En escena</div><div class="s" id="ss" data-fit="h" data-max="140" data-min="64">Nombre de la orquesta</div>')
R('<div class="z" id="sz"><b>24</b> titulados</div>','<div class="z" id="sz">Comuna, Región</div><div class="dr" id="sd">Dirección <b>Nombre Apellido</b></div>')
R(".z b{color:var(--au2);font-weight:500}",".z b{color:var(--au2);font-weight:500}\n.dr{font-size:32px;margin-top:14px;color:var(--mu);animation:up .8s .6s ease both}.dr b{color:var(--wh);font-weight:500}")
R("document.getElementById('ss').textContent=g.t||'Nombre de la carrera';var n=L.length?g.b-g.a+1:0;\n document.getElementById('sz').innerHTML=n?('<b>'+n+'</b> '+(n===1?'titulado':'titulados')):'';\n document.getElementById('sn').textContent=C.length?'Carrera '+(C.indexOf(g.t)+1)+' de '+C.length:'';",
  "var it=L[c]||{};document.getElementById('ss').textContent=g.t||'Nombre de la orquesta';\n document.getElementById('sz').textContent=it.e||'';var sd=document.getElementById('sd');sd.innerHTML=it.h?'Dirección <b>'+esc(it.h)+'</b>':'';\n document.getElementById('sn').textContent=C.length?'Orquesta '+(C.indexOf(g.t)+1)+' de '+C.length:'';")
R("k=JSON.stringify([g.t,g.a,g.b,C.length])","k=JSON.stringify([g.t,g.a,g.b,C.length,(L[c]||{}).e,(L[c]||{}).h])")
R("document.querySelectorAll('.n,.kick,.s,.rule,.z')","document.querySelectorAll('.n,.kick,.s,.rule,.z,.dr')")
R("# =========================================================== NÓMINA (titulados de la carrera en curso)","# =========================================================== PROGRAMA (obras de la orquesta en escena)")
R("P['FFR_Nomina']","P['FFR_Programa']"); R("'Festival Fernando Rosas · Nómina'","'Festival Fernando Rosas · Programa'")
R('<div class="kick">Nómina de titulados</div><b id="hb">Nombre de la carrera</b>','<div class="kick">Programa</div><b id="hb">Nombre de la orquesta</b>')
R("document.getElementById('hb').textContent=g.t||'Carrera';document.getElementById('hn').textContent=n?(n+(n===1?' titulado':' titulados')):'';",
  "var i0=L[g.a]||{};document.getElementById('hb').textContent=g.t||'Orquesta';document.getElementById('hn').textContent=[i0.e,i0.h?'Dirección '+i0.h:''].filter(Boolean).join(' · ');")
R("var cols=n<=10?1:n<=24?2:n<=45?3:4,rows=Math.max(1,Math.ceil(n/cols)),fs=Math.max(18,Math.min(36,Math.floor(600/rows*.5)));if(cols===1)rows=Math.max(rows,8);",
  "var cols=n<=7?1:n<=14?2:3,rows=Math.max(1,Math.ceil(n/cols)),fs=Math.max(22,Math.min(44,Math.floor(600/rows*.42)));if(cols===1)rows=Math.max(rows,6);")
R("<span>'+esc(it.o||'')+'</span>'","<span class=\"ob\">'+esc(it.o||'')+'</span>'")
R(".it small{flex:none;font-size:.6em;color:var(--au2);letter-spacing:1px;text-transform:uppercase}",".it{justify-content:space-between}.it .ob{font-family:\"Playfair Display\";font-weight:600}\n.it small{flex:none;font-size:.62em;color:var(--mu);letter-spacing:.5px}")
R("<div class=\"t\" id=\"pt\">Volvemos en unos minutos</div>","<div class=\"t\" id=\"pt\">Intermedio</div>")
R("p.titulo||'Volvemos en unos minutos'","p.titulo||'Intermedio'")
R('<div class="kick">Felicitaciones, titulados</div>','<div class="kick">Gracias</div>')
R('<div class="s" id="fs" data-ev="nombre">Ceremonia de Titulación 2026</div>','<div class="s" id="fs" data-ev="nombre">XX Festival Fernando Rosas</div>')
R("# =========================================================== LOWER THIRD (un titulado)","# =========================================================== LOWER THIRD (la obra que suena o una persona)")
R('<div class="ds" id="ds">Distinción</div>','<div class="ds" id="ds">Orquesta</div>')
R(">Nombre Apellido Apellido</div><div class=\"cg\" id=\"cg\">Carrera</div>",">Nombre de la obra</div><div class=\"cg\" id=\"cg\">Compositor</div>")
R("lt:{nombre:'Nombre Apellido Apellido',cargo:'Pedagogía en Historia y Geografía',empresa:'Distinción máxima'}","lt:{nombre:'Danzas eslavas op. 46 n.º 8',cargo:'Antonín Dvořák',empresa:'Orquesta Juvenil de Ejemplo'}")
R("'Festival Fernando Rosas · Carrera en pantalla'","'Festival Fernando Rosas · Orquesta en pantalla'")
R('<div class="k" id="tk">Carrera</div><div class="t" id="tt">Nombre de la carrera</div>','<div class="k" id="tk">Orquesta</div><div class="t" id="tt">Nombre de la orquesta</div>')
R("t.kicker||'Carrera'","t.kicker||'Orquesta'")
R('<span id="zl">Felicitaciones</span>','<span id="zl">Saludos</span>'); R("m.label||'Felicitaciones'","m.label||'Saludos'")
R(".mo img{width:220px;",".mo img{width:250px;")
s=s.replace("'UCSH_PIP_'","'FFR_PIP_'")
s=s.replace("if f.startswith('IMP_'): os.remove('out/' + f)","if not f.startswith('FFR_'): os.remove('out/' + f)")
open('build.py','w').write(s)
import re;print(re.findall(r'.{25}(?:UCSH|ucsh|itulad|arrera|Nómina).{25}',s))
