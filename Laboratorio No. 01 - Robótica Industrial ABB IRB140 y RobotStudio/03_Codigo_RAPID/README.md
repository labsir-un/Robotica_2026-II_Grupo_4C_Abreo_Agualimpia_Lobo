# Código RAPID

En esta carpeta se encuentra el código completo desarrollado en **RAPID** para la práctica de Robótica Industrial. El programa controla el robot ABB, la banda transportadora y las diferentes rutinas solicitadas durante el laboratorio.

El archivo principal es **`Codigo_Completo_RAPID.mod`**, donde se encuentra integrado todo el programa.

---

## 1. Programa principal `main`

El procedimiento `main` permanece ejecutándose continuamente mediante un ciclo `WHILE TRUE`. Dependiendo de la entrada digital que se active, el robot ejecuta una de las tres funciones principales: **ciclo automático de decoración, mantenimiento o Farmear Aura**.

```rapid
    PROC main()
        WHILE TRUE DO
            IF DI_01 = 1 THEN
                ConveyorStop;
                ResetTesters;
                HomeRobot;
                ConveyorForward;
                WaitTime 4.8;
                ConveyorStop;
                WaitTime 3;
                Set DO_01;
                Nombres;
                Reset DO_01;
                HomeRobot;
                ConveyorForward;
                WaitTime 4;
                ConveyorStop; 
            ELSEIF DI_02 = 1 THEN
                ConveyorStop;
                Reset DO_01;
                Reset DO_03;
                PoseMantenimiento;
                Set DO_02;
            ELSEIF DI_03 = 1 THEN
                ConveyorStop;
                ResetTesters;
                Set DO_03;
                FarmearAura;
                Reset DO_03;
                HomeRobot;
                WaitTime 3;
                ConveyorBackward;
                WaitTime 8;
                ConveyorStop;
            ENDIF
            WaitTime 0.1;
        ENDWHILE
    ENDPROC
```

### Funcionamiento

- **`DI_01`**: ejecuta el ciclo automático de decoración.
- **`DI_02`**: activa el modo de mantenimiento.
- **`DI_03`**: ejecuta la rutina **Farmear Aura**.
- **`WaitTime 0.1`**: introduce una pequeña pausa dentro del ciclo de ejecución.

---

## 2. Reinicio de las salidas digitales

Para evitar que alguna salida permanezca activa al comenzar una nueva rutina, se utiliza el procedimiento `ResetTesters`.

```rapid
PROC ResetTesters()
    Reset DO_01;
    Reset DO_02;
    Reset DO_03;
ENDPROC
```

Este procedimiento desactiva las tres salidas digitales utilizadas durante la práctica.

---

## 3. Control de la banda transportadora

La banda transportadora se controla mediante las señales **`FWD_Conveyor`** y **`BWD_Conveyor`**.

### Detener la banda

```rapid
PROC ConveyorStop()
    Reset FWD_Conveyor;
    Reset BWD_Conveyor;
ENDPROC
```

Este procedimiento desactiva las dos señales de la banda, haciendo que esta se detenga.

### Movimiento hacia adelante

```rapid
PROC ConveyorForward()
    ConveyorStop;
    Set FWD_Conveyor;
ENDPROC
```

Primero se detiene la banda y después se activa `FWD_Conveyor` para iniciar el movimiento hacia adelante.

### Movimiento hacia atrás

```rapid
PROC ConveyorBackward()
    ConveyorStop;
    Set BWD_Conveyor;
ENDPROC
```

Primero se detiene la banda y posteriormente se activa `BWD_Conveyor` para realizar el movimiento en sentido contrario.

---

## 4. Ciclo automático de decoración – `DI_01`

Cuando se activa **`DI_01`**, se ejecuta la secuencia automática de decoración.

```rapid
IF DI_01 = 1 THEN
    ConveyorStop;
    ResetTesters;
    HomeRobot;

    ConveyorForward;
    WaitTime 4.8;
    ConveyorStop;

    WaitTime 3;
    Set DO_01;
    Nombres;
    Reset DO_01;

    HomeRobot;
    ConveyorForward;
    WaitTime 4;
    ConveyorStop;
ENDIF
```

### Funcionamiento del ciclo

1. Se detiene la banda y se reinician las salidas digitales.
2. El robot se lleva a la posición **HOME**.
3. La banda transporta el pastel hacia la zona de trabajo.
4. La banda se detiene.
5. Se activa `DO_01`.
6. Se ejecuta la rutina `Nombres`.
7. Se desactiva `DO_01`.
8. El robot regresa a **HOME**.
9. La banda vuelve a moverse para retirar el pastel.
10. Finalmente, la banda se detiene.

---

## 5. Rutina de decoración `Nombres`

La rutina `Nombres` agrupa las diferentes trayectorias utilizadas para realizar la decoración.

```rapid
PROC Nombres()
    Path_20;
    Path_30;
    Path_40;
    Path_50;
    ...
    Path_1820;
    ...
ENDPROC
```

Cada procedimiento `Path_...` corresponde a una trayectoria generada para realizar una parte de la decoración. La rutina `Nombres` permite ejecutarlas de manera consecutiva.

---

## 6. Tipos de movimiento utilizados

Durante las trayectorias del robot se utilizan diferentes instrucciones de movimiento de RAPID.

### `MoveJ`

El movimiento `MoveJ` realiza un desplazamiento mediante movimiento articular.

```rapid
MoveJ ...,v500,z10,MyNewTool;
```

### `MoveL`

