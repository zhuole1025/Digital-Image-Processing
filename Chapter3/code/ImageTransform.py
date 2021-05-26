#!/user/bin/env python
# -*- coding:utf-8 -*-

import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

def img_reverse(img):
    return 255 - img;

img = cv2.imread('cat.jpg')
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows();
