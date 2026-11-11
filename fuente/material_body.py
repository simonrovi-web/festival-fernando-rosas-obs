SCREENS = [('inicio', 'Inicio', 'Escena INICIO', 'El XX Festival Fernando Rosas con la cuenta regresiva hasta las 15:00.'),
 ('orquesta', 'Orquesta', 'Escena ORQUESTA', 'Presenta cada orquesta antes de tocar: nombre, comuna y región, y su dirección.'),
 ('programa', 'Programa', 'Escena PROGRAMA', 'Las obras de la orquesta en escena con su compositor; la que suena se marca en dorado.'),
 ('pausa', 'Intermedio', 'Escena PAUSA', 'Entre las dos funciones: cuenta regresiva y la orquesta que viene.'),
 ('final', 'Final', 'Escena FINAL', 'Cierre de la transmisión.')]
tabs = ''.join('<button type="button" role="tab" id="t-%s" aria-controls="p-%s" aria-selected="%s"%s>%s</button>' % (k, k, 'true' if i == 0 else 'false', '' if i == 0 else ' tabindex="-1"', n) for i, (k, n, _, _) in enumerate(SCREENS))
panes = ''.join('<div class="pane" role="tabpanel" id="p-%s" aria-labelledby="t-%s">%s<div class="cap"><h3>%s</h3><small>%s</small><p>%s</p></div></div>' % (k, k, media(k, n), n, tag, d) for k, n, tag, d in SCREENS)
STG = [('telon', 'Telón', 'Dos paneles oscuros se cierran como el telón del Municipal y vuelven a abrirse.'),
 ('destello', 'Destello', 'Un círculo se expande desde el centro con un anillo dorado.'),
 ('franjas', 'Franjas', 'Franjas diagonales negras y doradas cruzan la pantalla.'),
 ('marco', 'Marco', 'Marcos rectangulares se cierran hacia el centro y luego se abren.')]
stg = ''.join('<li><button type="button" class="stage" data-hst="%s" aria-label="Reproducir la transición %s otra vez"><div aria-hidden="true"></div></button><h3>%s</h3><p>%s</p><code>FFR_Stinger_%s.html</code></li>' % (k, n, n, d, n.replace('ó', 'o')) for k, n, d in STG)

