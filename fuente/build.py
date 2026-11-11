#!/usr/bin/env python3
"""Gráficos del XX Festival Fernando Rosas (FOJI 25 años) para OBS (carpeta out/): pantallas completas, overlays y PiP.
Dirección: gala de teatro. Negro cálido y el dorado del logo FOJI 25 años, títulos en Playfair Display, texto en Montserrat (la letra de foji.cl)."""
import base64, io, os
from PIL import Image

B = lambda p: base64.b64encode(open(p, 'rb').read()).decode()
F = 'node_modules/@fontsource/'
def face(fam, path, w):
    return '@font-face{font-family:"%s";font-weight:%d;font-display:block;src:url(data:font/woff2;base64,%s) format("woff2");}' % (fam, w, B(F + path))
FONTS = ''.join([
    face('Playfair Display', 'playfair-display/files/playfair-display-latin-600-normal.woff2', 600),
    face('Playfair Display', 'playfair-display/files/playfair-display-latin-700-normal.woff2', 700),
    face('Montserrat', 'montserrat/files/montserrat-latin-400-normal.woff2', 400),
    face('Montserrat', 'montserrat/files/montserrat-latin-500-normal.woff2', 500),
    face('Montserrat', 'montserrat/files/montserrat-latin-700-normal.woff2', 700),
])

def png(path, w):
    im = Image.open(path); im.thumbnail((w, w * 3), Image.LANCZOS); b = io.BytesIO(); im.save(b, 'PNG', optimize=True)
    return 'data:image/png;base64,' + base64.b64encode(b.getvalue()).decode()
# Logo FOJI 25 años de foji.cl (blanco y dorado, 824×265), recortado.
LOGO = png('../Logo_FOJI25.png', 560)

BASE = r'''
:root{--nv:#2A1E14;--nv2:#3A2A1B;--dk:#120E0A;--dk2:#0B0907;--au:#E9A23B;--au2:#F8D068;--au3:#C9872A;--cel:#F8D068;
 --wh:#FFFFFF;--mu:#C9B99E;--ink:#0B2238}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1920px;height:1080px;overflow:hidden;font-family:"Montserrat",sans-serif;color:var(--wh)}
.sf{font-family:"Playfair Display",serif}
@keyframes up{from{opacity:0;transform:translateY(34px)}to{opacity:1;transform:none}}
@keyframes left{from{opacity:0;transform:translateX(-60px)}to{opacity:1;transform:none}}
@keyframes rise{from{opacity:0;transform:translateY(40px);filter:blur(6px)}to{opacity:1;transform:none;filter:none}}
@keyframes grow{from{transform:scaleX(0)}to{transform:scaleX(1)}}
@keyframes fade{from{opacity:0}to{opacity:1}}
@keyframes pulse{50%{opacity:.35}}
.hide{display:none!important}
'''
FULL = r'''
body{background:var(--dk)}
.stage{position:relative;width:1920px;height:1080px;overflow:hidden;
 background:radial-gradient(1100px 760px at 50% -18%,rgba(248,208,104,.26),transparent 62%),radial-gradient(1000px 520px at 50% 120%,rgba(122,20,32,.35),transparent 70%),linear-gradient(180deg,#2A1E14 0%,#17110C 42%,#0B0907 100%)}
.frm{position:absolute;inset:34px 34px 154px;border:1.5px solid rgba(233,162,59,.55);pointer-events:none;animation:fade 1.2s ease both}
.frm::after{content:"";position:absolute;inset:9px;border:1px solid rgba(233,162,59,.22)}
.frm i{position:absolute;width:22px;height:22px;border:1.5px solid var(--au);background:var(--dk)}
.frm i:nth-child(1){left:-12px;top:-12px}.frm i:nth-child(2){right:-12px;top:-12px}.frm i:nth-child(3){left:-12px;bottom:-12px}.frm i:nth-child(4){right:-12px;bottom:-12px}
.vig{position:absolute;inset:0;background:radial-gradient(1500px 900px at 50% 45%,transparent 58%,rgba(6,4,2,.55));pointer-events:none}
.logo{position:absolute;top:74px;left:50%;width:250px;transform:translateX(-50%);z-index:4}
.bar{position:absolute;left:0;right:0;bottom:0;height:120px;background:rgba(14,10,7,.94);border-top:3px solid var(--au);display:flex;align-items:center;padding:0 80px;z-index:4}
.cell{display:flex;align-items:center;gap:18px;padding:0 44px;border-left:1px solid rgba(255,255,255,.18);height:60px}
.cell:first-child{padding-left:0;border-left:0}
.cell svg{width:36px;height:36px;flex:none;stroke:var(--au);fill:none;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
.cell b{display:block;font-size:28px;font-weight:500;line-height:1.1;white-space:nowrap}
.cell span{display:block;font-size:22px;color:var(--mu);white-space:nowrap}
.cell.web{margin-left:auto;border-left:0;padding-right:0}
.kick{font-weight:500;font-size:28px;letter-spacing:9px;text-transform:uppercase;color:var(--au2);margin-right:-9px}
.rule{display:flex;align-items:center;gap:16px;justify-content:center;animation:fade .8s .4s ease both}
.rule::before,.rule::after{content:"";width:130px;height:1.5px;background:var(--au);transform-origin:right;animation:grow .9s .4s cubic-bezier(.16,1,.3,1) both}
.rule::after{transform-origin:left}
.rule i{width:12px;height:12px;border:1.5px solid var(--au);transform:rotate(45deg)}
'''
I_CAL = '<svg viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/></svg>'
I_PIN = '<svg viewBox="0 0 24 24"><path d="M12 22s7-7.2 7-12.5A7 7 0 0 0 5 9.5C5 14.8 12 22 12 22z"/><circle cx="12" cy="9.5" r="2.5"/></svg>'
I_WEB = '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.5 3 14.5 0 18M12 3c-3 3.5-3 14.5 0 18"/></svg>'
BAR = ('<div class="bar"><div class="cell">' + I_CAL + '<div><b data-ev="fecha">Viernes 27 de noviembre</b><span data-ev="hora_txt">Inicio 15:00 h</span></div></div>'
       '<div class="cell">' + I_PIN + '<div><b data-ev="lugar">Teatro Municipal de Santiago</b><span data-ev="dir">Agustinas 794, Santiago</span></div></div>'
       '<div class="cell web">' + I_WEB + '<div><b data-ev="web">foji.cl</b><span data-ev="hashtag">#FestivalFernandoRosas</span></div></div></div>')
