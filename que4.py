#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 12:44:05 2023

@author: bmiit202006100110086
"""


import cv2
import numpy as np
import matplotlib.pyplot as plt 


img=cv2.imread("5.jpg",0)
avg=np.mean(img)
print(avg)

ret,thresh1 = cv2.threshold(img,avg,255,cv2.THRESH_BINARY)


cv2.imshow("orignal",img)
cv2.imshow("binary",thresh1 )



cv2.waitKey(0)
cv2.destroyAllWindows()