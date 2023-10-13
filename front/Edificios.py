
from pygame.locals import *

# Cargamos las bibliotecas de OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from objloader import *


class Pampas:
    def __init__(self):
        self.vertexCoords = [
            # Cara frontal
            50, 40, 50,   50, 40, -50,   50, 0, -50,   50, 0, 50,
            # Cara trasera
            -50, 40, 50,    -50, 40, -50,    -50, 0, -50,    -50, 0, 50
        ]

        self.vertexTextureCoords = [
            0.0, 0.0,   # Vértice 0
            0.0, 1.0,   # Vértice 1
            1.0, 1.0,   # Vértice 2
            1.0, 0.0,   # Vértice 3
            0.0, 0.0,   # Vértice 4
            0.0, 1.0,   # Vértice 5
            1.0, 1.0,   # Vértice 6
            1.0, 0.0    # Vértice 7
        ]
        self.elementArray = [
            0, 1, 2, 3, 0, 3, 7, 4, 0, 4, 5, 1,
            6, 2, 1, 5, 6, 5, 4, 7, 6, 7, 3, 2]

        self.vertexColors = [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def draw(self, textures, x, y, z):
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[0])
        glColor3f(1.0, 1.0, 1.0)
        # Frente
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(50, 70, -50)  # X, Y, Z
        glTexCoord2f(0.0, 1.0)
        glVertex3f(50, 0, -50)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(50, 0, 50)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(50, 70, 50)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

        # Derecha
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[8])
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(50, 70, 50)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(50, 0, 50)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-25, 0, 50)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-25, 70, 50)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

        # Izquierda
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[8])
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(50, 0, -50)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(50, 70, -50)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-25, 70, -50)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-25, 0, -50)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

        # Atrás
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[8])
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-25, 0, 50)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-25, 70, 50)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-25, 70, -50)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-25, 0, -50)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

        # Arriba
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[8])
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(50, 70, -50)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(50, 70, 50)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-25, 70, -50)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-25, 70, -50)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()


class Edificio1:
    def __init__(self):
        self.vertexCoords = [
            # Cara frontal
            50, 40, 50,   50, 40, -50,   50, 0, -50,   50, 0, 50,
            # Cara trasera
            -50, 40, 50,    -50, 40, -50,    -50, 0, -50,    -50, 0, 50
        ]

        self.vertexTextureCoords = [
            0.0, 0.0,   # Vértice 0
            0.0, 1.0,   # Vértice 1
            1.0, 1.0,   # Vértice 2
            1.0, 0.0,   # Vértice 3
            0.0, 0.0,   # Vértice 4
            0.0, 1.0,   # Vértice 5
            1.0, 1.0,   # Vértice 6
            1.0, 0.0    # Vértice 7
        ]
        self.elementArray = [
            0, 1, 2, 3, 0, 3, 7, 4, 0, 4, 5, 1,
            6, 2, 1, 5, 6, 5, 4, 7, 6, 7, 3, 2]

        self.vertexColors = [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def draw(self, textures, x, y, z):
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[1])

        # Base
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(25, 120, 25)  # X, Y, Z
        glTexCoord2f(0.0, 1.0)
        glVertex3f(25, 120, -25)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(25, 0, -25)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(25, 0, 25)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

        # Atrás
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[1])
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-25, 120, 25)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(-25, 120, -25)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-25, 0, -25)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-25, 0, 25)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

        # Izquierda
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[1])
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(25, 120, -25)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(-25, 120, -25)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-25, 0, -25)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(25, 0, -25)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

        # Derecha
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[1])
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-25, 120, 25)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(25, 120, 25)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(25, 0, 25)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-25, 0, 25)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

        # Arriba
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[3])
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(25, 120, 25)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(25, 120, -25)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-25, 120, -25)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-25, 120, 25)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()