BG = '<div class="vig"></div><div class="frm"><i></i><i></i><i></i><i></i></div>'
RULE = '<div class="rule"><i></i></div>'

LIVE = r'''
function fitEl(el){var mx=+el.dataset.max,mn=+el.dataset.min||20,f=mx;el.style.fontSize=f+'px';
 var over=el.dataset.fit==='h'?function(){return el.scrollHeight>el.clientHeight+4}:function(){return el.scrollWidth>el.clientWidth+1};
 while(over()&&f>mn){f-=2;el.style.fontSize=f+'px'}}
function fitAll(){document.querySelectorAll('[data-fit]').forEach(fitEl)}
function esc(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function setT(sel,v){document.querySelectorAll(sel).forEach(function(el){if(v!=null&&el.textContent!==String(v))el.textContent=v})}
function grupo(L,c){var t=(L[c]||{}).t,a=c,b=c;while(a>0&&L[a-1].t===t)a--;while(b<L.length-1&&L[b+1].t===t)b++;return{t:t,a:a,b:b}}
function carreras(L){var o=[];L.forEach(function(x){if(o.indexOf(x.t)<0)o.push(x.t)});return o}
var LAST=0,D={};
function applyLive(d){if(!d||!d.ts||d.ts<LAST)return;LAST=d.ts;D=d;
 if(d.ev){for(var k in d.ev)setT('[data-ev="'+k+'"]',d.ev[k]);document.querySelectorAll('[data-evshow]').forEach(function(e){e.classList.toggle('hide',!(d.ev[e.dataset.evshow]||'').trim())})}
 if(window.onLive)window.onLive(d);fitAll()}
window.addEventListener('ffr',function(e){applyLive(e.detail)});
try{new BroadcastChannel('ffr').onmessage=function(e){applyLive(e.data)}}catch(e){}
window.addEventListener('storage',function(e){if(e.key==='ffr-live')try{applyLive(JSON.parse(e.newValue))}catch(x){}});
try{var L0=JSON.parse(localStorage.getItem('ffr-live')||'null');if(L0)applyLive(L0)}catch(e){}
if(document.fonts&&document.fonts.ready)document.fonts.ready.then(fitAll);setTimeout(fitAll,300);
var Q=new URLSearchParams(location.search);
'''

