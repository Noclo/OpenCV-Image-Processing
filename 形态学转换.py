# -*- coding: utf-8 -*-
# @Time : 2020/5/29
# @Author : J
# @File : 形态学转换.py
# @Software: PyCharm


#侵蚀
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("erosion.png",0)
kernel = np.ones((9,9),np.uint8)
# erosion = cv.erode(img,kernel,iterations = 1)#侵蚀
# dilation = cv.dilate(img,kernel,iterations = 1) #扩张
# opening = cv.morphologyEx(img,cv.MORPH_OPEN,kernel) #开运算
# closing = cv.morphologyEx(img,cv.MORPH_CLOSE,kernel) #闭运算
# gradient = cv.morphologyEx(img,cv.MORPH_GRADIENT,kernel) #形态学梯度  镂空 轮廓
# tophat = cv.morphologyEx(img,cv.MORPH_TOPHAT,kernel) #顶帽
blackhat = cv.morphologyEx(img,cv.MORPH_BLACKHAT,kernel) #黑帽





plt.subplot(1,2,1),plt.imshow(img),plt.title("Original") #121 1代表行 2代表列  1代表第一个图
plt.xticks([]),plt.yticks([])
plt.subplot(1,2,2),plt.imshow(blackhat),plt.title("closing")
plt.xticks(([])),plt.yticks([])
plt.show()















