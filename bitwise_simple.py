#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Michael Yu'
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = plt.imread("E:\Raspberry_upload\hat.jpg")
img_bg = plt.imread("E:\Raspberry_upload\image55.jpg")
"""
plt和cv2的通道顺序不一致，一定要注意。
"""
img_new = cv2.resize(img,(200,200))
rows,cols,channels = img_new.shape
rio = img_bg[0:rows, 0:cols]

img2gray = cv2.cvtColor(img_new,cv2.COLOR_BGR2GRAY)
print img2gray.shape
plt.imshow(img2gray)
plt.subplot(321),plt.imshow(img),plt.title('ORIGINAL')
plt.subplot(322),plt.imshow(img2gray,"gray"),plt.title('gray')
ret, mask = cv2.threshold(img2gray, 240, 255, cv2.THRESH_BINARY)
#0代表黑色 255代表白色
mask_inv = cv2.bitwise_not(mask)
plt.subplot(323),plt.imshow(mask,"gray"),plt.title('THRESH_BINARY')
plt.subplot(324),plt.imshow(mask_inv,"gray"),plt.title('THRESH_BINARY_inv')

rio_bg = cv2.bitwise_and(rio,rio,mask = mask)

plt.subplot(325),plt.imshow(rio_bg,"gray"),plt.title('rio_bg')

rio_fg = cv2.bitwise_and(img_new,img_new,mask = mask_inv)
dst = cv2.add(rio_bg,rio_fg)
img_bg[0:rows,0:cols] = dst
plt.subplot(326),plt.imshow(img_bg),plt.title('last')
"""
cv2.THRESH_BINARY_INV
cv2.THRESH_TRUNC
cv2.THRESH_TOZERO
cv2.THRESH_TOZERO_INV
"""

plt.show()