def page(title, css, body, js='', full=True):
    return ('<!doctype html><html lang="es"><head><meta charset="utf-8"><title>' + title + '</title><style>' + FONTS + BASE +
            (FULL if full else 'html,body{background:transparent}') + css + '</style></head><body>' + body +
            '<script>' + LIVE + js + '</script></body></html>')
LG = '<img class="logo" src="' + LOGO + '" alt="FOJI 25 años">'
P = {}

# =========================================================== INICIO
P['FFR_Inicio'] = page('Festival Fernando Rosas · Inicio', r'''
.c{position:absolute;left:0;right:0;top:330px;text-align:center;display:flex;flex-direction:column;align-items:center}
.c .kick{animation:up .9s .1s ease both}
.k2{font-family:"Playfair Display";font-weight:700;font-size:150px;line-height:.95;letter-spacing:1px;margin-top:6px;animation:rise 1.2s .25s cubic-bezier(.16,1,.3,1) both}
.c .rule{margin-top:26px}
.lema{font-size:38px;color:var(--wh);margin-top:24px;animation:up .9s .5s ease both}
.cdw{margin-top:40px;display:inline-flex;align-items:center;gap:24px;border:1px solid rgba(233,162,59,.5);border-radius:999px;padding:10px 12px 10px 36px;background:rgba(14,10,7,.55);animation:up .9s .65s ease both}
.cdw small{font-size:24px;font-weight:500;letter-spacing:4px;text-transform:uppercase;color:var(--mu)}
.cdw b{font-size:54px;font-weight:700;line-height:1;font-variant-numeric:tabular-nums;background:var(--au);color:var(--dk2);border-radius:999px;padding:8px 32px 10px}
.cdw b.soon{font-size:36px;padding:14px 32px}
''', '<div class="stage">' + BG + LG
 + '<div class="c"><div class="kick" data-ev="kicker_ini">XX</div><div class="k2">Festival Fernando Rosas</div>' + RULE
 + '<div class="lema" data-ev="lema" data-evshow="lema">FOJI 25 años · Teatro Municipal de Santiago</div>'
 + '<div class="cdw"><small id="cdl">Comenzamos en</small><b id="cd">15:00</b></div></div>'
 + BAR + '</div>', r'''
var TGT=null;
window.onLive=function(d){if(d.ini){TGT=d.ini.target||null;if(d.ini.label)document.getElementById('cdl').textContent=d.ini.label}tick()};
function tick(){var b=document.getElementById('cd');var hora=(D.ev&&D.ev.hora)||'';
 if(!TGT){b.textContent=hora||'Pronto';b.classList.toggle('soon',!hora);return}
 var r=Math.max(0,Math.round((TGT-Date.now())/1000));b.classList.remove('soon');
 b.textContent=r>=3600?Math.floor(r/3600)+':'+String(Math.floor(r%3600/60)).padStart(2,'0')+':'+String(r%60).padStart(2,'0'):String(Math.floor(r/60)).padStart(2,'0')+':'+String(r%60).padStart(2,'0');
 if(r<=0){b.textContent='Comenzamos';b.classList.add('soon')}}
setInterval(tick,250);tick();''')

# =========================================================== ORQUESTA (antes de que toque)
P['FFR_Orquesta'] = page('Festival Fernando Rosas · Orquesta', r'''
.c{position:absolute;left:0;right:0;top:340px;text-align:center;display:flex;flex-direction:column;align-items:center}
.n{font-size:26px;font-weight:500;letter-spacing:4px;color:var(--mu);text-transform:uppercase;animation:up .8s ease both}
.c .kick{margin-top:22px;animation:up .8s .1s ease both}
.s{font-family:"Playfair Display";font-weight:700;font-size:150px;line-height:1;max-width:1620px;height:310px;display:flex;align-items:center;justify-content:center;text-wrap:balance;margin-top:6px;animation:rise 1.1s .2s cubic-bezier(.16,1,.3,1) both}
.z{font-size:40px;margin-top:22px;color:var(--wh);animation:up .8s .5s ease both}
.z b{color:var(--au2);font-weight:500}
.dr{font-size:32px;margin-top:14px;color:var(--mu);animation:up .8s .6s ease both}.dr b{color:var(--wh);font-weight:500}
''', '<div class="stage">' + BG + LG
 + '<div class="c"><div class="n" id="sn">Orquesta 1 de 7</div><div class="kick">En escena</div><div class="s" id="ss" data-fit="h" data-max="140" data-min="64">Nombre de la orquesta</div>' + RULE + '<div class="z" id="sz">Comuna, Región</div><div class="dr" id="sd">Dirección <b>Nombre Apellido</b></div></div>'
 + BAR + '</div>', r'''
var K='';
window.onLive=function(d){var a=d.ag||{},L=a.items||[],c=a.cur||0,g=grupo(L,c),C=carreras(L),k=JSON.stringify([g.t,g.a,g.b,C.length,(L[c]||{}).e,(L[c]||{}).h]);if(k===K)return;K=k;
 var it=L[c]||{};document.getElementById('ss').textContent=g.t||'Nombre de la orquesta';
 document.getElementById('sz').textContent=it.e||'';var sd=document.getElementById('sd');sd.innerHTML=it.h?'Dirección <b>'+esc(it.h)+'</b>':'';
 document.getElementById('sn').textContent=C.length?'Orquesta '+(C.indexOf(g.t)+1)+' de '+C.length:'';
 document.querySelectorAll('.n,.kick,.s,.rule,.z,.dr').forEach(function(e){e.style.animation='none';void e.offsetWidth;e.style.animation=''})};''')

