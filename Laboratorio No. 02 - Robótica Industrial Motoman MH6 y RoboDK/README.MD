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



## 3. Procedimiento detallado para realizar movimientos manuales

Para realizar los movimientos manuales del Motoman MH6 se utilizó el teach pendant. El procedimiento realizado fue el siguiente:

1. Se coloca el controlador en modo `TEACH`.
2. Se libera la parada de emergencia.
3. Se presiona `SERVO ON READY` para habilitar el movimiento del robot.
4. Se ajusta el nivel de velocidad a `FAST`.
5. Se selecciona el modo de movimiento que se desea utilizar.
6. Para el movimiento por articulaciones, se seleccionan los ejes correspondientes y se utilizan las teclas de movimiento para desplazar cada articulación en el sentido deseado.
7. Para realizar movimientos cartesianos, se cambia al modo cartesiano y se seleccionan los ejes X, Y o Z.
8. Para realizar traslaciones, se utilizan las teclas correspondientes a `X+`, `X-`, `Y+`, `Y-`, `Z+` y `Z-`.
9. Para realizar rotaciones, se utilizan los movimientos correspondientes a la orientación alrededor de los ejes X, Y y Z.
10. El movimiento se detiene al dejar de presionar la tecla correspondiente.