class Edificio2:
    def __init__(self):
        self.vertexCoords = [
            # Cara frontal
            50, 40, 50,   50, 40, -50,   50, 0, -50,   50, 0, 50,
            # Cara trasera
            -50, 40, 50,    -50, 40, -50,    -50, 0, -50,    -50, 0, 50
        ]

        self.vertexTextureCoords = [
            0.0, 0.0,   # Vértice 0
            0.0, 1.0,   # Vértice 1
            1.0, 1.0,   # Vértice 2
            1.0, 0.0,   # Vértice 3
            0.0, 0.0,   # Vértice 4
            0.0, 1.0,   # Vértice 5
            1.0, 1.0,   # Vértice 6
            1.0, 0.0    # Vértice 7
        ]
        self.elementArray = [
            0, 1, 2, 3, 0, 3, 7, 4, 0, 4, 5, 1,
            6, 2, 1, 5, 6, 5, 4, 7, 6, 7, 3, 2]

        self.vertexColors = [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def draw(self, textures, x, y, z):
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[4])

        # Base
        glBegin(GL_QUADS)

        # glColor3f(0.0, 0.6, 0.0)
        ### ----- Chasis (base) -----###
        # Enfrente
        glTexCoord2f(0.0, 0.0)
        glVertex3f(25, 100, -25)  # X, Y, Z
        glTexCoord2f(0.0, 1.0)
        glVertex3f(25, 0, -25)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(25, 0, 25)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(25, 100, 25)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

        # Atrás
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[4])
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-25, 0, -25)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(-25, 100, -25)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-25, 100, 25)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-25, 0, 25)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

        # Izquierda
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[4])
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(25, 0, -25)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(25, 100, -25)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-25, 100, -25)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-25, 0, -25)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

        # Derecha
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[4])
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-25, 0, 25)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(-25, 100, 25)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(25, 100, 25)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(25, 0, 25)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

        # Arriba
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[3])
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(25, 100, 25)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(25, 100, -25)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-25, 100, -25)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-25, 100, 25)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()


class Zara:
    def __init__(self):
        self.vertexCoords = [
            # Cara frontal
            50, 40, 50,   50, 40, -50,   50, 0, -50,   50, 0, 50,
            # Cara trasera
            -50, 40, 50,    -50, 40, -50,    -50, 0, -50,    -50, 0, 50
        ]

        self.vertexTextureCoords = [
            0.0, 0.0,   # Vértice 0
            0.0, 1.0,   # Vértice 1
            1.0, 1.0,   # Vértice 2
            1.0, 0.0,   # Vértice 3
            0.0, 0.0,   # Vértice 4
            0.0, 1.0,   # Vértice 5
            1.0, 1.0,   # Vértice 6
            1.0, 0.0    # Vértice 7
        ]
        self.elementArray = [
            0, 1, 2, 3, 0, 3, 7, 4, 0, 4, 5, 1,
            6, 2, 1, 5, 6, 5, 4, 7, 6, 7, 3, 2]

        self.vertexColors = [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def draw(self, textures, x, y, z):
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[7])

        # Base
        glBegin(GL_QUADS)

        # glColor3f(0.0, 0.6, 0.0)
        ### ----- Chasis (base) -----###
        # Enfrente
        glTexCoord2f(0.0, 0.0)
        glVertex3f(30, 50, 30)  # X, Y, Z
        glTexCoord2f(0.0, 1.0)
        glVertex3f(30, 50, -30)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(30, 0, -30)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(30, 0, 30)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

        # Atrás
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[2])
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-30, 50, 30)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(-30, 50, -30)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-30, 0, -30)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-30, 0, 30)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

        # Izquierda
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[6])
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(30, 50, -30)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(-30, 50, -30)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-30, 0, -30)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(30, 0, -30)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

        # Derecha
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[6])
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-30, 50, 30)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(30, 50, 30)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(30, 0, 30)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-30, 0, 30)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

        # Arriba
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[7])
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(30, 50, 30)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(30, 50, -30)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-30, 50, -30)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-30, 50, 30)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()