# =========================================================== PROGRAMA (obras de la orquesta en escena)
P['FFR_Programa'] = page('Festival Fernando Rosas · Programa', r'''
.logo{left:auto;right:96px;top:84px;width:190px;transform:none}
.hd{position:absolute;left:110px;top:96px;right:360px}
.hd .kick{margin-right:0}
.hd b{display:block;font-family:"Playfair Display";font-weight:700;font-size:76px;line-height:1.02;margin-top:10px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.hd span{display:block;font-size:26px;color:var(--mu);margin-top:6px}
.gr{position:absolute;left:110px;right:110px;top:300px;height:600px;display:grid;grid-auto-flow:column;grid-template-rows:repeat(var(--rows,10),minmax(0,1fr));grid-template-columns:repeat(var(--cols,2),minmax(0,1fr));column-gap:46px}
.it{display:flex;align-items:center;gap:16px;font-size:var(--fs,32px);border-bottom:1px solid rgba(255,255,255,.10);white-space:nowrap;overflow:hidden;animation:up .5s ease both;padding:0 14px;border-radius:4px}
.it span{overflow:hidden;text-overflow:ellipsis}
.it{justify-content:space-between}.it .ob{font-family:"Playfair Display";font-weight:600}
.it small{flex:none;font-size:.62em;color:var(--mu);letter-spacing:.5px}
.it.done{color:var(--mu)}
.it.cur{background:var(--au);color:var(--dk2);font-weight:700;border-bottom-color:transparent}
.it.cur small{color:var(--dk2)}
''', '<div class="stage">' + BG + LG
 + '<div class="hd"><div class="kick">Programa</div><b id="hb">Nombre de la orquesta</b><span id="hn"></span></div><div class="gr" id="gr"></div>' + BAR + '</div>', r'''
window.onLive=function(d){var a=d.ag||{},L=a.items||[],c=a.cur||0,g=grupo(L,c),S=L.slice(g.a,g.b+1),n=S.length;
 var cols=n<=7?1:n<=14?2:3,rows=Math.max(1,Math.ceil(n/cols)),fs=Math.max(22,Math.min(44,Math.floor(600/rows*.42)));if(cols===1)rows=Math.max(rows,6);
 var gr=document.getElementById('gr');gr.style.setProperty('--cols',cols);gr.style.setProperty('--rows',rows);gr.style.setProperty('--fs',fs+'px');
 var i0=L[g.a]||{};document.getElementById('hb').textContent=g.t||'Orquesta';document.getElementById('hn').textContent=[i0.e,i0.h?'Dirección '+i0.h:''].filter(Boolean).join(' · ');
 var h=S.map(function(it,i){var k=g.a+i;return '<div class="it'+(k===c?' cur':k<c?' done':'')+'" style="animation-delay:'+(Math.min(i,40)*.02)+'s"><span class="ob">'+esc(it.o||'')+'</span>'+(it.c?'<small>'+esc(it.c)+'</small>':'')+'</div>'}).join('');
 if(gr.dataset.k!==h){var fresh=gr.dataset.t!==g.t;gr.dataset.k=h;gr.dataset.t=g.t;gr.innerHTML=h;if(!fresh)gr.querySelectorAll('.it').forEach(function(e){e.style.animation='none'})}};''')

