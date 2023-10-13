
from pygame.locals import *

# Cargamos las bibliotecas de OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from objloader import *
import math


class Coche:
    def __init__(self, x, z):
        self.Position = [x, 4.0, z]
        self.speed = 0.1
        self.position_buffer = []
        self.direction = [1, 0]

    def cargar(self):
        global obj
        obj = OBJ("objetos3D/Car.obj", swapyz=True)
        obj.generate()

    def update(self, new_x, new_z, direction):
        self.direction = direction
        self.Position = [new_x, self.Position[1], new_z]
        # if self.Position != [new_x, self.Position[1], new_z]:
        #     self.position_buffer.append([new_x, self.Position[1], new_z, direction])

    # def move(self):
    #     if self.position_buffer:
    #         new_x, new_y, new_z, direction = self.position_buffer[0]

    #         delta_x = new_x - self.Position[0]
    #         delta_z = new_z - self.Position[2]
    #         distance = math.sqrt(delta_x**2 + delta_z**2)

    #         if distance > self.speed:
    #             step = [delta_x * self.speed / distance, 0, delta_z * self.speed / distance]
    #             self.Position = [x + y for x, y in zip(self.Position, step)]
    #         else:
    #             self.Position = [new_x, new_y, new_z]
    #             self.position_buffer.pop(0)

    def draw(self):
        global obj
        # self.move()
        glPushMatrix()
        glTranslatef(self.Position[0], 4, self.Position[2])
        glScaled(5, 5, 5)
        if self.direction == [1, 0]:
            glRotatef(90, 0, -1, 0)
        elif self.direction == [-1, 0]:
            glRotatef(90, 0, 1, 0)
        elif self.direction == [0, 1]:
            glRotatef(180, 0, 1, 0)

        glRotatef(90, -1, 0, 0)
        obj.render()
        glPopMatrix()


