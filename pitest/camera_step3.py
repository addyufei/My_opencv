#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Michael Yu'
"""
抓拍RBG图片
"""
import picamera
import picamera.array
import time
import numpy as np
import cv2
import io

def PreviewOpencvBGR(camera):
    image_size = (1920,1080)
    with picamera.array.PiRGBArray(camera,image_size) as stream:
        for frame in camera.capture_continuous(stream, format='bgr', splitter_port = 2, resize = image_size, use_video_port=True):
            cv_image = frame.array #转换到opencv图像
            print cv_image.shape
            stream.seek(0)
            stream.truncate(0)

with picamera.PiCamera() as camera:
    camera.resolution = (1920,1080)
    camera.framerate = 25
    camera.annotate_text = "HKUTANGYU.Inc"
    camera.vflip = True # 垂直翻转
    camera.hflip = True # 水平翻转
    print "start preview direct from GPU"
    camera.start_preview() # the start_preview() function
    PreviewOpencvBGR(camera)