# =========================================================== PAUSA
P['FFR_Pausa'] = page('Festival Fernando Rosas · Pausa', r'''
.c{position:absolute;left:0;right:0;top:330px;text-align:center;display:flex;flex-direction:column;align-items:center}
.t{font-family:"Playfair Display";font-weight:700;font-size:130px;line-height:1;animation:rise 1s cubic-bezier(.16,1,.3,1) both}
.c .rule{margin-top:28px}
.s{font-size:38px;margin-top:22px;animation:up .8s .2s ease both}
.clk{font-size:84px;font-weight:700;font-variant-numeric:tabular-nums;margin-top:18px;color:var(--au2)}
.next{display:inline-flex;align-items:center;gap:22px;margin-top:26px;border:1px solid rgba(233,162,59,.5);background:rgba(14,10,7,.6);border-radius:999px;padding:10px 38px 10px 12px;animation:up .8s .3s ease both;max-width:1500px}
.next small{background:var(--au);color:var(--dk2);font-size:22px;font-weight:700;letter-spacing:2px;text-transform:uppercase;padding:10px 22px;border-radius:999px;white-space:nowrap}
.next b{font-size:34px;font-weight:500;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
''', '<div class="stage">' + BG + LG
 + '<div class="c"><div class="t" id="pt">Intermedio</div>' + RULE + '<div class="s" id="ps"></div>'
 + '<div class="clk hide" id="pc">05:00</div><div class="next hide" id="pn"><small>A continuación</small><b id="pnt"></b></div></div>'
 + BAR + '</div>', r'''
var END=null;
window.onLive=function(d){var p=d.pau||{};document.getElementById('pt').textContent=p.titulo||'Intermedio';document.getElementById('ps').textContent=p.sub||'';
 END=p.end||null;var a=d.ag||{},L=a.items||[],g=grupo(L,a.cur||0),it=L[g.b+1];
 var n=document.getElementById('pn');n.classList.toggle('hide',!it||!p.next);if(it)document.getElementById('pnt').textContent=it.t||'';tick()};
function tick(){var c=document.getElementById('pc');if(!END){c.classList.add('hide');return}c.classList.remove('hide');var r=Math.max(0,Math.round((END-Date.now())/1000));c.textContent=String(Math.floor(r/60)).padStart(2,'0')+':'+String(r%60).padStart(2,'0')}
setInterval(tick,250);''')

# =========================================================== FINAL
P['FFR_Final'] = page('Festival Fernando Rosas · Final', r'''
.c{position:absolute;left:0;right:0;top:340px;text-align:center;display:flex;flex-direction:column;align-items:center}
.c .kick{animation:up .9s ease both}
.t{font-family:"Playfair Display";font-weight:700;font-size:130px;line-height:1;margin-top:14px;max-width:1700px;animation:rise 1.1s .15s cubic-bezier(.16,1,.3,1) both}
.c .rule{margin-top:28px}
.s{font-size:38px;margin-top:22px;animation:up .9s .4s ease both}
''', '<div class="stage">' + BG + LG
 + '<div class="c"><div class="kick">Gracias</div><div class="t" id="ft">Gracias por acompañarnos</div>' + RULE + '<div class="s" id="fs" data-ev="nombre">XX Festival Fernando Rosas</div></div>'
 + BAR + '</div>', r'''
window.onLive=function(d){var f=d.fin||{};document.getElementById('ft').textContent=f.titulo||'Gracias por acompañarnos';if(f.sub)document.getElementById('fs').textContent=f.sub};''')

