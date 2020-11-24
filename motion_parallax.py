import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
import random

window = 0
width, height = 500, 500  # window size

c1 = random.randint(0,10)
c2 = random.randint(0,10)
c3 = random.randint(0,10)
c4 = random.randint(0,10)
color1 = c1/10
color2 = c2/10
color3 = c3/10
color4 = c4/10

def drawSquare(x, y, width, height):
    glBegin(GL_QUADS)  # start drawing a square
    glVertex2f(x, y)  # bottom left point
    glVertex2f(x + width, y)  # bottom right point
    glVertex2f(x + width, y + height)  # top right point
    glVertex2f(x, y + height)  # top left point
    glEnd()  # done drawing

def drawTriangleL(x, y, width, height):
    glBegin(GL_TRIANGLES)
    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glEnd()

def drawTriangleR(x, y, width, height):
    glBegin(GL_TRIANGLES)
    glVertex2f(x, y)
    glVertex2f(x, y + height )
    glVertex2f(x + width, y)
    glEnd()

def drawBirds(x,y, width, height):
    glBegin(GL_LINES)
    glVertex2f(x+width,y+height)
    glVertex2f(x,y)
    glEnd()


def drawSphereish(posx, posy, sides, radius):
    glBegin(GL_POLYGON)
    for i in range(100):
        cosine = radius * cos(i * 2 * pi / sides) + posx
        sine = radius * sin(i * 2 * pi / sides) + posy
        glVertex2f(cosine, sine)
    glEnd()

def drawScene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # clear the screen
    glLoadIdentity()  # reset position
    refresh2d(width, height)

	# background
    glColor3f(0, 0, 1.0)  # set color to blue
    drawSquare(0, 0, 500, 500)

	#layer 1

    glColor3f(1.0, 1.0, 0.0)  # sun color yellow
    drawSphereish(375, 425, 16, 25)


	#layer 2

    glColor3f(color1, color2, color3)        # tallest mountain in back
    drawTriangleL(50, 0, 250, 350)
    drawTriangleR(300, 0, 250, 350)


	#layer 3

    glColor3f(color2, color3, color4)        # left mountain
    drawTriangleL(25, 0, 200, 300)
    drawTriangleR(225, 0, 200, 300)

    glColor3f(color3, color4, color1)  # right mountain
    drawTriangleL(200, 0, 200, 300)
    drawTriangleR(400, 0, 200, 300)

    glColor3f(color4, color1, color2)  # extra front mountain
    drawTriangleL(100, 0, 100, 250)
    drawTriangleR(200, 0, 100, 250)

    glColor3f(0.0, 0.75, 0.0)  # set color to green
    drawSquare(0,0 , 500, 150)

	#layer 4                               #grass loop
    x = 0
    i = 0
    while (x < 160):
        x += 1
        i += 5
        glColor3f(0.0, 1.0, 0.0)
        drawSquare(i, 150, 2, 8)


    glColor3f(0.4, 0.0, 0.0)  # set color to brown
    drawSquare(50, 100, 20, 75)  # draw the trunk
    glColor3f(0.0, 0.5, 0.0)  # set color to green
    drawSphereish(60, 200, 35, 45)  # draw the leaves

    glutSwapBuffers()  # important for double buffering

def drawParallax(Mx, My):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # clear the screen
    glLoadIdentity()  # reset position
    refresh2d(width, height)

    foreX = (Mx-250)* 0.5
    foreY = (My-250)* 0.5
    fMX = (Mx-250)* 0.25
    fMY = (My-250)* 0.25
    mMX = (Mx-250)* 0.15
    mMY = (My-250)* 0.15
    rMX = (Mx-250)* 0.05
    rMY = (My-250)* 0.05
    sX = (Mx-250)* 0.02
    sY = (My-250)* 0.02
     
    
	# background
    glColor3f(0, 0, 1.0)  # set color to blue
    drawSquare(0, 0, 500, 500)

	#layer 1

    glColor3f(1.0, 1.0, 0.0)  # sun color yellow
    drawSphereish(375+sX, 425+sY, 16, 25)


	#layer 2

    glColor3f(color1, color2, color3)        # tallest mountain in back
    drawTriangleL(50+rMX, rMY, 250, 350)
    drawTriangleR(300+rMX, rMY, 250, 350)


	#layer 3

    glColor3f(color2, color3, color4)        # left mountain
    drawTriangleL(mMX+25, mMY, 200, 300)
    drawTriangleR(mMX+225, mMY, 200, 300)

    glColor3f(color3, color4, color1)  # right mountain
    drawTriangleL(mMX+200, mMY, 200, 300)
    drawTriangleR(mMX+400, mMY, 200, 300)

    glColor3f(color4, color1, color2)  # extra front mountain
    drawTriangleL(fMX+100, fMY, 100, 250)
    drawTriangleR(fMX+200, fMY, 100, 250)
    
    glColor3f(0.0, 0.75, 0.0)  # set color to green
    drawSquare(0, 0, 500, 150+foreY)

	#layer 4                               #grass loop
    x = 0
    i = -10
    while (x < 140):
        x += 1
        i += 5
        glColor3f(0.0, 0.75, 0.0)
        drawSquare(i+foreX, 150+foreY, 2, 8)

        

    glColor3f(0.4, 0.0, 0.0)  # set color to brown
    drawSquare(50+foreX, 100+foreY, 20, 75)  # draw the trunk
    glColor3f(0.0, 0.5, 0.0)  # set color to green
    drawSphereish(60+foreX, 200+foreY, 35, 45)  # draw the leaves

    glutSwapBuffers()  # important for double buffering

def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

# initialization
glutInit()  # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH | GLUT_DOUBLE)
glutInitWindowSize(width, height)  # set window size
glutInitWindowPosition(0, 0)  # set window position
wind = glutCreateWindow("CSC 322 Fall 2020 Final Project")  # create window with title
glutDisplayFunc(drawScene)  # set showScreen function callback
glutIdleFunc(drawScene)  # draw all the time
glutPassiveMotionFunc(drawParallax);
glutMainLoop()  # start everything