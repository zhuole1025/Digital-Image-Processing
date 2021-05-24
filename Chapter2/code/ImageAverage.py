#!/user/bin/env python
# -*- coding:utf-8 -*
import cv2
import numpy as np
import random
import skimage
from skimage import util

def imgAverage(img,imgnum):
    # 随机生成imgnum张高斯噪声图像
    imgs = [util.random_noise(img, "gaussian")] * imgnum
    height, width, channels = img.shape
    NewImage = np.zeros((height, width, channels), np.float)#random_noise()函数生成的图像为浮点数据图像
    for k in range (imgnum):
        NewImage += imgs[k]
    NewImage /= imgnum
    return NewImage

img = cv2.imread('img2.jpg')
cv2.imshow("img",img)
img_noised = util.random_noise(img, "gaussian")
cv2.imshow("img_noised",img_noised)
imageaverage5 = imgAverage(img,5)
imageaverage10 = imgAverage(img,10)
imageaverage20 = imgAverage(img,20)
imageaverage50 = imgAverage(img,50)
cv2.imshow("imageaverage5",imageaverage5)
cv2.imshow("imageaverage10",imageaverage10)
cv2.imshow("imageaverage20",imageaverage20)
cv2.imshow("imageaverage50",imageaverage50)
cv2.waitKey(0)
cv2.destroyAllWindows()