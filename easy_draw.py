#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Michael Yu'
import numpy as np
import cv2
from matplotlib import pyplot as plt
def draw_line():
    img = np.zeros((512,512,3),np.uint8)
    #生成一个空彩色图像
    """
    img = np.zeros((512,512),np.uint8)#生成一个空灰度图像
    """
    cv2.line(img,(0,0),(511,511),(255,0,0),5)
    """
    函数为：cv2.line（img,Point pt1,Point pt2,color,thickness=1,line_type=8 shift=0）
    有值的代表有默认值，不用给也行。可以看到这个函数主要接受参数为两个点的坐标，
    线的颜色（彩色图像的话颜色就是一个1*3的数组）
    """
    plt.imshow(img,"gray")
    plt.show()

def draw_rectangle():
    img = np.zeros((512,512,3),np.uint8)
    cv2.rectangle(img,(100,100),(400,400),(0,255,0),1)
    plt.imshow(img,"gray")
    plt.show()


def draw_circle():
    img = np.zeros((512,512,3),np.uint8)
    cv2.circle(img,(250,250),100,(255,0,0),5)
    """
    坐标和半径
    """
    plt.imshow(img,"gray")
    plt.show()

def draw_ellipse():
    img = np.zeros((512,512,3),np.uint8)
    cv2.ellipse(img,(250,250),(100,50),0,0,180,255,-1)
    """
    椭圆：中心点 长轴 短轴
    """
    plt.imshow(img,"gray")
    plt.show()

def draw_reshape():
    img = np.zeros((512,512,3),np.uint8)
    pts = np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
    pts = pts.reshape((-1,1,2))
    """
    多边形
    """
    plt.imshow(img,"gray")
    plt.show()

def draw_font():
    name = "heloo"
    img = np.zeros((512,512,3),np.uint8)
    font = cv2.FONT_HERSHEY_SIMPLEX
    print name
    cv2.putText(img,name,(10,500),font,4,(255,255,255),2)
    """
    写文字，中文问题没有很好的解决
    """
    plt.imshow(img,"gray")
    plt.show()

if __name__ == "__main__":
    draw_font()
