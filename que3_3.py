#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 12:44:05 2023

@author: bmiit202006100110086
"""


import cv2
import numpy as np
import matplotlib.pyplot as plt 


img=cv2.imread("3.jpg",0)
orihist=cv2.calcHist([img],[0],None,[256],[0,256])
image2 = cv2.convertScaleAbs(img, alpha=0.5, beta=60)
equ= cv2.normalize(img, None, 0, 1.0, cv2.NORM_MINMAX, dtype=cv2.CV_32F)
chanhist=cv2.calcHist([image2],[0],None,[256],[0,256])



plt.plot(orihist)
plt.title("orignal img3 histogram")
plt.xlabel("pixel value")
plt.ylabel("frequncy")
plt.show()

plt.plot(chanhist)
plt.title("chan img3 histogram")
plt.xlabel("pixel value")
plt.ylabel("frequncy")
plt.show()


cv2.imshow("orignal",img)
cv2.imshow("img ",image2)
cv2.imshow("equ ",equ)





cv2.waitKey(0)
cv2.destroyAllWindows()