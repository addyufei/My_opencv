#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Michael Yu'
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread("E:\Raspberry_upload\image55.jpg",0)
plt.imshow(img,cmap="gray",interpolation='bicubic')
plt.xticks([]),plt.yticks([])
#隐藏横坐标和纵坐标
plt.show()
