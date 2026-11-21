# Laboratorio 02 - Robótica Industrial: Análisis y Operación del Manipulador Motoman MH6

## 1. Cuadro comparativo detallado de las características técnicas del Motoman MH6 y el IRB140

| Característica | Motoman MH6 utilizado en la práctica | ABB IRB140 |
|---|---|---|
| Fabricante | Yaskawa Motoman | ABB |
| Tipo de robot | Articulado vertical de 6 ejes | Articulado de 6 ejes |
| Grados de libertad del brazo | 6 | 6 |
| Ejes externos de la estación | 2: 1 eje lineal y 1 eje rotativo | No considerados |
| Grados de libertad totales del sistema | 8 | 6 |
| Carga máxima | 6 kg | 6 kg |
| Alcance máximo | 1422 mm | 810 mm |
| Repetibilidad | ±0,08 mm | ±0,03 mm |
| Velocidad máxima por eje | S: 220 °/s; L: 200 °/s; U: 220 °/s; R: 410 °/s; B: 410 °/s; T: 610 °/s | Eje 1: 200 °/s; Eje 2: 200 °/s; Eje 3: 260 °/s; Eje 4: 360 °/s; Eje 5: 360 °/s; Eje 6: 450 °/s |
| Aplicaciones típicas | Manipulación de materiales, alimentación de máquinas, ensamblaje, dispensado, empaque y soldadura | Manipulación de materiales, alimentación de máquinas, soldadura, corte, ensamblaje, inspección y dosificación |
| Masa aproximada del manipulador | 130 kg | 98 kg |
| Estructura | Robot articulado vertical de 6 ejes con dos ejes externos en la estación | Robot articulado de 6 ejes |



## 2. Descripción de las configuraciones home1 y home2 del Motoman MH6

Durante la práctica se identificaron dos posiciones de referencia del robot: WORK HOME POSITION y SECOND HOME POS.

### Home1 – WORK HOME POSITION

En el teach pendant, esta posición aparece como `WORK HOME POSITION`. Allí se muestran las seis articulaciones del robot: S, L, U, R, B y T. También aparecen las columnas ORIGIN y CURRENT, que permiten comparar la posición de referencia con la posición actual del robot.

Los valores observados fueron:

| Articulación | ORIGIN | CURRENT |
|---|---:|---:|
| S | 0 | 0 |
| L | -115280 | -115280 |
| U | -11622 | -11622 |
| R | 1 | 1 |
| B | 42647 | 42647 |
| T | 1392 | 1392 |

### Home2 – SECOND HOME POS

La segunda posición aparece como `SECOND HOME POS`. En esta pantalla se muestran los valores SPECIFIED, CURRENT y DIFFERENCE.

SPECIFIED corresponde a la posición guardada para este Home, CURRENT muestra la posición en la que se encontraba el robot y DIFFERENCE muestra la diferencia entre ambas. En la fotografía, todas las diferencias son 0.

| Articulación | SPECIFIED | CURRENT | DIFFERENCE |
|---|---:|---:|---:|
| S | 0 | 0 | 0 |
| L | 2037 | 2037 | 0 |
| U | 2359 | 2359 | 0 |
| R | 0 | 0 | 0 |
| B | -121 | -121 | 0 |
| T | 1392 | 1392 | 0 |

### ¿Cuál posición es mejor?

Para realizar el trabajo del robot, la posición más útil es WORK HOME POSITION, ya que corresponde a la posición de trabajo establecida para el manipulador. Esta posición sirve como referencia para realizar las actividades y movimientos de la práctica.

SECOND HOME POS funciona como una segunda posición de referencia del robot y puede utilizarse para llevarlo a una configuración diferente.



## 3. Procedimiento detallado para realizar movimientos manuales, especificando cómo cambiar entre modos de operación (articulaciones, cartesiano) y realizar traslaciones y rotaciones en los ejes X, Y, Z

Para realizar los movimientos manuales del Motoman MH6 desde el teach pendant del controlador DX100, primero se debe girar el selector de modo (MODE) a la posición TEACH, liberar el botón de paro de emergencia, presionar la tecla SERVO ON READY y mantener apretado suavemente el interruptor trasero Enable switch en su posición intermedia hasta que la luz SERVO ON quede encendida fija.

Una vez energizados los servomotores, se presiona la tecla COORD para alternar entre los modos de movimiento, verificando en el icono de la pantalla el cambio entre el modo articular (Joint) y el modo cartesiano (Cartesian).

En el modo Joint, manteniendo presionado el Enable switch y pulsando de forma continua las teclas de ejes, cada par de botones mueve una articulación de forma independiente hasta que se suelta la tecla. En el bloque izquierdo, X-/S- y X+/S+ giran la base (eje S), Y-/L- y Y+/L+ mueven el hombro (eje L) y Z-/U- y Z+/U+ accionan el codo (eje U). En el bloque derecho, X-/R- y X+/R+ rotan el antebrazo (eje R), Y-/B- y Y+/B+ flexionan la muñeca (eje B) y Z-/T- y Z+/T+ giran la brida (eje T).

