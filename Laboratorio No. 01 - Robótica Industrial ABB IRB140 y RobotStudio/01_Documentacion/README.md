# Documentación

En esta carpeta se encuentra la documentación correspondiente al desarrollo del Laboratorio No. 01 de Robótica Industrial.
## Descripción de la solución implementada.
**Asignatura:** Robótica Industrial  
**Ubicación:** Laboratorio de Sistemas Inteligentes Robotizados (Lab SIR - UNAL)  
**Equipo:** Grupo 4C ("Robot Abel")  
**Integrantes:**
* Sharon M. Lobo V.
* Cristian E. Agualimpia T.
* Fabian S. Abreo 
### 1. Visión General de la Celda de Trabajo y Entorno Físico
Se implementó y automatizó una celda de trabajo industrial para la decoración de pasteles utilizando un robot industrial **ABB IRB 140**, una **banda transportadora bidireccional**, un gabinete controlador **ABB IRC5** con módulo de entradas/salidas digitales (DSQC 652), una **caja de botonera industrial con testigos luminosos de estado**, y una herramienta porta-marcador impresa en 3D.

Para la validación experimental se construyeron **dos maquetas físicas de pasteles**:
* Base cilíndrica rígida recubierta superiormente con papel adhesivo transparente (*contact*).
* Acabado estético lateral simulando glaseado rosado (*drip cake*).
* La superficie plástica permitió ejecutar trazos continuos con marcadores de borrado en seco y limpiar el plano de trabajo tras cada ciclo sin degradar la maqueta.

### 2. Diseños CAD y Calibración del TCP (`tooldata`)
* **Calibración Física (Método de Reorientación en Punta Fija):** Se utilizó una punta metálica fija en la mesa como referencia espacial. El robot aproximó la herramienta desde 4 orientaciones distintas manteniendo el extremo del marcador inmóvil en el espacio mientras el *flange* reorientaba su pose. El controlador IRC5 calculó las coordenadas del centro de la herramienta (`tooldata`).
* **Validación en RobotStudio:** Se importó el modelo CAD de la herramienta porta-marcador a la estación virtual y se ajustaron los parámetros cartesianos de la simulación reduciendo el margen de error del TCP antes de transferir la configuración al robot real.

### 3. Trayectorias y Objeto de Trabajo (`wobjdata`)
* **Trazado:** Se programó el dibujo de la figura central de **Pac-Man comiendo puntos hacia un fantasma**, flanqueado por los nombres del equipo (**SHARON**, **ESTEBAN**, **FABIAN**).
* **Movimientos:** Se utilizaron movimientos articulares (`MoveJ`) para aproximaciones en el aire ($Z = -10\text{ mm}$) y retornos a la pose `HOME`, y movimientos lineales rectilíneos (`MoveL`) para el contacto y trazado continuo.
* **Ajuste de Plano (`wobjdata`):** Para absorber desalineaciones mecánicas o variaciones de altura de la banda transportadora entre sesiones de laboratorio, la trayectoria se vinculó a un `wobjdata`, permitiendo re-calibrar el offset en $Z$ sin reprogramar los puntos del dibujo.

### 4. Secuencia de Operación y Modos de Trabajo
La celda se gestiona desde la botonera de control vinculada a las entradas y salidas digitales del controlador:

1. **Rutina 1: Ciclo Automático de Decoración (`DI_01` / `DO_01` - Testigo 1):**
   * El pastel ingresa por la banda transportadora (`FWD_Conveyor = 1`).
   * Al posicionarse frente al robot, la banda se detiene y se activa el Testigo 1 (`DO_01 = 1`).
   * El robot desciende y ejecuta el trazado completo (Pac-Man y nombres).
   * Al finalizar, se eleva a la posición segura `HOME`, el Testigo 1 se apaga y la banda reanuda su marcha para entregar el producto terminado.
2. **Rutina 2: Pose de Mantenimiento (`DI_02` / `DO_02` - Testigo 2):**
   * La banda se detiene y el manipulador se desplaza hacia una posición elevada de fácil acceso frontal.
   * Permite la inspección visual, reemplazo o ajuste de altura del marcador. El Testigo 2 permanece encendido como indicador de estado.
3. **Rutina 3: Coreografía "Farmear Aura" (`DI_03` / `DO_03` - Testigo 3):**
   * Con la banda detenida, se activa el Testigo 3.
   * El robot ejecuta una rutina de reorientación continua del TCP en el aire mediante bucles y condicionales. Al terminar, retorna a la pose `HOME` y deshabilita la salida.