BODY = '''<a class="skip" href="#main">Saltar al contenido</a>
<div class="top">
 <header class="container nav">
  <img src="__LOGOW__" alt="FOJI 25 años" width="817" height="259" style="height:52px;width:auto">
  <nav aria-label="Secciones"><ul>
   <li><a href="#identidad">Identidad</a></li><li><a href="#pantallas">Pantallas</a></li><li><a href="#overlays">Gráficos en vivo</a></li><li><a href="#pip">PiP</a></li><li><a href="#transiciones">Transiciones</a></li><li><a href="#control">Control</a></li><li><a href="#obs">En OBS</a></li>
  </ul></nav>
 </header>
 <section class="hero" aria-labelledby="h-hero">
  <div class="container grid12">
   <div class="intro">
    <h1 id="h-hero">El Festival Fernando Rosas en pantalla</h1>
    <p class="lead">El kit para transmitir la XX versión desde el Teatro Municipal, orquesta por orquesta.</p>
    <div class="hero-actions"><a class="btn" href="#pantallas">Ver las pantallas</a></div>
   </div>
   <figure class="hero-visual" data-loop>
    <div class="screen" id="hero-screen">
     <img src="__ESTUDIO__" alt="Escena ESTUDIO con la orquesta en pantalla, lower third de la obra, mensaje y mosca" data-on="1" width="1600" height="900" fetchpriority="high">
     <img src="__ORQUESTA__" alt="Pantalla Orquesta" data-on="0" aria-hidden="true" width="1280" height="720">
     <img src="__PROGRAMA__" alt="Pantalla Programa" data-on="0" aria-hidden="true" width="1280" height="720">
     <div class="stage-layer" aria-hidden="true"><div></div></div>
    </div>
    <figcaption class="hero-cap"><span id="hero-now">Escena ESTUDIO, pasando a ORQUESTA con la transición Telón.</span><button class="btn btn--quiet btn--small" type="button" data-loop-toggle>Pausar</button></figcaption>
   </figure>
  </div>
 </section>
</div>
<main id="main">
<section class="sec sec--l" id="identidad" aria-labelledby="h-id">
 <div class="container">
  <div class="head"><h2 id="h-id">Identidad visual</h2><p class="lead">Logo y dorado tomados de foji.cl, en clave de gala de teatro: negro cálido, el dorado del logo 25 años y títulos con serifa.</p></div>
  <div class="grid12 id-body">
   <table class="swatches">
    <thead><tr><th scope="col"><span class="visually-hidden">Muestra</span></th><th scope="col">Color</th><th scope="col">Código</th><th scope="col">Uso</th></tr></thead>
    <tbody>
     <tr><td><i class="chip" style="background:var(--imp-1)"></i></td><td class="nm">Negro teatro</td><td><code>#1A130D</code></td><td class="use">Fondos, tarjetas y barras</td></tr>
     <tr><td><i class="chip" style="background:var(--imp-2)"></i></td><td class="nm">Negro profundo</td><td><code>#0B0907</code></td><td class="use">Degradados y barra inferior</td></tr>
     <tr><td><i class="chip" style="background:var(--imp-3)"></i></td><td class="nm">Dorado FOJI</td><td><code>#E9A23B</code></td><td class="use">Marcos finos, etiquetas y la obra que suena</td></tr>
     <tr><td><i class="chip" style="background:var(--imp-4)"></i></td><td class="nm">Dorado claro</td><td><code>#F8D068</code></td><td class="use">Luz de escenario en los fondos</td></tr>
     <tr><td><i class="chip" style="background:var(--imp-5)"></i></td><td class="nm">Rojo butaca</td><td><code>#7A1420</code></td><td class="use">Brillo cálido al pie de los fondos</td></tr>
     <tr><td><i class="chip" style="background:var(--imp-6)"></i></td><td class="nm">Marfil</td><td><code>#F6F0E6</code></td><td class="use">Títulos y textos</td></tr>
    </tbody>
   </table>
   <div class="specimens">
    <div class="spec"><small>Nombres y títulos</small><span class="face">Playfair Display</span><p>Orquestas, obras y títulos de pantalla.</p></div>
    <div class="spec"><small>Texto</small><span class="face face--alt">Montserrat</span><p class="alt">La letra de foji.cl: compositores, etiquetas y datos.</p></div>
   </div>
   <ul class="logos" style="grid-template-columns:minmax(0,1fr) minmax(0,1fr)">
    <li><div class="tile t-blue"><img src="__LOGOW__" alt="Logo FOJI 25 años" width="817" height="259"></div><span>Logo FOJI 25 años de foji.cl, para fondos oscuros</span></li>
   </ul>
  </div>
 </div>
</section>

<section class="sec" id="pantallas" aria-labelledby="h-pa">
 <div class="container">
  <div class="head"><h2 id="h-pa">Pantallas completas</h2><p class="lead">Por cada orquesta: primero su presentación, después el programa mientras toca. El programa se pega en CONTROL_EN_VIVO.</p></div>
  <div data-switch>
   <div class="seg" role="tablist" aria-label="Pantallas">__TABS__</div>
   <div class="panels">__PANES__</div>
  </div>
  <p class="hint" style="margin-top:var(--space-lg)">Haz clic en cualquier imagen para verla en grande.</p>
 </div>
</section>

<section class="band" id="overlays" aria-labelledby="h-ov">
 <div class="container">
  <div class="head"><h2 id="h-ov">Gráficos en vivo sobre cámara</h2><p class="lead">Se superponen a las cámaras en la escena ESTUDIO. La imagen de fondo es solo de referencia.</p></div>
  <div class="bento">
   <figure class="b-lead">__M_ESTUDIO__<figcaption><h3>Todo junto en ESTUDIO</h3><span>Orquesta en pantalla, lower third de la obra, mensaje y mosca al mismo tiempo.</span></figcaption></figure>
   <figure class="b-side">__M_LT__<figcaption><h3>Lower third de la obra</h3><span>Obra, compositor y orquesta. Con SIGUIENTE pasa sola a la obra que sigue; también sirve para la dirección.</span></figcaption></figure>
   <figure class="b-side">__M_REPLAY__<figcaption><h3>Repetición</h3><span>Marca de repetición durante los replays (escena REPLAY).</span></figcaption></figure>
   <figure class="b-third">__M_TEMA__<figcaption><h3>Orquesta en pantalla</h3><span>La orquesta que está tocando y su comuna, arriba a la izquierda.</span></figcaption></figure>
   <figure class="b-third">__M_MENSAJE__<figcaption><h3>Mensaje inferior</h3><span>Saludos y avisos; si el texto es largo, se desplaza.</span></figcaption></figure>
   <figure class="b-third">__M_MOSCA__<figcaption><h3>Mosca</h3><span>Logo, EN VIVO y mensajes que rotan.</span></figcaption></figure>
  </div>
 </div>
</section>

<section class="sec" id="pip" aria-labelledby="h-pip">
 <div class="container">
  <div class="head"><h2 id="h-pip">Picture in picture</h2><p class="lead">Cinco marcos para palabras de autoridades, entrevistas en el foyer y saludos. Las ventanas quedan transparentes y el control escribe los nombres.</p></div>
  <div class="bento">
   <figure class="b-lead">__M_PIP1__<figcaption><h3>Presentación + cámara</h3><span>Video o presentación de una orquesta, y quien habla al lado con su nombre y cargo.</span></figcaption></figure>
   <figure class="b-side">__M_PIP5__<figcaption><h3>Esquina</h3><span>Una cámara chica sobre cualquier pantalla completa, como el programa.</span></figcaption></figure>
   <figure class="b-side">__M_PIP4__<figcaption><h3>Cámara + video vertical</h3><span>Para saludos de las orquestas grabados con el celular.</span></figcaption></figure>
   <figure class="b-half">__M_PIP2__<figcaption><h3>Dos cámaras</h3><span>Entrevista: quien pregunta y un músico o director.</span></figcaption></figure>
   <figure class="b-half">__M_PIP3__<figcaption><h3>Tres cámaras</h3><span>Conversación de tres, con el título arriba.</span></figcaption></figure>
  </div>
  <p class="hint" style="margin-top:var(--space-lg)">Instalar gráficos crea las escenas PIP_PRESENTACION, PIP_DOS, PIP_TRES, PIP_VERTICAL y PIP_ESQUINA, con una fuente de color del tamaño justo en cada ventana para reemplazarla por tu cámara.</p>
 </div>
</section>

<section class="sec sec--l" id="transiciones" aria-labelledby="h-tr">
 <div class="container">
  <div class="head"><h2 id="h-tr">Transiciones</h2><p class="lead">Cuatro transiciones de gala hechas en HTML para OBS, aquí tal como corren. Tapan la pantalla a la mitad y el control cambia la escena en ese momento. También vienen en video con transparencia (4 s y 2 s, en 1080p y 720p).</p></div>
  <div data-loop id="tr-loop">
   <div class="tr-tools"><p class="hint">Toca una transición para verla de nuevo.</p><button class="btn btn--quiet btn--small" type="button" data-loop-toggle>Pausar</button></div>
   <ul class="stingers stingers--two">__STG__</ul>
  </div>
 </div>
</section>

<section class="well" id="control" aria-labelledby="h-ct">
 <div class="container">
  <div class="head"><h2 id="h-ct">Herramientas de control</h2><p class="lead">Se abren en Chrome en el PC de la transmisión y se conectan a OBS.</p></div>
  <div class="ctl">
   <figure class="media c-main" style="margin:0"><img src="__CONTROL__" alt="CONTROL_EN_VIVO" tabindex="0" role="button" aria-label="Ver CONTROL_EN_VIVO en grande" loading="lazy" width="1400" height="887"></figure>
   <div class="c-main-tx"><h3>CONTROL_EN_VIVO</h3><p>El programa por orquesta, lower thirds, orquesta en pantalla, mensajes, mosca, PiP, pantallas, escenas, transiciones y repeticiones.</p></div>
   <figure class="media c-midi" style="margin:0"><img src="__MIDI__" alt="PANEL_MIDI" tabindex="0" role="button" aria-label="Ver PANEL_MIDI en grande" loading="lazy" width="1400" height="1000"></figure>
   <div class="c-midi-tx"><h3>PANEL_MIDI</h3><p>Cualquier acción en un pad del controlador: obra siguiente, lower third, escenas a vista previa, transiciones y repeticiones.</p></div>
  </div>
 </div>
</section>

<section class="obs" id="obs" aria-labelledby="h-obs">
 <div class="container">
  <div class="head"><h2 id="h-obs">Cómo queda en OBS</h2><p class="lead">El botón INSTALAR crea estas escenas con sus gráficos; en ESTUDIO y en las PiP van tus cámaras.</p></div>
  <ul class="scenes" aria-label="Escenas que crea INSTALAR"><li>INICIO</li><li>ESTUDIO</li><li>ORQUESTA</li><li>PROGRAMA</li><li>PAUSA</li><li>REPLAY</li><li>FINAL</li><li>PIP_…</li></ul>
  <ol class="steps">
   <li><span>Descomprimir el kit en una carpeta fija y abrir <b>CONTROL_EN_VIVO.html</b> en Chrome.</span></li>
   <li><span>En OBS activar el <b>servidor WebSocket</b>, copiar la contraseña y pulsar <b>CONECTAR</b>.</span></li>
   <li><span>Pulsar <b>Instalar gráficos en OBS</b> y agregar las cámaras en ESTUDIO y en las escenas PiP.</span></li>
   <li><span>Pegar el <b>programa</b> desde Excel: orquesta, comuna, dirección, obra y compositor.</span></li>
   <li><span>Durante el concierto: ORQUESTA al presentar, PROGRAMA y <b>SIGUIENTE ▶</b> en cada obra; PAUSA entre las funciones.</span></li>
  </ol>
 </div>
</section>
</main>
<footer class="foot">
 <div class="container"><img src="__LOGOW__" alt="FOJI" width="817" height="259" style="height:56px;width:auto"><p>Kit de transmisión del XX Festival Fernando Rosas · FOJI 25 años. Identidad tomada de foji.cl.</p></div>
</footer>
<div id="lb" role="dialog" aria-label="Imagen ampliada"><img alt="" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=="></div>
'''
rep = {'__LOGOW__': P3('../Logo_FOJI25.png', 520), '__ESTUDIO__': J('estudio'), '__ORQUESTA__': J('orquesta'), '__PROGRAMA__': J('programa'),
 '__TABS__': tabs, '__PANES__': panes, '__STG__': stg, '__CONTROL__': J('control'), '__MIDI__': J('midi'),
 '__M_ESTUDIO__': media('estudio', 'Todo junto en ESTUDIO'), '__M_LT__': media('lt', 'Lower third de la obra'), '__M_REPLAY__': media('replay', 'Repetición'),
 '__M_TEMA__': media('tema', 'Orquesta en pantalla'), '__M_MENSAJE__': media('mensaje', 'Mensaje inferior'), '__M_MOSCA__': media('mosca', 'Mosca'),
 '__M_PIP1__': media('pip_Presentacion', 'PiP presentación más cámara'), '__M_PIP2__': media('pip_Dos', 'PiP dos cámaras'), '__M_PIP3__': media('pip_Tres', 'PiP tres cámaras'), '__M_PIP4__': media('pip_Vertical', 'PiP cámara más video vertical'), '__M_PIP5__': media('pip_Esquina', 'PiP esquina')}
