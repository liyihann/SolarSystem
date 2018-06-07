from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import random
from PIL import Image

wide=800
height=600
size=10
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
BUFSIZE = 512
selectBuff = (GLuint * BUFSIZE)()

isSelected=[False for x in range(9)]

def init():
    global g_text, sun_texture, mercury_texture, venus_texture, earth_texture, mars_texture, jupiter_texture, saturn_texture, uranus_texture, neptune_texture,background_texture
    global suninfo,mercuryinfo,venusinfo,earthinfo,marsinfo,jupiterinfo,saturninfo,uranusinfo,neptuneinfo
    glClearColor(0.0, 0.0, 0.0, 0.0)
    lPosition()
    glShadeModel(GL_SMOOTH)
    # glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_TEXTURE_2D)
    g_text = gluNewQuadric()
    sun_texture = load_texture("./texture/sun.bmp")
    mercury_texture = load_texture("./texture/mercury.bmp")
    venus_texture = load_texture("./texture/venus.jpg")
    earth_texture = load_texture("./texture/earth.jpg")
    mars_texture = load_texture("./texture/mars.jpg")
    jupiter_texture = load_texture("./texture/jupiter.bmp")
    saturn_texture =load_texture("./texture/saturn.jpg")
    uranus_texture = load_texture("./texture/uranus.jpg")
    neptune_texture = load_texture("./texture/neptune.jpg")
    # background_texture = load_texture("./texture/background.jpg")
    suninfo = load_texture("./information/suninfo.jpg")
    mercuryinfo = load_texture("./information/mercuryinfo.jpg")
    venusinfo = load_texture("./information/venusinfo.jpg")
    earthinfo = load_texture("./information/earthinfo.jpg")
    marsinfo = load_texture("./information/marsinfo.jpg")
    jupiterinfo = load_texture("./information/jupiterinfo.jpg")
    saturninfo = load_texture("./information/saturninfo.jpg")
    uranusinfo = load_texture("./information/uranusinfo.jpg")
    neptuneinfo = load_texture("./information/neptuneinfo.jpg")
    ''' init_stars  '''
    for i in range(0,2000):
        for j in range(0,3):
            star[i][j] = random.random()% 20 - 10

def reshape( w, h):
    glViewport(0, 0, GLsizei(w), GLsizei(h))
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, float(w) / float(h), 1.0, 20)
    glMatrixMode(GL_MODELVIEW)
    cPosition()

def draw():
    lPosition()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    # glRotatef(1,1,1,1)
    glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_OBJECT_LINEAR)
    glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_OBJECT_LINEAR)
    glEnable(GL_TEXTURE_GEN_S)
    glEnable(GL_TEXTURE_GEN_T)
    glEnable(GL_TEXTURE_2D)
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    # drawBackground()
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
    if isSelected[0]:
        glPushMatrix()
        glLoadIdentity()
        glBindTexture(GL_TEXTURE_2D, suninfo)
        glTranslatef(-2.8, 1.5, 0)
        gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
        glRectf(0, 0,1, 1)
        glPopMatrix()
    if isSelected[1]:
        glPushMatrix()
        glLoadIdentity()
        glBindTexture(GL_TEXTURE_2D, mercuryinfo)
        glTranslatef(-2.8, 1.5, 0)
        gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
        glRectf(0, 0,1, 1)
        glPopMatrix()
    if isSelected[2]:
        glPushMatrix()
        glLoadIdentity()
        glBindTexture(GL_TEXTURE_2D, venusinfo)
        glTranslatef(-2.8, 1.5, 0)
        gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
        glRectf(0, 0,1, 1)
        glPopMatrix()
    if isSelected[3]:
        glPushMatrix()
        glLoadIdentity()
        glBindTexture(GL_TEXTURE_2D, earthinfo)
        glTranslatef(-2.8, 1.5, 0)
        gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
        glRectf(0, 0,1, 1)
        glPopMatrix()
    if isSelected[4]:
        glPushMatrix()
        glLoadIdentity()
        glBindTexture(GL_TEXTURE_2D, marsinfo)
        glTranslatef(-2.8, 1.5, 0)
        gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
        glRectf(0, 0,1, 1)
        glPopMatrix()
    if isSelected[5]:
        glPushMatrix()
        glLoadIdentity()
        glBindTexture(GL_TEXTURE_2D, jupiterinfo)
        glTranslatef(-2.8, 1.5, 0)
        gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
        glRectf(0, 0,1, 1)
        glPopMatrix()
    if isSelected[6]:
        glPushMatrix()
        glLoadIdentity()
        glBindTexture(GL_TEXTURE_2D, saturninfo)
        glTranslatef(-2.8, 1.5, 0)
        gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
        glRectf(0, 0,1, 1)
        glPopMatrix()
    if isSelected[7]:
        glPushMatrix()
        glLoadIdentity()
        glBindTexture(GL_TEXTURE_2D, uranusinfo)
        glTranslatef(-2.8, 1.5, 0)
        gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
        glRectf(0, 0,1, 1)
        glPopMatrix()
    if isSelected[8]:
        glPushMatrix()
        glLoadIdentity()
        glBindTexture(GL_TEXTURE_2D, neptuneinfo)
        glTranslatef(-2.8, 1.5, 0)
        gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
        glRectf(0, 0,1, 1)
        glPopMatrix()
    glPopMatrix()
    glDisable(GL_TEXTURE_2D)

    glutSwapBuffers()
    glFlush()


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
    # glLoadName(1)
    glPushMatrix()
    glPushName(1)
    glBindTexture(GL_TEXTURE_2D,sun_texture)
    gluSphere(g_text,0.6,32,32)
    glPopName()
    glPopMatrix()

