import requests
from Assets import Estatua
from Assets import Semaforo
from Assets import Banca
from Assets import Arbol
from Assets import Banquetas
from Assets import Calle
from Edificios import Carne
from Edificios import Banco
from Edificios import Circle
from Edificios import Monton
from Edificios import Zara
from Edificios import Edificio6
from Edificios import Edificio5
from Edificios import Edificio4
from Edificios import Edificio3
from Edificios import Edificio2
from Edificios import Edificio1
from Edificios import Pampas
from Assets import Coche
import pygame
from pygame.locals import *
import socket
import time


# Cargamos las bibliotecas de OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import threading

from objloader import *

# Se carga el archivo de la clase Cubo
import sys

sys.path.append('..')
# from Assets import Edificio


def obtener_direccion_ipv4():
    try:
        # Obtener el nombre del host local
        hostname = socket.gethostname()

        # Obtener la dirección IPv4 asociada con el nombre del host
        direccion_ipv4 = socket.gethostbyname(hostname)

        return direccion_ipv4
    except Exception as e:
        print("Error al obtener la dirección IPv4:", str(e))
        return None
    
def play_sound(file):
    pygame.mixer.Sound(file).play()

def show_configuration_window():
    pygame.init()
    screen = pygame.display.set_mode((350, 200))
    pygame.display.set_caption("Simulation Speed Configuration")
    
    pygame.mixer.init()  # Initialize Pygame mixer for audio

    # Load audio files
    sound_file = "sounds/sound.mp3"
    nsound_file = "sounds/nsound.mp3"

    sound = pygame.mixer.Sound(sound_file)
    nsound = pygame.mixer.Sound(nsound_file)

    # Inicializa la velocidad con un valor predeterminado
    running_speed = 4.0

    # Configuración de eventos
    speed_change_rate = 0.1
    key_repeat_delay = 200  # Milisegundos
    key_repeat_interval = 50  # Milisegundos

    last_key_time = 0
    key_repeat = False
    nsound_played = False  # Flag to track if nsound has been played

    # Loop para la ventana de configuración
    running = True

    while running:
        current_time = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    exit()
                elif event.key == K_RETURN:
                    running = False
                elif event.key == K_UP:
                    if current_time - last_key_time > key_repeat_delay:
                        running_speed += speed_change_rate
                        running_speed = min(10.0, running_speed)  # Límite superior
                        last_key_time = current_time
                        key_repeat = True
                        play_sound(sound_file)  # Play sound when key is pressed
                elif event.key == K_DOWN:
                    if current_time - last_key_time > key_repeat_delay:
                        running_speed -= speed_change_rate
                        running_speed = max(0.1, running_speed)  # Límite inferior
                        last_key_time = current_time
                        key_repeat = True
                        play_sound(sound_file)  # Play sound when key is pressed
            elif event.type == KEYUP:
                if event.key in (K_UP, K_DOWN):
                    key_repeat = False

        if key_repeat:
            if current_time - last_key_time > key_repeat_interval:
                if pygame.key.get_pressed()[K_UP]:
                    running_speed += speed_change_rate
                    running_speed = min(10.0, running_speed)  # Límite superior
                elif pygame.key.get_pressed()[K_DOWN]:
                    running_speed -= speed_change_rate
                    running_speed = max(0.1, running_speed)  # Límite inferior
                last_key_time = current_time

        if not nsound_played and (running_speed == 0.1 or running_speed == 10.0):
            play_sound(nsound_file)  # Play sound when the limit is reached
            nsound_played = True  # Set the flag to indicate nsound has been played

        if nsound_played and running_speed != 0.1 and running_speed != 10.0:
            nsound_played = False  # Reset the flag when the speed is no longer at the limit

        screen.fill((255, 255, 255))
        font = pygame.font.Font(None, 36)
        text = font.render(f"Speed: {running_speed:.1f}", True, (0, 0, 0))
        text_rect = text.get_rect(center=(175, 150))
        screen.blit(text, text_rect)

        # Display the message above the speed display
        message_font = pygame.font.Font(None, 24)
        message_text = message_font.render("Press Up or Down Keys to Change Speed", True, (0, 0, 0))
        message_rect = message_text.get_rect(center=(175, 50))
        screen.blit(message_text, message_rect)
        icon = pygame.image.load("icon.png")
        pygame.display.set_icon(icon)

        pygame.display.update()

    pygame.quit()
    return running_speed