class Banquetas:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def draw(self, x, y, z):
        glPushMatrix()
        glTranslatef(x, y, z)
        # glRotatef(90, -1, 0, 0)

        half_largo = self.largo / 2.0
        half_ancho = self.ancho / 2.0

        glBegin(GL_QUADS)
        glColor3f(1.0, 1.0, 0.0)  # Amarillo (R=1.0, G=1.0, B=0.0)

        # Cara frontal
        glVertex3f(-half_ancho, -half_ancho, -half_largo)
        glVertex3f(half_ancho, -half_ancho, -half_largo)
        glVertex3f(half_ancho, half_ancho, -half_largo)
        glVertex3f(-half_ancho, half_ancho, -half_largo)

        # Cara trasera
        glVertex3f(-half_ancho, -half_ancho, half_largo)
        glVertex3f(half_ancho, -half_ancho, half_largo)
        glVertex3f(half_ancho, half_ancho, half_largo)
        glVertex3f(-half_ancho, half_ancho, half_largo)

        # Cara izquierda
        glVertex3f(-half_ancho, -half_ancho, -half_largo)
        glVertex3f(-half_ancho, half_ancho, -half_largo)
        glVertex3f(-half_ancho, half_ancho, half_largo)
        glVertex3f(-half_ancho, -half_ancho, half_largo)

        # Cara derecha
        glVertex3f(half_ancho, -half_ancho, -half_largo)
        glVertex3f(half_ancho, half_ancho, -half_largo)
        glVertex3f(half_ancho, half_ancho, half_largo)
        glVertex3f(half_ancho, -half_ancho, half_largo)

        # Cara superior
        glVertex3f(-half_ancho, half_ancho, -half_largo)
        glVertex3f(half_ancho, half_ancho, -half_largo)
        glVertex3f(half_ancho, half_ancho, half_largo)
        glVertex3f(-half_ancho, half_ancho, half_largo)

        # Cara inferior
        glVertex3f(-half_ancho, -half_ancho, -half_largo)
        glVertex3f(half_ancho, -half_ancho, -half_largo)
        glVertex3f(half_ancho, -half_ancho, half_largo)
        glVertex3f(-half_ancho, -half_ancho, half_largo)

        glEnd()
        glPopMatrix()

    def draw2(self, x, y, z):
        glPushMatrix()
        glTranslatef(x, y, z)
        # glRotatef(0, 0, 180, 0)

        half_largo = self.largo / 2.0
        half_ancho = self.ancho / 2.0

        glBegin(GL_QUADS)
        glColor3f(1.0, 1.0, 0.0)  # Amarillo (R=1.0, G=1.0, B=0.0)

        # Cara frontal
        glVertex3f(-half_ancho, -half_ancho, -half_largo)
        glVertex3f(half_ancho, -half_ancho, -half_largo)
        glVertex3f(half_ancho, half_ancho, -half_largo)
        glVertex3f(-half_ancho, half_ancho, -half_largo)

        # Cara trasera
        glVertex3f(-half_ancho, -half_ancho, half_largo)
        glVertex3f(half_ancho, -half_ancho, half_largo)
        glVertex3f(half_ancho, half_ancho, half_largo)
        glVertex3f(-half_ancho, half_ancho, half_largo)

        # Cara izquierda
        glVertex3f(-half_ancho, -half_ancho, -half_largo)
        glVertex3f(-half_ancho, half_ancho, -half_largo)
        glVertex3f(-half_ancho, half_ancho, half_largo)
        glVertex3f(-half_ancho, -half_ancho, half_largo)

        # Cara derecha
        glVertex3f(half_ancho, -half_ancho, -half_largo)
        glVertex3f(half_ancho, half_ancho, -half_largo)
        glVertex3f(half_ancho, half_ancho, half_largo)
        glVertex3f(half_ancho, -half_ancho, half_largo)

        # Cara superior
        glVertex3f(-half_ancho, half_ancho, -half_largo)
        glVertex3f(half_ancho, half_ancho, -half_largo)
        glVertex3f(half_ancho, half_ancho, half_largo)
        glVertex3f(-half_ancho, half_ancho, half_largo)

        # Cara inferior
        glVertex3f(-half_ancho, -half_ancho, -half_largo)
        glVertex3f(half_ancho, -half_ancho, -half_largo)
        glVertex3f(half_ancho, -half_ancho, half_largo)
        glVertex3f(-half_ancho, -half_ancho, half_largo)

        glEnd()
        glPopMatrix()


class Calle:
    def __init__(self, dim):
        self.Dimboard = dim

    def draw(self, radius, num, textures):
        glPushMatrix()
        glTranslatef(0, 2.5, 0)
        glRotatef(90, -1, 0, 0)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[26])
        gluDisk(gluNewQuadric(), 0, radius, num, 1)
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

    def drawRectangulo1(self, textures):
        glPushMatrix()
        glTranslatef(0, 1.5, 0)
        # glRotatef(90, -1, 0, 0)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[25])
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(200, 0, 50)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(200, 0, -50)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-200, 0, -50)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-200, 0, 50)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

    def drawRectangulo2(self, textures):
        glPushMatrix()
        glTranslatef(0, 1.5, 0)
        # glRotatef(90, -1, 0, 0)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[25])
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(50, 0, -200)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(-50, 0, -200)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-50, 0, 200)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(50, 0, 200)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

    def draw2(self, radius, num):
        glPushMatrix()
        glTranslatef(0, 4, 0)
        glRotatef(90, -1, 0, 0)
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0.3, 0.3, 0.3)  # Color gris
        for i in range(num + 1):
            theta = 2.0 * math.pi * float(i) / float(num)
            x = radius * math.cos(theta)  # Añadir el centro_x
            z = radius * math.sin(theta)  # Añadir el center_z
            glVertex2f(x, z)
        glEnd()
        glPopMatrix()


