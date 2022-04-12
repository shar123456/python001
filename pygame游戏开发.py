#安装 pip install pygame

import pygame
import sys
import time
from pygame.locals import * #检测事件

#创建窗口
screen=pygame.display.set_mode((400,300))
#读取图片
img1=pygame.image.load(r"./images/game.jpg")
img2=pygame.image.load(r"./images/F.png")

while 1==1:
    a=0#x轴位置
    b=50#y轴位置
    for x in range(30):
        #在窗口中加入对象
        screen.blit(img1,(0,0))
        screen.blit(img2,(a,b))
        #刷新窗口，显示所有对象
        pygame.display.update()
        if x<=15:
            a+=10  #向右移动10个像素
        else:
            a-=10 #向左移动10个像素
        time.sleep(0.1)

        #检测用户退出
        for event in pygame.event.get():
            if event.type==QUIT:
                print("退出")
                sys.exit(0)