# botao esquerdo: girar objeto
# botao direito: mover objeto
# scroll: zoom
import sys, pygame
from pygame.locals import *
from pygame.constants import *
from OpenGL.GL import *
from OpenGL.GLU import *
# modulo para carregar obj
from objloader import *
from util import *

pygame.init()
viewport = (800,600)
hx = viewport[0]/2
hy = viewport[1]/2
srf = pygame.display.set_mode(viewport, OPENGL | DOUBLEBUF)

glLightfv(GL_LIGHT0, GL_POSITION,  (-40, 200, 100, 0.0))
glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.5, 1.0))
glEnable(GL_LIGHT0)
glEnable(GL_LIGHTING)
glEnable(GL_COLOR_MATERIAL)
glEnable(GL_DEPTH_TEST)
glShadeModel(GL_SMOOTH) # shader

# carrega o obj
walls  = OBJ("walls.obj", swapyz=True)
couch  = OBJ("couch.obj", swapyz=True)
table  = OBJ("table.obj", swapyz=True)
scream = OBJ("ogrito.obj",swapyz=True)
carpet = OBJ("carpet.obj",swapyz=True)

clock = pygame.time.Clock()

glMatrixMode(GL_PROJECTION)
glLoadIdentity()
width, height = viewport
gluPerspective(70.0, width/float(height), 1, 100.0)
glEnable(GL_DEPTH_TEST)
glMatrixMode(GL_MODELVIEW)

rx, ry = (0,0)
tx, ty = (0,0)
zpos = 5
rotate = move = False
while 1:
    clock.tick(30)
    for e in pygame.event.get():
        if e.type == QUIT:
            sys.exit()
        elif e.type == KEYDOWN and e.key == K_ESCAPE:
            sys.exit()
        elif e.type == MOUSEBUTTONDOWN:
            if e.button == 4: zpos = max(1, zpos-1)
            elif e.button == 5: zpos += 1
            elif e.button == 1: rotate = True
            elif e.button == 3: move = True
        elif e.type == MOUSEBUTTONUP:
            if e.button == 1: rotate = False
            elif e.button == 3: move = False
        elif e.type == MOUSEMOTION:
            i, j = e.rel
            if rotate:
                rx += i
                ry += j
            if move:
                tx += i
                ty -= j

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # renderizar objetos ================
    glPushMatrix()
    glTranslate(tx/20., ty/20., - zpos)
    glRotate(ry, 1, 0, 0)
    glRotate(rx, 0, 1, 0)

    # ============ sala ===================
    render(walls)
    render(couch)
    render(table , pos=[3.3,0,-2.5], rot=[0,90,0], scale=[.7,.7,.7])
    render(scream, pos=[3,3.5,-6.7], scale=[.8,.8,1])
    render(carpet, pos=[-.3,0,1], scale=[1.3, 1 ,1.3])
    # ======================================

    # ============
    # demais objetos aqui
    # ============

    glPopMatrix()
    # ==================================

    pygame.display.set_caption('projeto - CG')
    pygame.display.flip()