class Semaforo:
    def __init__(self, x, z):
        self.position = [x, 4, z]
        self.largo = 50
        self.ancho = 5
        self.condition = False

    def update(self, condition):
        self.condition = condition

    def draw(self):
        glPushMatrix()
        glTranslatef(self.position[0], 4, self.position[2])
        glRotatef(90, -1, 0, 0)

        half_largo = self.largo / 2.0
        half_ancho = self.ancho / 2.0

        glBegin(GL_QUADS)
        if self.condition:
            glColor3f(0.0, 1.0, 0.0)  # Color verde
        else:
            glColor3f(1.0, 0.0, 0.0)  # Color rojo

        # Cara frontal
        glVertex3f(-half_ancho, -half_ancho, -half_largo)
        glVertex3f(half_ancho, -half_ancho, -half_largo)
        glVertex3f(half_ancho, half_ancho, -half_largo)
        glVertex3f(-half_ancho, half_ancho, -half_largo)

        # Cara trasera
        glVertex3f(-half_ancho, -half_ancho, half_largo)
        glVertex3f(half_ancho, -half_ancho, half_largo)
        glVertex3f(half_ancho, half_ancho, half_largo)
        glVertex3f(-half_ancho, half_ancho, half_largo)

        # Cara izquierda
        glVertex3f(-half_ancho, -half_ancho, -half_largo)
        glVertex3f(-half_ancho, half_ancho, -half_largo)
        glVertex3f(-half_ancho, half_ancho, half_largo)
        glVertex3f(-half_ancho, -half_ancho, half_largo)

        # Cara derecha
        glVertex3f(half_ancho, -half_ancho, -half_largo)
        glVertex3f(half_ancho, half_ancho, -half_largo)
        glVertex3f(half_ancho, half_ancho, half_largo)
        glVertex3f(half_ancho, -half_ancho, half_largo)

        # Cara superior
        glVertex3f(-half_ancho, half_ancho, -half_largo)
        glVertex3f(half_ancho, half_ancho, -half_largo)
        glVertex3f(half_ancho, half_ancho, half_largo)
        glVertex3f(-half_ancho, half_ancho, half_largo)

        # Cara inferior
        glVertex3f(-half_ancho, -half_ancho, -half_largo)
        glVertex3f(half_ancho, -half_ancho, -half_largo)
        glVertex3f(half_ancho, -half_ancho, half_largo)
        glVertex3f(-half_ancho, -half_ancho, half_largo)

        glEnd()
        glColor3f(1.0, 1.0, 1.0)
        glPopMatrix()


class Arbol:
    def __init__(self, dim):
        self.DimBoard = dim

    def cargar(self):
        global obj2
        obj2 = OBJ("objetos3D/Lowpoly_tree_sample.obj", swapyz=True)
        obj2.generate()

    def draw(self, x, y, z):
        global obj2
        glPushMatrix()
        glTranslatef(x, y, z)
        glScaled(3, 3, 3)
        glRotatef(90, -1, 0, 0)
        obj2.render()
        glPopMatrix()


class Banca:
    def __init__(self, dim):
        self.DimBoard = dim

    def cargar(self):
        global obj3
        obj3 = OBJ("objetos3D/Bench_LowRes.obj", swapyz=True)
        obj3.generate()

    def draw(self, x, y, z):
        global obj3
        glPushMatrix()
        glTranslatef(x, y, z)
        glScaled(0.1, 0.1, 0.1)
        glRotatef(90, -1, 0, 0)
        obj3.render()
        glPopMatrix()


class Estatua:
    def __init__(self, dim):
        self.DimBoard = dim

    def cargar(self):
        global obj4
        obj4 = OBJ("objetos3D/fountain1_0002.obj", swapyz=True)
        obj4.generate()

    def draw(self, x, y, z):
        global obj4
        glPushMatrix()
        glTranslatef(x, y, z)
        # glScaled(0.1, 0.1, 0.1)
        glRotatef(90, -1, 0, 0)
        obj4.render()
        glPopMatrix()