Al cambiar al modo Cartesian con la tecla COORD, los dos bloques de teclas dividen su función entre desplazamientos lineales y giros del efector final respecto a la base. Los botones del bloque izquierdo (X-/X+, Y-/Y+ y Z-/Z+) realizan las traslaciones a lo largo de los ejes X, Y y Z, mientras que los botones del bloque derecho (X-/X+, Y-/Y+ y Z-/Z+) ejecutan las rotaciones de la herramienta alrededor de esos mismos ejes X, Y y Z.



## 4. Manejo de velocidad en movimientos manuales

En la página 44 del manual proporcionado para el curso, se explica cómo controlar la rapidez con la que se mueve el brazo robótico o manipulador. Básicamente, cuando presionamos los botones de avance o retroceso, el robot se va a mover a la velocidad que tengamos configurada en ese instante. Si tenemos dudas de cuál es esa velocidad, solo tenemos que mirar la pantalla de nuestra consola de programación donde siempre nos va a aparecer indicada.   

Para cambiar estas velocidades, usamos principalmente dos botones: uno para ir más rápido y otro para ir más lento. Si presionamos el botón de rápido repetidas veces, la velocidad va a ir subiendo paso a paso desde el nivel más bajo llamado "INCH" (pulgadas), pasando por lento y medio, hasta llegar al nivel rápido. Por el contrario, si usamos el botón de lento, la velocidad va a ir bajando en reversa desde el nivel rápido hasta llegar de nuevo al de "INCH".

Además de esto, el manual nos da un par de notas importantes a tener en cuenta en la parte de abajo. La primera es que si usamos los botones de avance o retroceso normales, el robot se va a mover en la velocidad lenta por defecto, incluso si lo teníamos puesto en el nivel más bajo de "INCH". La segunda nota es que hay un botón especial de alta velocidad que nos permite mover el robot muy rápido, pero este botón solo funciona cuando lo movemos hacia adelante y no nos va a servir de nada si intentamos moverlo hacia atrás.





## 5. Descripción de las principales funcionalidades de RoboDK, explicando cómo se comunica con el manipulador Motoman y qué procesos realiza para ejecutar movimientos

RoboDK es un software que permite modelar, programar y simular robots industriales. En la práctica se utilizó para crear la trayectoria del robot, comprobarla primero de forma virtual y posteriormente enviarla al manipulador Motoman para realizarla físicamente.

Entre sus principales funcionalidades se encuentran la simulación del robot, la creación y modificación de trayectorias, la programación de movimientos y la conexión con el robot para realizar la ejecución desde el computador.

Para mover el Motoman, RoboDK establece una comunicación entre el computador y el controlador del robot. Desde el programa se envían las instrucciones de movimiento al manipulador, permitiendo que la trayectoria programada en RoboDK sea ejecutada por el robot físico.

El proceso utilizado en la práctica fue:

1. Seleccionar y configurar el manipulador Motoman en RoboDK.
2. Crear la trayectoria que debe seguir el robot.
3. Simular la trayectoria en RoboDK para comprobar los movimientos.
4. Establecer la comunicación entre el computador y el controlador del Motoman.
5. Enviar las instrucciones de movimiento desde RoboDK.
6. Ejecutar la trayectoria en el manipulador físico.



## 6. Análisis comparativo entre RoboDK y RobotStudio, destacando ventajas, limitaciones y aplicaciones de cada herramienta

| Aspecto | RoboDK | RobotStudio |
|---|---|---|
| Función principal | Simular y programar robots industriales. | Simular y programar robots ABB. |
| Compatibilidad | Permite trabajar con robots de diferentes fabricantes, como Motoman y ABB. | Está principalmente orientado a robots ABB. |
| Simulación | Permite probar las trayectorias antes de llevarlas al robot. | Permite simular el robot y la celda de trabajo antes de realizar el montaje físico. |
| Programación | Permite crear programas y trayectorias para diferentes robots. | Permite programar robots ABB y trabajar con sus herramientas de simulación. |
| Ventajas | Es fácil de usar y permite trabajar con diferentes marcas de robots. | Tiene herramientas específicas para los robots ABB y permite trabajar con sus sistemas de programación. |
| Limitaciones | Algunas funciones dependen del robot y de la conexión utilizada. | Está más limitado a robots y sistemas ABB. |
| Aplicaciones | Simulación, programación y generación de trayectorias para robots industriales. | Simulación, programación y diseño de celdas de trabajo con robots ABB. |

En esta práctica usamos RoboDK porque el robot utilizado fue el Motoman MH6. Con este programa se hizo la trayectoria polar, primero se probó en la simulación y después se realizó con el robot físico. RobotStudio se usa principalmente cuando se trabaja con robots ABB.








