from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import random
from PIL import Image

day = 0
mercuryYear=0
venusYear=0
year=0
marsYear=0
jupiterYear=0
saturnYear=0
uranusYear=0
neptuneYear=0
g_text=gluNewQuadric()
star = [[0 for i in range(3)] for i in range(2000)]

light_angle = 0.0
light_radius = 8.0
cam_radius = 7.0
cam_radius1=0.0
cam_position=[0 for i in range(3)]
cam_angle_u = 0.3
cam_angle_v = 0.3
state = 1

def init():
    global g_text,sun_texture,mercury_texture,venus_texture,earth_texture,mars_texture,jupiter_texture,saturn_texture,uranus_texture,neptune_texture
    glClearColor(0.0,0.0,0.0,0.0)
    lPosition()
    glShadeModel(GL_SMOOTH)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_TEXTURE_2D)
    g_text=gluNewQuadric()
    sun_texture = load_texture("./texture/sun.bmp")
    mercury_texture = load_texture("./texture/mercury.bmp")
    venus_texture = load_texture("./texture/venus.jpg")
    earth_texture = load_texture("./texture/earth.jpg")
    mars_texture = load_texture("./texture/mars.jpg")
    jupiter_texture = load_texture("./texture/jupiter.bmp")
    saturn_texture = load_texture("./texture/saturn.jpg")
    uranus_texture = load_texture("./texture/uranus.jpg")
    neptune_texture = load_texture("./texture/neptune.jpg")

def init_stars():
    for i in range(0,2000):
        for j in range(0,3):
            star[i][j] = random.random()% 20 - 10

def load_texture(filename):
    image = Image.open(filename)
    ix = image.size[0]
    iy = image.size[1]

    image = image.tobytes("raw", "RGBX", 0, -1)
    # Create Texture
    texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture)  # 2d texture (x and y size)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)

    glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
    # set the texture's minification properties (mapping textures to bigger areas)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    # set the texture's stretching properties (mapping textures to smaller areas)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)
    return texture


def stars():

    glBegin(GL_POINTS)
    glColor3f(1.0,1.0,1.0)
    for i in range(0,2000):
        glVertex3f(star[i][0], star[i][1], star[i][2])
    glEnd()


def drawSun():
    glPushMatrix()
    glBindTexture(GL_TEXTURE_2D,sun_texture)
    gluSphere(g_text,0.6,32,32)
    glPopMatrix()

def drawMercury():
    glPushMatrix()
    glBindTexture(GL_TEXTURE_2D, mercury_texture)
    glRotatef (float(mercuryYear), 0.0, 0.0, 1.0)
    glTranslatef (0.8, 0.0, 0.0)
    glRotatef (float(day), 0.0, 0.0, 1.0)
    gluSphere(g_text,0.13, 20, 16) #draw smaller planet
    glPopMatrix()

def drawVenus():
    glPushMatrix()
    glBindTexture(GL_TEXTURE_2D, venus_texture)
    glRotatef (GLfloat(venusYear), 0.0, 0.0, 1.0)
    glTranslatef (1.3, 0.0, 0.0)
    glRotatef (float(day), 0.0, 0.0, 1.0)
    gluSphere(g_text,0.2, 20, 16) #draw smaller planet
    glPopMatrix()

def drawEarth():
    glPushMatrix()
    glBindTexture(GL_TEXTURE_2D, earth_texture)
    glRotatef (GLfloat(year), 0.0, 0.0, 1.0)
    glTranslatef (1.8, 0.0, 0.0)
    glRotatef (GLfloat(day), 0.0, 0.0, 1.0)
    gluSphere(g_text,0.16, 20, 16) #draw smaller planet
    glPopMatrix()

def drawMars():
    glPushMatrix()
    glBindTexture(GL_TEXTURE_2D, mars_texture)
    glRotatef (GLfloat(marsYear), 0.0, 0.0, 1.0)
    glTranslatef (2.2, 0.0, 0.0)
    glRotatef (GLfloat(day), 0.0, 0.0, 1.0)
    gluSphere(g_text,0.14, 20, 16) #draw smaller planet
    glPopMatrix()

def drawJupiter():
    glPushMatrix()
    glBindTexture(GL_TEXTURE_2D, mars_texture)
    glRotatef (GLfloat(jupiterYear), 0.0, 0.0, 1.0)
    glTranslatef (2.7, 0.0, 0.0)
    glRotatef (GLfloat(day), 0.0, 0.0, 1.0)
    gluSphere(g_text,0.22, 20, 16) #draw smaller planet
    glPopMatrix()

