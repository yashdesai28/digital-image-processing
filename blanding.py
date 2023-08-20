# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 18:53:03 2023

@author: Admin
"""

import cv2
import numpy as py
import matplotlib.pyplot as plt

img1=cv2.imread("elon.jpg",0)
img2=cv2.imread("hole.png",0)

size=(805,987)

reimg2=cv2.resize(img2, size)

add2=cv2.addWeighted(img1, 1, reimg2, 0.5, 0.0)


cv2.imshow("add2",add2)



cv2.waitKey(0)
cv2.destroyAllWindows()