class Monton:
    def __init__(self):
        self.vertexCoords = [
            # Cara frontal
            50, 40, 50,   50, 40, -50,   50, 0, -50,   50, 0, 50,
            # Cara trasera
            -50, 40, 50,    -50, 40, -50,    -50, 0, -50,    -50, 0, 50
        ]

        self.vertexTextureCoords = [
            0.0, 0.0,   # Vértice 0
            0.0, 1.0,   # Vértice 1
            1.0, 1.0,   # Vértice 2
            1.0, 0.0,   # Vértice 3
            0.0, 0.0,   # Vértice 4
            0.0, 1.0,   # Vértice 5
            1.0, 1.0,   # Vértice 6
            1.0, 0.0    # Vértice 7
        ]
        self.elementArray = [
            0, 1, 2, 3, 0, 3, 7, 4, 0, 4, 5, 1,
            6, 2, 1, 5, 6, 5, 4, 7, 6, 7, 3, 2]

        self.vertexColors = [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def draw(self, textures, x, y, z):
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[10])

        # Atrás
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(30, 50, 60)  # X, Y, Z
        glTexCoord2f(0.0, 1.0)
        glVertex3f(30, 50, -60)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(30, 0, -60)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(30, 0, 60)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

        # Enfrente
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[10])
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-15, 50, 60)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(-15, 50, -60)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-15, 0, -60)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-15, 0, 60)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

        # Izquierda
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[11])
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(30, 50, -60)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(-15, 50, -60)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-15, 0, -60)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(30, 0, -60)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

        # Derecha
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[12])
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-15, 50, 60)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(30, 50, 60)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(30, 0, 60)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-15, 0, 60)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

        # Arriba
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[13])
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(30, 50, -60)  # X, Y, Z
        glTexCoord2f(0.0, 1.0)
        glVertex3f(30, 50, 60)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-15, 50, 60)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(-15, 50, -60)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()


class Circle:
    def __init__(self):
        self.vertexCoords = [
            # Cara frontal
            50, 40, 50,   50, 40, -50,   50, 0, -50,   50, 0, 50,
            # Cara trasera
            -50, 40, 50,    -50, 40, -50,    -50, 0, -50,    -50, 0, 50
        ]

        self.vertexTextureCoords = [
            0.0, 0.0,   # Vértice 0
            0.0, 1.0,   # Vértice 1
            1.0, 1.0,   # Vértice 2
            1.0, 0.0,   # Vértice 3
            0.0, 0.0,   # Vértice 4
            0.0, 1.0,   # Vértice 5
            1.0, 1.0,   # Vértice 6
            1.0, 0.0    # Vértice 7
        ]
        self.elementArray = [
            0, 1, 2, 3, 0, 3, 7, 4, 0, 4, 5, 1,
            6, 2, 1, 5, 6, 5, 4, 7, 6, 7, 3, 2]

        self.vertexColors = [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def draw(self, textures, x, y, z):
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[14])

        # Base
        glBegin(GL_QUADS)

        # glColor3f(0.0, 0.6, 0.0)
        ### ----- Chasis (base) -----###
        # Enfrente
        glTexCoord2f(0.0, 0.0)
        glVertex3f(30, 50, -30)  # X, Y, Z
        glTexCoord2f(0.0, 1.0)
        glVertex3f(30, 0, -30)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(30, 0, 30)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(30, 50, 30)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

        # Atrás
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[14])
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-30, 50, 30)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(-30, 50, -30)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-30, 0, -30)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-30, 0, 30)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

        # Izquierda
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[14])
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-30, 50, -30)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(-30, 0, -30)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(30, 0, -30)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(30, 50, -30)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

        # Derecha
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[14])
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-30, 0, 30)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(-30, 50, 30)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(30, 50, 30)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(30, 0, 30)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

        # Arriba
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[15])
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(30, 50, 30)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(30, 50, -30)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-30, 50, -30)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-30, 50, 30)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()


