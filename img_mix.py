#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Michael Yu'
import cv2
import numpy as np
from matplotlib import pyplot as plt
img1 = cv2.imread("E:\Raspberry_upload\image55.jpg")
img2 = cv2.imread("E:\Raspberry_upload\y22.jpg")
res = cv2.resize(img2,(720L,480L)) #调整img2尺寸
print res.shape
print img1.shape
dst = cv2.addWeighted(img1,0.9,res,0.1,0)
plt.imshow(dst)
plt.show()