def drawMercury():
    # glLoadName(2)
    glPushMatrix()
    glPushName(2)
    glBindTexture(GL_TEXTURE_2D, mercury_texture)
    glRotatef (float(mercuryYear), 0.0, 0.0, 1.0)
    glTranslatef (0.8, 0.0, 0.0)
    glRotatef (float(day), 0.0, 0.0, 1.0)
    gluSphere(g_text,0.13, 20, 16) #draw smaller planet
    glPopName()
    glPopMatrix()
    drawOrbit(0.8)

def drawVenus():
    # glLoadName(3)
    glPushMatrix()
    glPushName(3)
    glBindTexture(GL_TEXTURE_2D, venus_texture)
    glRotatef (GLfloat(venusYear), 0.0, 0.0, 1.0)
    glTranslatef (1.3, 0.0, 0.0)
    glRotatef (float(day), 0.0, 0.0, 1.0)
    gluSphere(g_text,0.2, 20, 16) #draw smaller planet
    glPopName()
    glPopMatrix()
    drawOrbit(1.3)

def drawEarth():
    # glLoadName(4)
    glPushMatrix()
    glPushName(4)
    glBindTexture(GL_TEXTURE_2D, earth_texture)
    glRotatef (GLfloat(year), 0.0, 0.0, 1.0)
    glTranslatef (1.8, 0.0, 0.0)
    glRotatef (GLfloat(day), 0.0, 0.0, 1.0)
    gluSphere(g_text,0.16, 20, 16) #draw smaller planet
    glPopName()
    glPopMatrix()
    drawOrbit(1.8)

def drawMars():
    # glLoadName(5)
    glPushMatrix()
    glPushName(5)
    glBindTexture(GL_TEXTURE_2D, mars_texture)
    glRotatef (GLfloat(marsYear), 0.0, 0.0, 1.0)
    glTranslatef (2.2, 0.0, 0.0)
    glRotatef (GLfloat(day), 0.0, 0.0, 1.0)
    gluSphere(g_text,0.14, 20, 16) #draw smaller planet
    glPopName()
    glPopMatrix()
    drawOrbit(2.2)

def drawJupiter():
    # glLoadName(6)
    glPushMatrix()
    glPushName(6)
    glBindTexture(GL_TEXTURE_2D, mars_texture)
    glRotatef (GLfloat(jupiterYear), 0.0, 0.0, 1.0)
    glTranslatef (2.7, 0.0, 0.0)
    glRotatef (GLfloat(day), 0.0, 0.0, 1.0)
    gluSphere(g_text,0.22, 20, 16) #draw smaller planet
    glPopName()
    glPopMatrix()
    drawOrbit(2.7)

def park():
    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0,0,0)
    for i in range(0,380,20):
        p=float(i*3.14/180)
        glVertex3f(float(math.sin(p) * 0.22), float(math.cos(p) * 0.22), 0.0)
    glEnd()

def drawSaturn():
    # glLoadName(7)
    glPushMatrix()
    glPushName(7)
    glBindTexture(GL_TEXTURE_2D, saturn_texture)
    glRotatef (GLfloat(saturnYear), 0.0, 0.0, 1.0)
    glTranslatef (3.15, 0.0, 0.0)
    glRotatef (GLfloat(day), 0.0, 0.0, 1.0)
    gluSphere(g_text,0.14, 20, 16) #draw smaller planet
    glRotatef(0.2, 1.0, 0.0, 0.0)
    park()
    glPopName()
    glPopMatrix()
    drawOrbit(3.15)

def drawUranus():
    # glLoadName(8)
    glPushMatrix()
    glPushName(8)
    glBindTexture(GL_TEXTURE_2D, uranus_texture)
    glRotatef (GLfloat(uranusYear), 0.0, 0.0, 1.0)
    glTranslatef (3.55, 0.0, 0.0)
    glRotatef (GLfloat(day), 0.0, 0.0, 1.0)
    gluSphere(g_text,0.12, 20, 16) #draw smaller planet
    glPopName()
    glPopMatrix()
    drawOrbit(3.55)