URL_BASE = "http://"+obtener_direccion_ipv4()+":5000"

r = requests.post(URL_BASE + "/games", allow_redirects=False)
print(r)
LOCATION = r.headers["Location"]

lista = r.json()

# Variables para controlar la vista con el mouse
mouse_x, mouse_y = 0, 0
rotate_x, rotate_y = 0, 0
mouse_down = False

screen_width = 500
screen_height = 500


# texturas
textures = []
mpF = "texturas/mrpampas.jpeg"
ed1 = "texturas/edificio1.jpg"
z1 = "texturas/zara1.jpg"
te1 = "texturas/techoe1.jpg"
ed2 = "texturas/edificio2.jpg"
te2 = "texturas/techo2.jpg"
z2 = "texturas/zara2.jpg"
z3 = "texturas/zara3.jpg"
mp2 = "texturas/mrpampas2.jpg"
piso = "texturas/piso1.jpg"
eds = "texturas/edificios.jpeg"
edsI = "texturas/edificiosI.jpeg"
edsD = "texturas/edificiosD.jpeg"
edsT = "texturas/edificiosT.jpg"
cir = "texturas/circle.jpg"
teR = "texturas/techoRojo.jpg"
ed3 = "texturas/edificio3.jpeg"
cua = "texturas/cuadrado.jpg"
ban = "texturas/banco.jpeg"
teb = "texturas/blanco.jpg"
banL = "texturas/bancoL.jpeg"
ed4 = "texturas/edificio4.jpg"
crn = "texturas/carne.jpeg"
crn2 = "texturas/carne2.jpg"
ed5 = "texturas/edificio5.jpg"
calle = "texturas/calle.jpg"
calle2 = "texturas/calle2.jpg"
clouds = "texturas/sky_clouds.jpg"

# vc para el obser.
FOVY = 60.0
ZNEAR = 0.01
ZFAR = 5000.0
# Variables para definir la posicion del observador
# gluLookAt(EYE_X,EYE_Y,EYE_Z,CENTER_X,CENTER_Y,CENTER_Z,UP_X,UP_Y,UP_Z)
EYE_X = 300.0
EYE_Y = 200.0
EYE_Z = 300.0
CENTER_X = 0
CENTER_Y = 0
CENTER_Z = 0
UP_X = 0
UP_Y = 1
UP_Z = 0
# Variables para dibujar los ejes del sistema
X_MIN = -500
X_MAX = 500
Y_MIN = -500
Y_MAX = 500
Z_MIN = -500
Z_MAX = 500
# Dimension del plano
DimBoard = 200

running_speed = show_configuration_window()

pygame.init()

clock = pygame.time.Clock()
previous_time = pygame.time.get_ticks()
dt = 0


agents = {}

print(lista)
count = 0
positions = [[-90, 25, -55], [-55, 25, 90], [55, 25, -90], [90, 25, 55]]
for agent in lista:
    if agent["type"] == "Car":
        agenti = Coche(agent["x"]* 20 - 160, agent["z"]* 20 - 160)
        agents[agent["id"]] = agenti
    elif agent["type"] == "TrafficLight":
        agenti = Semaforo(positions[count])
        count += 1
        print(agenti.position[0], agenti.position[2],
              "real position:", agent["x"], agent["z"])
        agents[agent["id"]] = agenti



circuloG = Calle(DimBoard)
circuloP = Calle(DimBoard)
banqueta1 = Banquetas(115, 5)
# estatua = Estatua(DimBoard)
edificio = Pampas()
edificio2 = Edificio1()
edificio3 = Zara()
edificio4 = Edificio2()
edificio5 = Monton()

edificio6 = Edificio3()
edificio7 = Edificio4()
edificio8 = Banco()
edificio9 = Edificio5()

edificio10 = Circle()
edificio11 = Carne()
edificio12 = Edificio6()
# edificio13 = Edificio(110,40)

arbol1 = Arbol(DimBoard)
arbol2 = Arbol(DimBoard)

banco1 = Banca(DimBoard)

estatua = Estatua(DimBoard)