El movimiento `MoveL` realiza un desplazamiento lineal del TCP entre los puntos programados.

```rapid
MoveL ...,v500,z10,MyNewTool;
```

### `MoveC`

El movimiento `MoveC` permite realizar trayectorias circulares utilizando los puntos definidos en la trayectoria.

```rapid
MoveC ...,v500,z10,MyNewTool;
```

Estos movimientos se utilizan en las diferentes trayectorias que forman la decoración del pastel.

---

## 7. Herramienta y WorkObject

El programa utiliza la herramienta **`MyNewTool`** y el sistema de coordenadas de trabajo **`Workobject_1`**.

```rapid
TASK PERS wobjdata Workobject_1:=[FALSE,TRUE,"",[[0,0,0],[1,0,0,0]],[[600,-50,100],[0,0,1,0]]];
```

El `WorkObject` permite definir el sistema de referencia utilizado para las trayectorias realizadas sobre el área de trabajo.

La herramienta `MyNewTool` corresponde a la herramienta utilizada por el robot durante la simulación.

---

## 8. Posición HOME

La posición HOME se encuentra definida mediante el siguiente `robtarget`:

```rapid
CONST robtarget Target_Home:=[[627.578400594,-1.755,500.392812155],[0.258819045,0,0.965925826,0],[-1,0,-1,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
```

Esta posición se utiliza como referencia para iniciar y finalizar diferentes rutinas del programa.

El procedimiento `HomeRobot` se utiliza para regresar el robot a esta posición.

---

## 9. Modo de mantenimiento – `DI_02`

Cuando se activa **`DI_02`**, la banda transportadora se detiene y el robot se dirige a la posición de mantenimiento.

```rapid
ELSEIF DI_02 = 1 THEN
    ConveyorStop;
    Reset DO_01;
    Reset DO_03;
    PoseMantenimiento;
    Set DO_02;
```

Antes de entrar en mantenimiento se desactivan `DO_01` y `DO_03`.

Posteriormente, `PoseMantenimiento` lleva el robot a la posición definida para realizar las actividades de mantenimiento y se activa `DO_02` para indicar este estado.

---

## 10. Rutina `FarmearAura`

La rutina `FarmearAura` contiene una secuencia de movimientos articulares diseñados para realizar una trayectoria diferente a la decoración.

```rapid
PROC FarmearAura()
    MoveAbsJ [[0,-2,-4,0,32,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v300,z10,MyNewTool;
    MoveAbsJ [[-12,3,2,15,42,-8],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v400,z10,MyNewTool;
    MoveAbsJ [[-25,1,-2,30,50,-15],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v500,z10,MyNewTool;
    MoveAbsJ [[-12,-2,-5,45,58,-5],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v400,z10,MyNewTool;
    MoveAbsJ [[0,2,1,30,48,8],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v500,z10,MyNewTool;
    MoveAbsJ [[12,-2,-5,-25,48,8],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v400,z10,MyNewTool;
    MoveAbsJ [[25,1,-2,-40,58,18],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v500,z10,MyNewTool;
    ...
ENDPROC
```

Los valores utilizados en cada `MoveAbsJ` corresponden a diferentes configuraciones articulares del robot. La combinación de estas posiciones genera la trayectoria de la rutina.

---

## 11. Ejecución de `FarmearAura` mediante `DI_03`

La rutina se ejecuta cuando se activa **`DI_03`**.

```rapid
ELSEIF DI_03 = 1 THEN
    ConveyorStop;
    ResetTesters;
    Set DO_03;

    FarmearAura;
    Reset DO_03;
    HomeRobot;

    WaitTime 3;
    ConveyorBackward;
    WaitTime 8;
    ConveyorStop;
ENDIF
```

Durante la ejecución de `FarmearAura`, la banda permanece detenida para permitir que el robot realice la trayectoria.

`DO_03` se mantiene activo durante la rutina y posteriormente se desactiva. Finalmente, el robot regresa a HOME y la banda puede moverse en sentido contrario.

---

## 12. Entradas y salidas digitales utilizadas

| Señal | Tipo | Función |
|---|---|---|
| `DI_01` | Entrada digital | Activar ciclo automático de decoración |
| `DI_02` | Entrada digital | Activar modo de mantenimiento |
| `DI_03` | Entrada digital | Activar rutina Farmear Aura |
| `DO_01` | Salida digital | Indicar ejecución de la decoración |
| `DO_02` | Salida digital | Indicar modo de mantenimiento |
| `DO_03` | Salida digital | Indicar ejecución de Farmear Aura |
| `FWD_Conveyor` | Salida digital | Movimiento hacia adelante de la banda |
| `BWD_Conveyor` | Salida digital | Movimiento hacia atrás de la banda |

---

## 13. Estructura general del programa

La lógica general del programa puede resumirse de la siguiente manera:

```text
                    INICIO
                       │
                       ▼
                 WHILE TRUE
                       │
          ┌────────────┼────────────┐
          │            │            │
       DI_01=1      DI_02=1      DI_03=1
          │            │            │
          ▼            ▼            ▼
      Decoración   Mantenimiento  Farmear Aura
          │            │            │
          ▼            ▼            ▼
      Banda +       Robot a       Robot ejecuta
      Nombres       mantenimiento  movimientos
          │            │            │
          ▼            ▼            ▼
        HOME         DO_02         HOME
          │
          ▼
      Banda sale
          │
          ▼
      Nuevo ciclo
```

El archivo **`Codigo_Completo_RAPID.mod`** contiene el código completo utilizado durante el desarrollo de la práctica.