# =========================================================== LOWER THIRD (la obra que suena o una persona)
P['FFR_Overlay_LowerThird'] = page('Festival Fernando Rosas · Lower third', r'''
#lt{position:absolute;left:110px;bottom:110px;display:flex;align-items:stretch;visibility:hidden;transition:bottom .4s}
#lt.up{bottom:210px}
#lt.in,#lt.out{visibility:visible}
.au{width:8px;background:var(--au)}
.card{position:relative;background:linear-gradient(100deg,rgba(42,30,20,.97),rgba(18,13,9,.97));padding:18px 64px 22px 34px;min-width:640px;box-shadow:0 18px 50px rgba(0,0,0,.35);border-top:1px solid rgba(233,162,59,.4);border-bottom:1px solid rgba(233,162,59,.4)}
.nm{font-family:"Playfair Display";font-size:66px;font-weight:700;line-height:1.05;white-space:nowrap}
.cg{font-size:28px;font-weight:400;margin-top:2px;white-space:nowrap;color:var(--mu)}
.ds{position:absolute;left:8px;top:-46px;background:var(--au);color:var(--dk2);font-weight:700;font-size:22px;letter-spacing:1.5px;text-transform:uppercase;padding:9px 20px;white-space:nowrap}
#lt.in .au{animation:upy .5s cubic-bezier(.16,1,.3,1) both}
#lt.in .card{animation:wipe .75s .1s cubic-bezier(.7,0,.2,1) both}
#lt.in .nm{animation:left .7s .35s ease both}
#lt.in .cg{animation:left .7s .5s ease both}
#lt.in .ds{animation:upy .5s .7s cubic-bezier(.16,1,.3,1) both}
@keyframes upy{from{transform:scaleY(0)}to{transform:none}}
@keyframes wipe{from{clip-path:inset(0 100% 0 0)}to{clip-path:inset(0 0 0 0)}}
#lt.out .nm,#lt.out .cg,#lt.out .ds{animation:fadeo .25s ease both}
#lt.out .card{animation:wipeo .45s .15s cubic-bezier(.7,0,.3,1) both}
#lt.out .au{animation:fadeo .3s .5s ease both}
@keyframes fadeo{to{opacity:0;transform:translateY(-10px)}}
@keyframes wipeo{from{clip-path:inset(0 0 0 0)}to{clip-path:inset(0 100% 0 0)}}
''', '<div id="lt"><div class="ds" id="ds">Orquesta</div><div class="au"></div><div class="card"><div class="nm" id="nm" data-max="66" data-min="38" data-fit="w">Nombre de la obra</div><div class="cg" id="cg">Compositor</div></div></div>', r'''
var V=false,K='';
function render(l){document.getElementById('nm').textContent=l.nombre||'Nombre Apellido';document.getElementById('cg').textContent=l.cargo||'';
 var s=document.getElementById('ds');s.textContent=l.empresa||'';s.classList.toggle('hide',!l.empresa);
 var w=Math.max(document.getElementById('nm').scrollWidth,document.getElementById('cg').scrollWidth);document.querySelector('.card').style.width=Math.min(1500,Math.max(640,w+100))+'px';fitAll()}
function play(c){var el=document.getElementById('lt');el.classList.remove('in','out');void el.offsetWidth;if(c)el.classList.add(c)}
window.onLive=function(d){var show=!!(d.show&&d.show.lt),l=d.lt||{},k=JSON.stringify(l);
 document.getElementById('lt').classList.toggle('up',!!(d.show&&d.show.msg));
 if(show&&(!V||k!==K)){var go=function(){K=k;render(l);play('in')};if(V){play('out');setTimeout(go,850)}else go();V=true}
 else if(!show&&V){V=false;play('out')}};
if(Q.get('demo'))setTimeout(function(){window.onLive({show:{lt:true},lt:{nombre:'Danzas eslavas op. 46 n.º 8',cargo:'Antonín Dvořák',empresa:'Orquesta Juvenil de Ejemplo'}})},300);''', full=False)

# =========================================================== MOSCA
P['FFR_Overlay_Mosca'] = page('Festival Fernando Rosas · Mosca', r'''
.mo{position:absolute;right:60px;top:52px;display:flex;flex-direction:column;align-items:flex-end;gap:10px;transform-origin:right top;transition:opacity .4s,transform .35s}
.mo.bl,.mo.tl{right:auto;left:60px;align-items:flex-start;transform-origin:left top}
.mo.br,.mo.bl{top:auto;bottom:52px;flex-direction:column-reverse;transform-origin:right bottom}
.mo.bl{transform-origin:left bottom}
.mo img{width:250px;filter:drop-shadow(0 3px 10px rgba(0,0,0,.6))}
.mo .row{display:flex;gap:10px;align-items:center}
.live{display:flex;align-items:center;gap:10px;background:var(--au);color:var(--dk2);border-radius:4px;padding:6px 16px 6px 12px;font-weight:700;font-size:20px;letter-spacing:1.5px;box-shadow:0 6px 18px rgba(0,0,0,.3)}
.live i{width:10px;height:10px;border-radius:50%;background:var(--dk2);animation:pulse 2s ease-in-out infinite}
.msg{background:rgba(14,10,7,.9);border:1px solid rgba(233,162,59,.35);border-radius:4px;padding:6px 16px;font-weight:500;font-size:20px;max-width:560px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;transition:opacity .5s}
.msg.off{opacity:0}
''', '<div class="mo" id="mo"><img src="' + LOGO + '" alt="FOJI"><div class="row"><div class="msg" id="msg">#FestivalFernandoRosas</div><div class="live" id="live"><i></i><span id="est">EN VIVO</span></div></div></div>', r'''
var MS=[],mi=0,C={pos:'tr',scale:1,op:1,live:true,msgs:true},SH=true;
function apply(){var m=document.getElementById('mo');m.className='mo '+(C.pos||'tr');m.style.transform='scale('+(+C.scale||1)+')';m.style.opacity=SH?(C.op==null?1:C.op):0;
 if(/^b/.test(C.pos)&&C.avoid)m.style.bottom=C.avoid+'px';else m.style.bottom='';
 document.getElementById('live').classList.toggle('hide',!C.live);document.getElementById('msg').classList.toggle('hide',!C.msgs||!MS.length);document.getElementById('est').textContent=C.estado||'EN VIVO'}
window.onLive=function(d){if(d.mosca){C=d.mosca;MS=C.list||[]}SH=!(d.show&&d.show.mosca===false);if(mi>=MS.length)mi=0;document.getElementById('msg').textContent=MS[mi]||'';apply()};
setInterval(function(){if(MS.length<2)return;var el=document.getElementById('msg');el.classList.add('off');setTimeout(function(){mi=(mi+1)%MS.length;el.textContent=MS[mi];el.classList.remove('off')},550)},6000);apply();''', full=False)

