from robodk.robolink import *    # API para comunicarte con RoboDK
from robodk.robomath import *    # Funciones matemáticas
import math
from matplotlib.textpath import TextPath
from matplotlib.font_manager import FontProperties
from matplotlib.transforms import Affine2D

#------------------------------------------------
# 1) Conexión a RoboDK e inicialización
#------------------------------------------------
RDK = Robolink()

# Elegir un robot (si hay varios, aparece un popup)
robot = RDK.ItemUserPick("Selecciona un robot", ITEM_TYPE_ROBOT)
if not robot.Valid():
    raise Exception("No se ha seleccionado un robot válido.")

# Conectar al robot físico
#if not robot.Connect():
#    raise Exception("No se pudo conectar al robot. Verifica que esté en modo remoto y que la configuración sea correcta.")

# Confirmar conexión
#if not robot.ConnectedState():
#    raise Exception("El robot no está conectado correctamente. Revisa la conexión.")

#print("Robot conectado correctamente.")

def revisar_estado():
    estado, mensaje = robot.ConnectedState()

    if estado != ROBOTCOM_READY:
        robot.Stop()
        raise Exception("El robot dejó de estar listo: " + mensaje)

#------------------------------------------------
# 2) Cargar el Frame (ya existente) donde quieres dibujar
#    Ajusta el nombre si tu Frame se llama diferente
#------------------------------------------------
frame_name = "Frame_from_Target1"
frame = RDK.Item(frame_name, ITEM_TYPE_FRAME)
if not frame.Valid():
    raise Exception(f'No se encontró el Frame "{frame_name}" en la estación.')

#revisar_estado()
robot.MoveJ(robot.JointsHome())

# Asignamos este frame al robot
robot.setPoseFrame(frame)
# Usamos la herramienta activa
robot.setPoseTool(robot.PoseTool())

# Ajustes de velocidad y blending
robot.setSpeed(100)   # mm/s - Ajusta según necesites
robot.setRounding(2)  # blending (radio de curvatura)         __________ERROR__________Ajustarlos a la figura, no puede ser rosa polar, ni circulo

#------------------------------------------------
# 3) Parámetros de la figura
#------------------------------------------------
num_points = 180       # Cuántos puntos muestreamos (mayor = más suave)           __________ERROR__________ encontrar un equilibrio entre numero de puntos y que la figura se vea bien, no se pueden colocaar muchos puntos porque se satura el internet
A = 150                # Amplitud (150 mm = radio máximo)
n = 3                  # Numerador de la curva polar
d = 5                  # Denominador de la curva polar
z_surface = 0          # Z=0 en el plano del frame
z_safe = 50             # Altura segura para aproximarse y salir              ____________ERROR________ la diracción de z está positivo hacia dentro

#------------------------------------------------
# 4) Movimiento al centro en altura segura
#------------------------------------------------
# El centro de la rosa (r=0) corresponde a x=0, y=0
#revisar_estado()
robot.MoveJ(transl(0, 0, z_surface - z_safe))

# Bajamos a la "superficie" (Z=0)
#revisar_estado()
robot.MoveL(transl(0, 0, z_surface))

#------------------------------------------------
# 5) Dibujar la rosa polar
#    r = A * sin(k*theta)
#    x = r*cos(theta), y = r*sin(theta)
#------------------------------------------------
# Recorremos la figura completa comenzando y terminando en el centro
theta_start = 5*math.pi/6
theta_span = 5*math.pi

for i in range(num_points+1):
    # Fracción entre 0 y 1
    t = i / num_points
    # Ángulo actual
    theta = theta_start + theta_span * t

    # Calculamos r
    r = A * math.cos((n/d) * theta)

    # Convertimos a coordenadas Cartesianas X, Y
    x = r * math.cos(theta)
    y = r * math.sin(theta)

    # Movemos linealmente (MoveL) en el plano del Frame
    #revisar_estado()
    robot.MoveL(transl(x, y, z_surface))               # ____________ERROR___________ no se puede repizar la figura, solo se hace una vez

# Al terminar, subimos de nuevo para no chocar
#revisar_estado()
robot.MoveL(transl(x, y, z_surface - z_safe))

#------------------------------------------------
# 6) Dibujar los nombres
#------------------------------------------------
nombres = ["Sharon", "Esteban", "Fabián"]
fuente = FontProperties(family="DejaVu Sans")

tamano = 150
escala = 25.4 / 72

posiciones = [
    (50, -370),
    (0, -370),
    (-50, -370)
]

for nombre, posicion in zip(nombres, posiciones):
    texto = TextPath((0, 0), nombre, size=tamano, prop=fuente)
    texto = texto.transformed(Affine2D().rotate_deg(90))
    letras = texto.to_polygons(closed_only=False)

    for letra in letras:
        if len(letra) < 2:
            continue

        x = posicion[0] - letra[0][0] * escala
        y = posicion[1] + letra[0][1] * escala

        #revisar_estado()
        robot.MoveL(transl(x, y, z_surface - z_safe))
        #revisar_estado()
        robot.MoveL(transl(x, y, z_surface))

        for punto in letra[1:]:
            x = posicion[0] - punto[0] * escala
            y = posicion[1] + punto[1] * escala
            #revisar_estado()
            robot.MoveL(transl(x, y, z_surface))
        
        #revisar_estado()
        robot.MoveL(transl(x, y, z_surface - z_safe))

robot.MoveJ(robot.JointsHome())

print(f"¡Trayectoria completada en el frame '{frame_name}'!")          #____________ERROR__________ Tiene que comenzar en home y volver a home
