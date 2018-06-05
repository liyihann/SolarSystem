from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

year = 0
day = 0


def draw():
    glClear(GL_COLOR_BUFFER_BIT) #清空颜色缓冲区
    glColor3f(1, 1, 1)  #重置颜色，白色
    glRotatef(1,1,1,1) #旋转参数
    glPushMatrix() #压栈

    glutWireSphere(1, 20, 16) #绘制太阳

    glRotatef(GLfloat(year),1,1,0) #沿y轴旋转
    glTranslatef(3, 0, 0) #将场景中的物体沿x轴正方向移动2个单位长
    glRotatef(GLfloat(day),0,1,0) #沿y轴旋转

    glutWireSphere(0.2,10,8) #绘制行星


    glPopMatrix() #出栈
    #glutWireTeapot(0.5)
    glutSwapBuffers()
    glFlush() #刷新窗口以显示当前绘制图形

def init():
    glClearColor(0,0,0,0)
    glShadeModel(GL_FLAT) #选择平面明暗模式或光滑明暗模式

def reshape(w,h):
    glViewport(0,0,GLsizei(w),GLsizei(h)) #设置机口
    glMatrixMode(GL_PROJECTION) #指定哪一个矩阵是当前矩阵
    glLoadIdentity()
    gluPerspective(60,float(w)/float(h),1.0,20) #创建透视投影矩阵(fovy,aspect,zNear,zFar)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 5, 5, 0, 0, 0, 0, 1, 0)

def keyboard(key,x,y):
    global day,year
    if key=='d':
        day = (day+10)%360
        glutPostRedisplay()
    elif key =='D':
        day = (day - 10 )%360
        glutPostRedisplay()
    elif key =='y':
        year = (year+5)%360
        glutPostRedisplay()
    elif key =='Y':
        year ==(year-5)%360
        glutPostRedisplay()
    else:
        return

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
glutInitWindowSize(400, 400) #窗口大小
glutInitWindowPosition(100, 100) #窗口左上角位置
glutCreateWindow("Solar System")
init() #初始化
glutDisplayFunc(draw) #执行显示
glutIdleFunc(draw)#动画效果
glutReshapeFunc(reshape)
#glutKeyboardFunc(keyboard)
glutMainLoop() #进入glut事件处理循环