def drawNeptune():
    # glLoadName(9)
    glPushMatrix()
    glPushName(9)
    glBindTexture(GL_TEXTURE_2D, neptune_texture)
    glRotatef (GLfloat(jupiterYear), 0.0, 0.0, 1.0)
    glTranslatef (3.8, 0.0, 0.0)
    glRotatef (GLfloat(day), 0.0, 0.0, 1.0)
    gluSphere(g_text,0.10, 20, 16) #draw smaller planet
    glPopName()
    glPopMatrix()
    drawOrbit(3.8)

def rotate():
    global day, mercuryYear, venusYear, year, marsYear, jupiterYear, saturnYear, uranusYear, neptuneYear
    mercuryYear+=3
    if mercuryYear>=360:
        mercuryYear-=360
    venusYear+=2
    if venusYear>=360:
        venusYear-=360
    year+=0.8
    if year>=360:
        year-=360
    marsYear+=0.8
    if marsYear>=360:
        marsYear-=360
    jupiterYear+=0.3
    if jupiterYear>=360:
        jupiterYear-=360
    saturnYear+=0.2
    if saturnYear>=360:
        saturnYear-=360
    uranusYear+=0.05
    if uranusYear>=360:
        uranusYear-=360
    neptuneYear+=0.01
    if neptuneYear>=360:
        neptuneYear-=360
    glutPostRedisplay()

def drawOrbit(radius):
    # glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_LINE_STRIP)
    for i in range(100):
        glVertex2f(radius * math.cos(2 * math.pi / 100 * i), radius * math.sin(2 * math.pi / 100 * i))
    glEnd()

def lPosition():
    y= light_radius * math.cos(light_angle)
    z=light_radius*math.sin(light_angle)
    light_position=[3.0,y,z,0.0]
    glLightfv(GL_LIGHT0,GL_POSITION,light_position)

def cPosition():
    cam_radius1 = cam_radius*math.cos(cam_angle_v)
    cam_position[0] = cam_radius1*math.cos(cam_angle_u)
    cam_position[1] = cam_radius1*math.sin(cam_angle_u)
    cam_position[2] = cam_radius*math.sin(cam_angle_v)
    glLoadIdentity()
    gluLookAt(cam_position[0],cam_position[1],cam_position[2], 0.0, 0.0, 0.0, 0.0, 0.0, 1.0)

def select(button,state,x,y):

    if button != GLUT_LEFT_BUTTON or state != GLUT_DOWN:
        return
    viewport = (GLint * 4)()
    glSelectBuffer(BUFSIZE, selectBuff)
    glGetIntegerv(GL_VIEWPORT, viewport)
    glMatrixMode(GL_PROJECTION)
    glInitNames()
    glPushMatrix()
    glRenderMode(GL_SELECT)
    glLoadIdentity()
    gluPickMatrix(x,viewport[3]-y+viewport[1],10,10,viewport)
    gluPerspective(60.0, float(wide) / float(height), 1.0, 10)

    glMatrixMode(GL_MODELVIEW)
    draw()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)

    hits = glRenderMode(GL_RENDER)
    if hits:
        process(selectBuff[3])
    else:
        print("Please click on the sun or planets!")
        for i in range(len(isSelected)):
            isSelected[i] = False
    glutPostRedisplay()

def process(id):
    muteOthers(id)
    if id == 1:
        print ("You clicked on the Sun!")
    elif id == 2:
        print ("You clicked on Mercury!")
    elif id == 3:
        print ("You clicked on Venus!")

    elif id == 4:
        print ("You clicked on Earth!")

    elif id == 5:
        print ("You clicked on Mars!")

    elif id == 6:
        print ("You clicked on Jupiter!")

    elif id == 7:
        print ("You clicked on Saturn!")

    elif id == 8:
        print ("You clicked on Uranus!")

    elif id == 9:
        print ("You clicked on Neptune!")
    else:
        print ("Nothing was clicked on!")

def muteOthers(id):
    global isSelected
    for i in range(len(isSelected)):
        isSelected[i]=False
    isSelected[id - 1] = True

def myidle():
    global day
    day+=2
    if day>=360:
        day=day-360
    glutPostRedisplay()


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(wide,height)
glutInitWindowPosition(100, 100)
mainWin = glutCreateWindow("Solar System")
init()
glutDisplayFunc(draw) #执行显示
glutReshapeFunc(reshape)
glutIdleFunc(myidle)
glutMouseFunc(select)
glutMainLoop() #进入glut事件处理循环