class Edificio3:
    def __init__(self):
        self.vertexCoords = [
            # Cara frontal
            50, 40, 50,   50, 40, -50,   50, 0, -50,   50, 0, 50,
            # Cara trasera
            -50, 40, 50,    -50, 40, -50,    -50, 0, -50,    -50, 0, 50
        ]

        self.vertexTextureCoords = [
            0.0, 0.0,   # Vértice 0
            0.0, 1.0,   # Vértice 1
            1.0, 1.0,   # Vértice 2
            1.0, 0.0,   # Vértice 3
            0.0, 0.0,   # Vértice 4
            0.0, 1.0,   # Vértice 5
            1.0, 1.0,   # Vértice 6
            1.0, 0.0    # Vértice 7
        ]
        self.elementArray = [
            0, 1, 2, 3, 0, 3, 7, 4, 0, 4, 5, 1,
            6, 2, 1, 5, 6, 5, 4, 7, 6, 7, 3, 2]

        self.vertexColors = [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def draw(self, textures, x, y, z):
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[16])

        # Frente
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(25, 100, -25)  # X, Y, Z
        glTexCoord2f(0.0, 1.0)
        glVertex3f(25, 0, -25)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(25, 0, 25)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(25, 100, 25)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

        # Atrás
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[16])
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-25, 0, -25)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(-25, 100, -25)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-25, 100, 25)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-25, 0, 25)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

        # Izquierda
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[16])
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(25, 0, -25)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(25, 100, -25)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-25, 100, -25)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-25, 0, -25)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

        # Derecha
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[16])
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-25, 0, 25)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(-25, 100, 25)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(25, 100, 25)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(25, 0, 25)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

        # Arriba
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[3])
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(25, 100, 25)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(25, 100, -25)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-25, 100, -25)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-25, 100, 25)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()


class Edificio4:
    def __init__(self):
        self.vertexCoords = [
            # Cara frontal
            50, 40, 50,   50, 40, -50,   50, 0, -50,   50, 0, 50,
            # Cara trasera
            -50, 40, 50,    -50, 40, -50,    -50, 0, -50,    -50, 0, 50
        ]

        self.vertexTextureCoords = [
            0.0, 0.0,   # Vértice 0
            0.0, 1.0,   # Vértice 1
            1.0, 1.0,   # Vértice 2
            1.0, 0.0,   # Vértice 3
            0.0, 0.0,   # Vértice 4
            0.0, 1.0,   # Vértice 5
            1.0, 1.0,   # Vértice 6
            1.0, 0.0    # Vértice 7
        ]
        self.elementArray = [
            0, 1, 2, 3, 0, 3, 7, 4, 0, 4, 5, 1,
            6, 2, 1, 5, 6, 5, 4, 7, 6, 7, 3, 2]

        self.vertexColors = [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def draw(self, textures, x, y, z):
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[17])

        # Base
        glBegin(GL_QUADS)

        # glColor3f(0.0, 0.6, 0.0)
        ### ----- Chasis (base) -----###
        # Enfrente
        glTexCoord2f(0.0, 0.0)
        glVertex3f(30, 50, -30)  # X, Y, Z
        glTexCoord2f(0.0, 1.0)
        glVertex3f(30, 0, -30)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(30, 0, 30)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(30, 50, 30)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

        # Atrás
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[17])
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-30, 50, 30)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(-30, 50, -30)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-30, 0, -30)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-30, 0, 30)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

        # Izquierda
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[17])
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-30, 50, -30)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(-30, 0, -30)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(30, 0, -30)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(30, 50, -30)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

        # Derecha
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[17])
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-30, 0, 30)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(-30, 50, 30)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(30, 50, 30)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(30, 0, 30)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

        # Arriba
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[5])
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(30, 50, 30)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(30, 50, -30)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-30, 50, -30)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-30, 50, 30)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()