def park():
    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0,0,0)
    for i in range(0,380,20):
        p=float(i*3.14/180)
        glVertex3f(float(math.sin(p) * 0.22), float(math.cos(p) * 0.22), 0.0)
    glEnd()

def drawSaturn():
    glPushMatrix()
    glBindTexture(GL_TEXTURE_2D, saturn_texture)
    glRotatef (GLfloat(saturnYear), 0.0, 0.0, 1.0)

    glTranslatef (3.15, 0.0, 0.0)
    glRotatef (GLfloat(day), 0.0, 0.0, 1.0)
    gluSphere(g_text,0.14, 20, 16) #draw smaller planet
    glRotatef(0.2, 1.0, 0.0, 0.0)
    park()
    glPopMatrix()

def drawUranus():
    glPushMatrix()
    glBindTexture(GL_TEXTURE_2D, uranus_texture)
    glRotatef (GLfloat(uranusYear), 0.0, 0.0, 1.0)
    glTranslatef (3.55, 0.0, 0.0)
    glRotatef (GLfloat(day), 0.0, 0.0, 1.0)
    gluSphere(g_text,0.12, 20, 16) #draw smaller planet
    glPopMatrix()

def drawNeptune():
    glPushMatrix()
    glBindTexture(GL_TEXTURE_2D, neptune_texture)
    glRotatef (GLfloat(jupiterYear), 0.0, 0.0, 1.0)
    glTranslatef (3.8, 0.0, 0.0)
    glRotatef (GLfloat(day), 0.0, 0.0, 1.0)
    gluSphere(g_text,0.10, 20, 16) #draw smaller planet
    glPopMatrix()

def rotate():
    global day, mercuryYear, venusYear, year, marsYear, jupiterYear, saturnYear, uranusYear, neptuneYear
    mercuryYear+=6
    if mercuryYear>=360:
        mercuryYear-=360
    venusYear+=3
    if venusYear>=360:
        venusYear-=360
    year+=2
    if year>=360:
        year-=360
    marsYear+=1
    if marsYear>=360:
        marsYear-=360
    jupiterYear+=0.25
    if jupiterYear>=360:
        jupiterYear-=360
    saturnYear+=0.2
    if saturnYear>=360:
        saturnYear-=360
    uranusYear+=0.05
    if uranusYear>=360:
        uranusYear-=360
    neptuneYear+=0.05
    if neptuneYear>=360:
        neptuneYear-=360
    glutPostRedisplay()


def lPosition():
    y= light_radius * math.cos(light_angle)
    z=light_radius*math.sin(light_angle)
    light_position=[3.0,y,z,0.0]
    glLightfv(GL_LIGHT0,GL_POSITION,light_position)

def draw():
    lPosition()
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glColor3f(1.0,1.0,1.0)
    #glRotatef(1,1,1,1)
    glTexGeni(GL_S,GL_TEXTURE_GEN_MODE,GL_OBJECT_LINEAR)
    glTexGeni(GL_T,GL_TEXTURE_GEN_MODE,GL_OBJECT_LINEAR)
    glEnable(GL_TEXTURE_GEN_S)
    glEnable(GL_TEXTURE_GEN_T)
    glEnable(GL_TEXTURE_2D)
    stars()
    stars()
    drawSun()
    drawMercury()
    drawVenus()
    drawEarth()
    drawMars()
    drawJupiter()
    drawSaturn()
    drawUranus()
    drawNeptune()
    rotate()
    glDisable(GL_TEXTURE_2D)
    glutSwapBuffers()
    glFlush()

def cPosition():
    cam_radius1 = cam_radius*math.cos(cam_angle_v)
    cam_position[0] = cam_radius1*math.cos(cam_angle_u)
    cam_position[1] = cam_radius1*math.sin(cam_angle_u)
    cam_position[2] = cam_radius*math.sin(cam_angle_v)
    glLoadIdentity()
    gluLookAt(cam_position[0],cam_position[1],cam_position[2], 0.0, 0.0, 0.0, 0.0, 0.0, 1.0)

def reshape(w,h):
    glViewport(0,0,GLsizei(w),GLsizei(h))
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, float(w) / float(h), 1.0, 20)
    glMatrixMode(GL_MODELVIEW)
    cPosition()



def myidle():
    global day
    day+=5
    if day>=360:
        day=day-360
    glutPostRedisplay()


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(800,600)
glutInitWindowPosition(100, 100)
glutCreateWindow("Solar System")
init()
init_stars()
glutDisplayFunc(draw) #执行显示
glutReshapeFunc(reshape)
glutIdleFunc(myidle)#动画效果
glutMainLoop() #进入glut事件处理循环