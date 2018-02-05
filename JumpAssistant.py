#coding=utf8
import os
import PIL,numpy
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

IsUpdate=True
image=""

def getScreenFromMobile(): #从手机屏幕获取截屏图片
    os.system('adb shell screencap -p /sdcard/sreen.png')
    os.system('adb pull /sdcard/sreen.png')
    return numpy.array(PIL.Image.open('sreen.png'))

def jumpToNext(position1,position2): #跳到下一张图
    x1,y1=position1
    x2,y2=position2
    distance=((x2-x1)**2+(y2-y1)**2)**0.5
    os.system('adb shell input swipe %d %d %d %d %d' % (x2,y2,x2,y2,int(distance * 2.0)))
    #os.system('adb shell input swipe 0 0 0 0 {}'.format(int(distance*2.0)))  点击位置不变会被测出来时

def callback(event,coor=[]): #点击图片回调函数
    global IsUpdate
    coor.append((event.xdata,event.ydata))
    if len(coor)==2:
        jumpToNext(coor.pop(),coor.pop())
        IsUpdate=True

def updateScreen(frame): #更新截屏图片
    global IsUpdate,image
    if IsUpdate:
        time.sleep(1)
        image.set_array(getScreenFromMobile())
        IsUpdate=False
    return image,

def simulationMobile():  #实时同步手机
    global image
    figure=plt.figure()
    image=plt.imshow(getScreenFromMobile(),animated=True)
    figure.canvas.mpl_connect('button_press_event',callback)
    fa=FuncAnimation(figure,updateScreen,interval=50,blit=True) #直接运行函数不行，必须实例化
    plt.show()

if __name__=='__main__':
    os.system('adb connect 192.168.1.107:5555')#connect mobile
    simulationMobile()

