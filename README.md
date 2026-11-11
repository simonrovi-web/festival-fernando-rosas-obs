# Kit de transmisión · XX Festival Fernando Rosas

Gráficos en vivo para OBS del XX Festival Fernando Rosas (FOJI 25 años), el viernes 27 de noviembre en el Teatro Municipal de Santiago: a las 15:00 las seis orquestas comunales y a las 19:00 el concierto de gala de la OSNJ con la Orquesta Filarmónica de Santiago.

Identidad: negro de teatro `#1A130D` / `#0B0907` y el dorado del logo FOJI 25 años `#E9A23B`, títulos en Playfair Display y textos en Montserrat (la letra de foji.cl). El logo se tomó de foji.cl; si llega el logo oficial del festival o de los auspiciadores, se reemplaza en `Logos/` y en los gráficos.

## Contenido

| Archivo / carpeta | Para qué sirve |
|---|---|
| `MATERIAL_FOJI.html` | Panel de muestra de todo el material. |
| `CONTROL_EN_VIVO.html` | Página de control: se conecta a OBS y maneja el programa, lower thirds, orquesta en pantalla, mensajes, mosca, PiP, pantallas, repeticiones y transiciones. |
| `PANEL_MIDI.html` | Controlar todo desde un controlador MIDI. Ábrelo en el mismo Chrome que el control. |
| `Paneles/` | Inicio, Orquesta, Programa, Pausa (intermedio), Final, overlays (lower third, orquesta en pantalla, mensaje, mosca, repetición), los 5 marcos PiP y los stingers HTML. |
| `Transiciones/` | Telón, Destello, Franjas y Marco en video con transparencia y sonido: 4 s (corte 2000 ms) y **Corta** de 2 s (corte 1000 ms), en 1080p y `720p/`. |
| `Logos/` | Logo FOJI 25 años. |

## El programa

Cada fila es una obra: **Orquesta | Comuna, región | Dirección | Obra | Compositor**. En la tarjeta **Programa por orquesta** abre *Pegar el programa* y usa cualquiera de estas formas:

- Cinco columnas copiadas desde Excel.
- Una línea por obra: `Orquesta Juvenil de X | Comuna, Región | Nombre Apellido | Obra | Compositor`
- Por bloques: `Orquesta | Comuna, región | Dirección` en una línea, debajo sus obras como `Obra | Compositor`, y una línea en blanco antes de la orquesta siguiente.

El concierto de las 19:00 va como una orquesta más (por ejemplo `OSNJ y Orquesta Filarmónica de Santiago | Concierto de gala · 19:00 | Paolo Bortolameolli`). Mientras no tengas el programa, **↺ Programa de ejemplo** carga uno de prueba.

## Puesta en marcha (una vez, en el PC de OBS)

1. Descomprime el kit en una carpeta fija.
2. En OBS: **Herramientas → Ajustes del servidor WebSocket** → habilitar → copiar la contraseña.
3. Abre `CONTROL_EN_VIVO.html` en Chrome, pega la contraseña y pulsa **CONECTAR**.
4. Pulsa **⚙ Instalar gráficos en OBS**: crea las escenas INICIO, ESTUDIO, ORQUESTA, PROGRAMA, PAUSA, REPLAY, FINAL y las cinco PIP_ con sus gráficos, y el stinger HTML encima de todo. No borra nada de lo que ya tengas.
5. En ESTUDIO agrega las cámaras del teatro **debajo** de los gráficos.
6. En **Datos del evento** revisa fecha, hora, lugar y textos.

## Durante el concierto

- **ORQUESTA** presenta a la orquesta que sube (nombre, comuna y región, dirección). Luego **ESTUDIO** con las cámaras.
- **SIGUIENTE ▶** pasa a la obra que sigue y muestra su lower third (obra, compositor y orquesta). La **orquesta en pantalla** cambia sola al cambiar de orquesta.
- **PROGRAMA** muestra todas las obras de la orquesta con la que suena marcada en dorado.
- **PAUSA** es el intermedio entre las 15:00 y las 19:00, con cuenta regresiva y la orquesta que viene.
- En la lista de personas del lower third aparecen las direcciones de cada orquesta para presentarlas.
- **Teclado**: `1`–`9` ponen la escena en vista previa, `Shift` + número la pasa directo al aire, `P` repite y `M` guarda un momento.

## Picture in picture (PiP)

| Escena | Formato | Ventanas |
|---|---|---|
| `PIP_PRESENTACION` | Presentación + cámara | 1340×754 y 420×236 |
| `PIP_DOS` | Dos cámaras | 885×498 cada una |
| `PIP_TRES` | Tres cámaras | 580×326 cada una |
| `PIP_VERTICAL` | Cámara + video vertical (celular) | 1150×647 y 460×818 |
| `PIP_ESQUINA` | Cámara chica sobre una pantalla completa | 420×236 |

Las ventanas quedan transparentes; *Instalar gráficos* deja una fuente de color del tamaño exacto en cada una para reemplazarla por la cámara. En la tarjeta **Picture in picture** escribes el título y el nombre y cargo de cada ventana.

## Transiciones

**Telón**, **Destello**, **Franjas** y **Marco**, con el sello "XX Festival Fernando Rosas" y el logo FOJI. Tapan la pantalla a la mitad y traen su sonido. En la tarjeta **Transiciones HTML** eliges diseño, duración y sonido. Para los videos de `Transiciones/` crea en OBS transiciones Stinger llamadas **FFR Telon**, **FFR Destello**, **FFR Franjas** o **FFR Marco** (o su versión **Corta**) y pulsa **🎬 Ajustar transiciones**.