def Texturas(filepath):
    textures.append(glGenTextures(1))
    id = len(textures) - 1
    glBindTexture(GL_TEXTURE_2D, textures[id])
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    image = pygame.image.load(filepath).convert()
    w, h = image.get_rect().size
    image_data = pygame.image.tostring(image, "RGBA")
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, w, h, 0,
                 GL_RGBA, GL_UNSIGNED_BYTE, image_data)
    glGenerateMipmap(GL_TEXTURE_2D)


def Init():
    screen = pygame.display.set_mode(
        (screen_width, screen_height), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Roundabout Simulation")

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(FOVY, screen_width/screen_height, ZNEAR, ZFAR)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(EYE_X, EYE_Y, EYE_Z, CENTER_X,
              CENTER_Y, CENTER_Z, UP_X, UP_Y, UP_Z)
    glClearColor(0.53, 0.81, 0.92, 1.0)
    glEnable(GL_DEPTH_TEST)
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

    Texturas(mpF)  # 0
    Texturas(ed1)  # 1
    Texturas(z1)  # 2
    Texturas(te1)  # 3
    Texturas(ed2)  # 4
    Texturas(te2)  # 5
    Texturas(z2)  # 6
    Texturas(z3)  # 7
    Texturas(mp2)  # 8
    Texturas(piso)  # 9
    Texturas(eds)  # 10
    Texturas(edsI)  # 11
    Texturas(edsD)  # 12
    Texturas(edsT)  # 13
    Texturas(cir)  # 14
    Texturas(teR)  # 15
    Texturas(ed3)  # 16
    Texturas(cua)  # 17
    Texturas(ban)  # 18
    Texturas(teb)  # 19
    Texturas(banL)  # 20
    Texturas(ed4)  # 21
    Texturas(crn)  # 22
    Texturas(crn2)  # 23
    Texturas(ed5)  # 24
    Texturas(calle)  # 25
    Texturas(calle2)  # 26
    Texturas(clouds)  # 27

    for agent in lista:
        if agent["type"] == "Car":
            agents[agent["id"]].cargar()

    # edificio1.cargar("4floorBuilding_Night_OBJ.obj")
    # hotel.cargar("Hotel(3star).obj")
    arbol1.cargar()
    arbol2.cargar()
    banco1.cargar()
    # estatua.cargar()


def PlanoTexturizado():
    glColor3f(1.0, 1.0, 1.0)
    glEnable(GL_TEXTURE_2D)
    # Front face
    glBindTexture(GL_TEXTURE_2D, textures[0])
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3d(-DimBoard, 0, -DimBoard)
    glTexCoord2f(0.0, 1.0)
    glVertex3d(-DimBoard, 0, DimBoard)
    glTexCoord2f(1.0, 1.0)
    glVertex3d(DimBoard, 0, DimBoard)
    glTexCoord2f(1.0, 0.0)
    glVertex3d(DimBoard, 0, -DimBoard)
    glEnd()
    glDisable(GL_TEXTURE_2D)


def render_skybox():
    # Save the current state of the ModelView matrix
    glPushMatrix()
    glLoadIdentity()

    # Set the skybox size (a large value to cover the scene)
    skybox_size = 2000.0

    glEnable(GL_TEXTURE_2D)

    # Bind the single cloud texture to all faces of the skybox
    glBindTexture(GL_TEXTURE_2D, textures[27])

    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3d(-skybox_size, -skybox_size, -skybox_size)
    glTexCoord2f(1.0, 0.0)
    glVertex3d(skybox_size, -skybox_size, -skybox_size)
    glTexCoord2f(1.0, 1.0)
    glVertex3d(skybox_size, skybox_size, -skybox_size)
    glTexCoord2f(0.0, 1.0)
    glVertex3d(-skybox_size, skybox_size, -skybox_size)
    glEnd()

    glDisable(GL_TEXTURE_2D)

    # Restore the previous ModelView matrix
    glPopMatrix()
    glPushMatrix()

    # backface
    glBindTexture(GL_TEXTURE_2D, textures[27])
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3d(-skybox_size, -skybox_size, -skybox_size)
    glTexCoord2f(1.0, 0.0)
    glVertex3d(skybox_size, -skybox_size, -skybox_size)
    glTexCoord2f(1.0, 1.0)
    glVertex3d(skybox_size, skybox_size, -skybox_size)
    glTexCoord2f(0.0, 1.0)
    glVertex3d(-skybox_size, skybox_size, -skybox_size)
    glEnd()

    glDisable(GL_TEXTURE_2D)

    # Restore the previous ModelView matrix
    glPopMatrix()


def display():
    global dt, running_speed
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    for agent in lista:
        agenti = agents[agent["id"]] 
        if isinstance(agenti, Coche):  
            if agent["condition"] == "SHOWN":
                agenti.set_target_position(
                agent["x"] * 20 - 160, agent["z"] * 20 - 160, agent["direction"])
                agenti.update(dt*running_speed) 
                agenti.draw()
            elif agent["x"]* 20 - 160!=agenti.Position[0] or agent["z"]* 20 - 160!=agenti.Position[2]:
                agenti.set_target_position(
                agent["x"] * 20 - 160, agent["z"] * 20 - 160, agent["direction"])
        if isinstance(agenti, Semaforo):
            agenti.draw()
            agenti.update(agent["condition"])

    render_skybox()
    
    circuloG.draw(100, 100, textures)
    circuloG.drawRectangulo1(textures)
    circuloG.drawRectangulo2(textures)
    circuloP.draw2(35, 100)
    banqueta1.draw(-50, 3, 143)
    banqueta1.draw(50, 3, -143)
    banqueta1.draw(-50, 3, -143)
    banqueta1.draw(50, 3, 143)

    edificio.draw(textures, -120, 0, 140)
    edificio2.draw(textures, 95, 0, 110)
    edificio3.draw(textures, 100, 0, 170)
    edificio4.draw(textures, 165, 0, 170)
    edificio5.draw(textures, -183, 0, 125)

    edificio6.draw(textures, 110, 0, -85)
    edificio7.draw(textures, 170, 0, -95)
    edificio8.draw(textures, 95, 0, -155)
    edificio9.draw(textures, 165, 0, -160)

    edificio10.draw(textures, -100, 0, -115)
    edificio11.draw(textures, -130, 0, -180)
    edificio12.draw(textures, -165, 0, -95)
    # edificio13.draw2(-175,55,-150)

    arbol1.draw(-110, 0, -68)
    arbol2.draw(155, 0, 100)
    banco1.draw(180, 0, 115)
    banco1.draw(-115, 0, 75)

    # estatua.draw(0,3,0)

    # Se dibuja el plano gris
    glColor3f(0.3, 0.3, 0.3)
    glBegin(GL_QUADS)
    glVertex3d(-DimBoard, 0, -DimBoard)
    glVertex3d(-DimBoard, 0, DimBoard)
    glVertex3d(DimBoard, 0, DimBoard)
    glVertex3d(DimBoard, 0, -DimBoard)
    glEnd()


def handle_mouse_input(event):
    global rotate_x, rotate_y, mouse_x, mouse_y, mouse_down

    if event.type == pygame.MOUSEMOTION:
        if mouse_down:
            dx, dy = event.rel
            rotate_x += dy
            rotate_y += dx

    elif event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:  # Botón izquierdo del mouse
            mouse_down = True

    elif event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1:  # Botón izquierdo del mouse
            mouse_down = False


def update_view():
    glLoadIdentity()
    gluLookAt(
        EYE_X, EYE_Y, EYE_Z,
        CENTER_X, CENTER_Y, CENTER_Z,
        UP_X, UP_Y, UP_Z
    )
    glRotatef(rotate_x, 1, 0, 0)
    glRotatef(rotate_y, 0, 1, 0)


def get_data_from_server():
    global lista, running_speed
    while True:
        response = requests.get(URL_BASE + LOCATION)
        lista = response.json()
        time.sleep(1/running_speed)


# Crea un temporizador para realizar la primera solicitud después de 0 segundos
data_timer = threading.Timer(0, get_data_from_server)
data_timer.daemon = True
data_timer.start()


done = False
Init()
while not done:
    current_time = pygame.time.get_ticks()
    dt = (current_time - previous_time) / 1000.0
    previous_time = current_time
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION):
            handle_mouse_input(event)

    # Actualiza la vista con los datos actualizados del servidor
    display()
    update_view()
    pygame.display.flip()
    clock.tick(60)

    icon = pygame.image.load("icon.png")
    pygame.display.set_icon(icon)
pygame.quit()