# =========================================================== CARRERA EN PANTALLA
P['FFR_Overlay_Tema'] = page('Festival Fernando Rosas · Orquesta en pantalla', r'''
#tm{position:absolute;left:60px;top:56px;display:flex;align-items:stretch;max-width:1180px;visibility:hidden}
#tm.in,#tm.out{visibility:visible}
.k{background:var(--au);color:var(--dk2);font-weight:700;font-size:20px;letter-spacing:2px;text-transform:uppercase;padding:0 18px;display:flex;align-items:center}
.t{background:rgba(14,10,7,.92);border:1px solid rgba(233,162,59,.35);border-left:0;font-family:"Playfair Display";font-size:36px;font-weight:700;padding:6px 28px 8px 22px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;box-shadow:0 10px 30px rgba(0,0,0,.25)}
.t span{font-family:"Montserrat";font-weight:400;color:var(--mu);font-size:22px;margin-left:12px}
#tm.in .k{animation:upy .45s cubic-bezier(.16,1,.3,1) both}
#tm.in .t{animation:wipe .6s .1s cubic-bezier(.7,0,.2,1) both}
#tm.out{animation:fo .4s ease both}
@keyframes upy{from{transform:scaleY(0)}to{transform:none}}
@keyframes wipe{from{clip-path:inset(0 100% 0 0)}to{clip-path:inset(0 0 0 0)}}
@keyframes fo{to{opacity:0;transform:translateY(-20px)}}
''', '<div id="tm"><div class="k" id="tk">Orquesta</div><div class="t" id="tt">Nombre de la orquesta</div></div>', r'''
var V=false,K='';
window.onLive=function(d){var s=!!(d.show&&d.show.tema),t=d.tema||{},k=JSON.stringify(t),el=document.getElementById('tm');
 var go=function(){K=k;document.getElementById('tk').textContent=t.kicker||'Orquesta';document.getElementById('tt').innerHTML=esc(t.titulo||'')+(t.sub?'<span>'+esc(t.sub)+'</span>':'');el.classList.remove('in','out');void el.offsetWidth;el.classList.add('in')};
 if(s&&(!V||k!==K)){if(V){el.classList.remove('in');el.classList.add('out');setTimeout(go,420)}else go();V=true}
 else if(!s&&V){V=false;el.classList.remove('in');el.classList.add('out')}};''', full=False)

