from OpenGL.GL import *
from OpenGL.GLU import *


def render(obj, pos=[0,0,0], rot=[0,0,0]):
    glPushMatrix()
    glTranslate(pos[0], pos[1], pos[2])
    glRotate(rot[1], 1, 0, 0)
    glRotate(rot[0], 0, 1, 0)
    glRotate(rot[2], 0, 0, 1)
    glCallList(obj.gl_list)
    glPopMatrix()