class Banco:
    def __init__(self):
        self.vertexCoords = [
            # Cara frontal
            50, 40, 50,   50, 40, -50,   50, 0, -50,   50, 0, 50,
            # Cara trasera
            -50, 40, 50,    -50, 40, -50,    -50, 0, -50,    -50, 0, 50
        ]

        self.vertexTextureCoords = [
            0.0, 0.0,   # Vértice 0
            0.0, 1.0,   # Vértice 1
            1.0, 1.0,   # Vértice 2
            1.0, 0.0,   # Vértice 3
            0.0, 0.0,   # Vértice 4
            0.0, 1.0,   # Vértice 5
            1.0, 1.0,   # Vértice 6
            1.0, 0.0    # Vértice 7
        ]
        self.elementArray = [
            0, 1, 2, 3, 0, 3, 7, 4, 0, 4, 5, 1,
            6, 2, 1, 5, 6, 5, 4, 7, 6, 7, 3, 2]

        self.vertexColors = [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def draw(self, textures, x, y, z):
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[20])

        # Base
        glBegin(GL_QUADS)

        # glColor3f(0.0, 0.6, 0.0)
        ### ----- Chasis (base) -----###
        # Enfrente
        glTexCoord2f(0.0, 0.0)
        glVertex3f(30, 50, -40)  # X, Y, Z
        glTexCoord2f(0.0, 1.0)
        glVertex3f(30, 0, -40)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(30, 0, 40)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(30, 50, 40)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

        # Atrás
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[18])
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-30, 0, 40)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(-30, 50, 40)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-30, 50, -40)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-30, 0, -40)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

        # Izquierda
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[20])
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(30, 0, -40)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(30, 50, -40)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-30, 50, -40)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-30, 0, -40)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

        # Derecha
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[20])
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-30, 0, 30)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(-30, 50, 30)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(30, 50, 30)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(30, 0, 30)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

        # Arriba
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[19])
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(30, 50, 30)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(30, 50, -40)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-30, 50, -40)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-30, 50, 30)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()


class Edificio5:
    def __init__(self):
        self.vertexCoords = [
            # Cara frontal
            50, 40, 50,   50, 40, -50,   50, 0, -50,   50, 0, 50,
            # Cara trasera
            -50, 40, 50,    -50, 40, -50,    -50, 0, -50,    -50, 0, 50
        ]

        self.vertexTextureCoords = [
            0.0, 0.0,   # Vértice 0
            0.0, 1.0,   # Vértice 1
            1.0, 1.0,   # Vértice 2
            1.0, 0.0,   # Vértice 3
            0.0, 0.0,   # Vértice 4
            0.0, 1.0,   # Vértice 5
            1.0, 1.0,   # Vértice 6
            1.0, 0.0    # Vértice 7
        ]
        self.elementArray = [
            0, 1, 2, 3, 0, 3, 7, 4, 0, 4, 5, 1,
            6, 2, 1, 5, 6, 5, 4, 7, 6, 7, 3, 2]

        self.vertexColors = [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def draw(self, textures, x, y, z):
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[21])

        # Frente
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(25, 115, -25)  # X, Y, Z
        glTexCoord2f(0.0, 1.0)
        glVertex3f(25, 0, -25)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(25, 0, 25)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(25, 115, 25)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

        # Atrás
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[21])
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-25, 0, -25)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(-25, 115, -25)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-25, 115, 25)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-25, 0, 25)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

        # Izquierda
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[21])
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(25, 0, -25)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(25, 115, -25)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-25, 115, -25)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-25, 0, -25)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

        # Derecha
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[21])
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-25, 0, 25)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(-25, 115, 25)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(25, 115, 25)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(25, 0, 25)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

        # Arriba
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[3])
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(25, 115, 25)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(25, 115, -25)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-25, 115, -25)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-25, 115, 25)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()