* ## Diagrama de flujo de la secuencia completa: ##
* Lógica de control para el ciclo automático (`DI_01`), pose de mantenimiento (`DI_02`) y rutina Farmear Aura (`DI_03`).

 ```mermaid
flowchart TD
    Start["Inicio: Espera de Señal"] --> CheckDI{"¿Qué botón se presionó?"}

    %% Ciclo Automático
    CheckDI -- "DI_01" --> R1_Start["Activar FWD_Conveyor = 1<br/>Testigo DO_01 = 1"]
    R1_Start --> R1_Wait["Esperar posición del pastel<br/>WaitTime"]
    R1_Wait --> R1_Stop["Detener banda<br/>FWD_Conveyor = 0"]
    R1_Stop --> R1_MoveJ1["MoveJ a aproximación<br/>Z = -10 mm"]
    R1_MoveJ1 --> R1_MoveL1["MoveL trazado Pac-Man<br/>y nombres del equipo"]
    R1_MoveL1 --> R1_MoveJ2["MoveJ elevación<br/>a posición segura"]
    R1_MoveJ2 --> R1_End["Apagar Testigo DO_01 = 0<br/>FWD_Conveyor = 1 para entregar"]
    R1_End --> HOME["Retorno a HOME"]
    
    %% Mantenimiento
    CheckDI -- "DI_02" --> R2_Start["Detener banda<br/>Activar DO_02 = 1"]
    R2_Start --> R2_MoveJ["MoveJ a pose elevada<br/>de acceso frontal"]
    R2_MoveJ --> R2_Wait["Esperar reajuste / inspección<br/>WaitTime o señal"]
    R2_Wait --> R2_End["Apagar Testigo DO_02 = 0"]
    R2_End --> HOME
    
    %% Farmer Aura
    CheckDI -- "DI_03" --> R3_Start["Detener banda<br/>Activar DO_03 = 1"]
    R3_Start --> R3_Loop["Iniciar bucle FOR/WHILE<br/>Reorientación continua del TCP"]
    R3_Loop --> R3_End["Apagar Testigo DO_03 = 0"]
    R3_End --> HOME

    %% Banda y salidas
    BWD_Conveyor["BWD_Conveyor = 1<br/>Retroceso de banda"] -.-> R1_Start
    Reset["Reset / Enclavamientos"] -.-> R1_Stop
```

  
* **Plano de planta de la celda:** Disposición espacial del robot, la banda transportadora y zonas de trabajo.

## Descripción de Instrucciones y Funciones de RAPID Utilizadas

### Declaraciones de Datos y Estructuras
* **`MODULE ... ENDMODULE`**: Encapsula y organiza todo el código, rutinas, datos y variables del programa en una unidad lógica dentro del controlador RAPID.
* **`PERS tooldata`**: Declara un dato persistente (`MyNewTool`) que almacena las propiedades físicas y geométricas de la herramienta porta-marcador. Define las coordenadas cartesianas del TCP ($X, Y, Z$), la orientación mediante cuaterniones y las características de masa/centro de gravedad.
* **`TASK PERS wobjdata`**: Define el sistema de coordenadas de trabajo (`Workobject_2`). Permite referenciar todas las trayectorias de la torta a un plano específico, facilitando la reutilización del trazado en distintas ubicaciones cuadrantes ( $x(+), y(+)$ y $x(+), y(-)$ ) sin reprogramar los puntos individuales.
* **`CONST robtarget`**: Define constantes de posición cartesiana (`Target_10`, `Target_20`, etc.). Almacenan las coordenadas tridimensionales de aproximación y trazado, la orientación del TCP y la configuración de ejes del robot.

### Instrucciones de Movimiento
* **`MoveJ`**: Realiza movimientos articulares rápidos hacia una posición. Se utiliza para desplazamientos en el aire donde la trayectoria intermedia no requiere ser una línea recta, como aproximaciones iniciales, elevaciones a la z-segura (puntos con $Z = -10\text{ mm}$) o retornos a la posición **HOME**.
* **`MoveL`**: Ejecuta movimientos rectilíneos controlados. Mantiene la punta del marcador en trayectoria recta a velocidad constante, utilizado para el trazado continuo sobre el pastel de los nombres y la figura de Pac-Man.

### Control de Entradas/Salidas y Sincronización
* **`Set`**: Activa una señal de salida digital poniéndola en nivel alto (`1`). Se utiliza para encender las salidas indicadoras (`DO_01`, `DO_02`, `DO_03`) o accionar el movimiento de la banda transportadora (`FWD_Conveyor`).
* **`Reset`**: Desactiva una salida digital poniéndola en nivel bajo (`0`). Se utiliza para apagar las señales indicadoras y aplicar enclavamientos de seguridad que impiden accionar simultáneamente el avance y retroceso de la banda (`FWD_Conveyor` y `BWD_Conveyor`).
* **`WaitTime`**: Detiene la ejecución del código durante un tiempo determinado en segundos. Permite estabilizar la banda transportadora tras enviar el comando de paro antes de que el robot inicie el contacto con el pastel.

### Lógica y Estructuras de Control
* **`PROC ... ENDPROC`**: Delimita procedimientos y subrutinas modulares. Permite segmentar las tareas del programa (como el control de la banda, la rutina de decoración o la rutina *Farmear Aura*) para llamarlas desde el procedimiento principal.
* **`IF ... THEN ... ELSE ... ENDIF`**: Estructura condicional utilizada para conmutar entre los modos de operación evaluando el estado de las entradas digitales (`DI_01`, `DI_02`, `DI_03`) y controlar fallos o límites de alcanzabilidad.
* **`WHILE ... ENDWHILE`**: Bucle condicional que repite un bloque de código mientras la condición sea Verdadera (`TRUE`). Se utiliza en la rutina principal para mantener el sistema escuchando continuamente las señales de entrada.
* **`FOR ... FROM ... TO ... DO ... ENDFOR`**: Ciclo de repetición con contador definido. Se emplea en la secuencia creativa (*Farmear Aura*) para ejecutar bucles iterativos de movimiento durante la coreografía del manipulador.

