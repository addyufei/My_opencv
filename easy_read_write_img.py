#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Michael Yu'
import cv2
import numpy as np
img = cv2.imread("E:\Raspberry_upload\image55.jpg",0)
'''
使用什么样的方式读入图片
cv2.IMREAD_COLOR == 2
cv2.IMREAD_GRAYSCALE == 0
cv2.IMREAD_UNCHANGED == -1
'''

cv2.namedWindow("image",cv2.WINDOW_NORMAL)

'''
namedWindow函数用于调整显示窗口的大小
cv2.WINDOW_NORMAL，窗口可以手动调整大小
cv2.WINDOW_AUTOSIZE，自动调整大小
'''

cv2.imshow("image",img)
key_value = cv2.waitKey(0)&0xFF
#64位系统需要增加&0xFF

if key_value == 27:
    cv2.destroyAllWindows()
elif key_value == ord('s'):
    cv2.imwrite("yufei.png",img)
    #好像只支持png格式
    cv2.destroyAllWindows()