# =========================================================== MENSAJE
P['FFR_Overlay_Mensaje'] = page('Festival Fernando Rosas · Mensaje', r'''
#zc{position:absolute;left:0;right:0;bottom:0;height:80px;display:flex;align-items:stretch;transform:translateY(110%);transition:transform .6s cubic-bezier(.7,0,.2,1);border-top:3px solid var(--au)}
#zc.on{transform:none}
.lb{flex:none;background:var(--au);color:var(--dk2);font-weight:700;font-size:24px;letter-spacing:2px;text-transform:uppercase;display:flex;align-items:center;padding:0 36px 0 50px}
.tx{flex:1;background:rgba(14,10,7,.96);padding-left:36px;display:flex;align-items:center;overflow:hidden;position:relative}
.tx span{font-size:32px;font-weight:400;white-space:nowrap}
.tx.mv span{animation:tick var(--d,20s) linear infinite;padding-left:100%}
@keyframes tick{from{transform:translateX(0)}to{transform:translateX(-100%)}}
''', '<div id="zc"><div class="lb"><span id="zl">Saludos</span></div><div class="tx" id="ztx"><span id="zt">Mensaje</span></div></div>', r'''
var K='',IT=[],ii=0,TT=null;
function showItem(){var sp=document.getElementById('zt'),box=document.getElementById('ztx');sp.textContent=IT[ii]||'';box.classList.remove('mv');
 requestAnimationFrame(function(){if(sp.scrollWidth>box.clientWidth-80){box.style.setProperty('--d',Math.max(10,sp.scrollWidth/140)+'s');box.classList.add('mv')}})}
window.onLive=function(d){var on=!!(d.show&&d.show.msg),m=d.msg||{};document.getElementById('zc').classList.toggle('on',on);
 var k=JSON.stringify(m);if(k===K)return;K=k;document.getElementById('zl').textContent=m.label||'Saludos';IT=(m.items||[]).filter(Boolean);ii=0;showItem();
 clearInterval(TT);if(IT.length>1)TT=setInterval(function(){ii=(ii+1)%IT.length;showItem()},(+m.every||10)*1000)};''', full=False)

# =========================================================== REPETICIÓN
P['FFR_Overlay_Replay'] = page('Festival Fernando Rosas · Repetición', r'''
.rp{position:absolute;left:60px;top:52px;display:flex;align-items:center;gap:14px;background:var(--au);color:var(--dk2);padding:8px 26px 8px 10px;box-shadow:0 10px 30px rgba(0,0,0,.35);animation:left .5s cubic-bezier(.16,1,.3,1) both}
.rp .ic{width:48px;height:48px;background:var(--dk2);display:flex;align-items:center;justify-content:center}
.rp .ic svg{width:28px;height:28px;fill:var(--au)}
.rp b{font-size:30px;font-weight:700;letter-spacing:3px;text-transform:uppercase}
.rec{position:absolute;inset:0;border:6px solid rgba(233,162,59,.55);pointer-events:none}
''', '<div class="rec"></div><div class="rp"><div class="ic"><svg viewBox="0 0 24 24"><path d="M11 6v12L2 12zM21 6v12l-9-6z"/></svg></div><b id="rt">Repetición</b></div>', r'''
window.onLive=function(d){if(d.replay&&d.replay.texto)document.getElementById('rt').textContent=d.replay.texto};''', full=False)

# =========================================================== PICTURE IN PICTURE
import sys; sys.path.insert(0, '/home/claude')
import pipgen
PIPCSS = r"""
body{background:transparent!important}
.pbg{position:absolute;inset:0;overflow:hidden;background:radial-gradient(1100px 760px at 50% -18%,rgba(248,208,104,.22),transparent 62%),linear-gradient(180deg,#2A1E14 0%,#17110C 42%,#0B0907 100%)}
.pbg .frm{inset:26px}
.win{position:absolute;border-radius:4px;box-shadow:0 0 0 2px var(--au),0 26px 60px rgba(0,0,0,.5)}
.plogo{position:absolute;top:56px;right:70px;width:200px}
.ptitle{position:absolute;left:60px;top:66px;max-width:1300px;font-family:"Playfair Display";font-size:68px;font-weight:700;line-height:1.05;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.lab{position:absolute;display:inline-flex;align-items:baseline;gap:14px;background:rgba(14,10,7,.95);border-left:6px solid var(--au);padding:8px 24px 10px 18px;box-shadow:0 12px 30px rgba(0,0,0,.35);white-space:nowrap;overflow:hidden}
.lab b{font-family:"Playfair Display";font-size:36px;font-weight:700;overflow:hidden;text-overflow:ellipsis}
.lab span{font-size:22px;color:var(--mu)}
"""
for k, L in pipgen.LAYOUTS.items():
    P['FFR_PIP_' + k] = page('Festival Fernando Rosas · PiP ' + L['nombre'], PIPCSS, pipgen.body(k, '<div class="frm"><i></i><i></i><i></i><i></i></div>', LOGO), pipgen.js(k, 4))

os.makedirs('out', exist_ok=True)
for f in os.listdir('out'):
    if not f.startswith('FFR_'): os.remove('out/' + f)
for k, v in P.items():
    open('out/%s.html' % k, 'w').write(v)
print(list(P))
