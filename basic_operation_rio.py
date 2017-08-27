#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Michael Yu'

import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread("E:\Raspberry_upload\image55.jpg")
px = img.item(100,100,1)
print px
#img.itemset((100,100,1),100)  #像素设置
print img.shape
"""
返回行 列 通道 ，如果是只返回行和列说明是灰度图。
(480L, 720L, 3L)
"""
print img.size
"""
图像的像素数目1036800
"""
print img.dtype
"""
图像的数据类型uint8
"""
img_roi_y = 28                           #[1]设置ROI区域的左上角的起点
img_roi_x = 440
img_roi_height = 104                         #[2]设置ROI区域的高度
img_roi_width = 175                           #[3]设置ROI区域的宽度
deng = img[img_roi_y:(img_roi_y+img_roi_height),
       img_roi_x:(img_roi_x+img_roi_width),
       1:2]
"""
3维数组，第一维 y坐标（行数） 第二维 x坐标（列数） 第3维 B G R
"""
img[0:104,0:175,1:2] = deng
plt.imshow(img)
plt.show()