class Carne:
    def __init__(self):
        self.vertexCoords = [
            # Cara frontal
            50, 40, 50,   50, 40, -50,   50, 0, -50,   50, 0, 50,
            # Cara trasera
            -50, 40, 50,    -50, 40, -50,    -50, 0, -50,    -50, 0, 50
        ]

        self.vertexTextureCoords = [
            0.0, 0.0,   # Vértice 0
            0.0, 1.0,   # Vértice 1
            1.0, 1.0,   # Vértice 2
            1.0, 0.0,   # Vértice 3
            0.0, 0.0,   # Vértice 4
            0.0, 1.0,   # Vértice 5
            1.0, 1.0,   # Vértice 6
            1.0, 0.0    # Vértice 7
        ]
        self.elementArray = [
            0, 1, 2, 3, 0, 3, 7, 4, 0, 4, 5, 1,
            6, 2, 1, 5, 6, 5, 4, 7, 6, 7, 3, 2]

        self.vertexColors = [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def draw(self, textures, x, y, z):
        glPushMatrix()
        glTranslatef(x, y, z)
        glRotatef(270, 0, 1, 0)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[23])

        # Atrás
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(30, 70, 60)  # X, Y, Z
        glTexCoord2f(0.0, 1.0)
        glVertex3f(30, 70, -60)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(30, 0, -60)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(30, 0, 60)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

        # Enfrente
        glPushMatrix()
        glTranslatef(x, y, z)
        glRotatef(270, 0, 1, 0)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[22])
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-15, 0, 60)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(-15, 70, 60)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-15, 70, -60)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-15, 0, -60)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

        # Izquierda
        glPushMatrix()
        glTranslatef(x, y, z)
        glRotatef(270, 0, 1, 0)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[23])
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(30, 70, -60)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(-15, 70, -60)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-15, 0, -60)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(30, 0, -60)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

        # Derecha
        glPushMatrix()
        glTranslatef(x, y, z)
        glRotatef(270, 0, 1, 0)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[23])
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-15, 70, 60)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(30, 70, 60)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(30, 0, 60)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-15, 0, 60)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

        # Arriba
        glPushMatrix()
        glTranslatef(x, y, z)
        glRotatef(270, 0, 1, 0)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[23])
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(30, 70, -60)  # X, Y, Z
        glTexCoord2f(0.0, 1.0)
        glVertex3f(30, 70, 60)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-15, 70, 60)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(-15, 70, -60)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()


class Edificio6:
    def __init__(self):
        self.vertexCoords = [
            # Cara frontal
            50, 40, 50,   50, 40, -50,   50, 0, -50,   50, 0, 50,
            # Cara trasera
            -50, 40, 50,    -50, 40, -50,    -50, 0, -50,    -50, 0, 50
        ]

        self.vertexTextureCoords = [
            0.0, 0.0,   # Vértice 0
            0.0, 1.0,   # Vértice 1
            1.0, 1.0,   # Vértice 2
            1.0, 0.0,   # Vértice 3
            0.0, 0.0,   # Vértice 4
            0.0, 1.0,   # Vértice 5
            1.0, 1.0,   # Vértice 6
            1.0, 0.0    # Vértice 7
        ]
        self.elementArray = [
            0, 1, 2, 3, 0, 3, 7, 4, 0, 4, 5, 1,
            6, 2, 1, 5, 6, 5, 4, 7, 6, 7, 3, 2]

        self.vertexColors = [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def draw(self, textures, x, y, z):
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[24])

        # Frente
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(25, 100, -25)  # X, Y, Z
        glTexCoord2f(0.0, 1.0)
        glVertex3f(25, 0, -25)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(25, 0, 25)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(25, 100, 25)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

        # Atrás
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[24])
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-25, 0, -25)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(-25, 100, -25)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-25, 100, 25)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-25, 0, 25)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

        # Izquierda
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[24])
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(25, 0, -25)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(25, 100, -25)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-25, 100, -25)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-25, 0, -25)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

        # Derecha
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[24])
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-25, 0, 25)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(-25, 100, 25)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(25, 100, 25)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(25, 0, 25)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

        # Arriba
        glPushMatrix()
        glTranslatef(x, y, z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textures[19])
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(25, 100, 25)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(25, 100, -25)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-25, 100, -25)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-25, 100, 25)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()
