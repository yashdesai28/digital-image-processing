#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 12:21:12 2023

@author: bmiit202006100110086
"""


import cv2
import numpy as np
import matplotlib.pyplot as plt


img4=cv2.imread("5.jpg",0)

avg=np.mean(img4)
print(avg)


withb=np.zeros((img4.shape[0],img4.shape[1]),dtype='uint8')
withoutb=np.zeros((img4.shape[0],img4.shape[1]),dtype='uint8')

for i in range(0,img4.shape[0]):
    
    for j in range(0,img4.shape[1]):
        
        if img4[i,j]>=85 and img4[i,j]<=255:
            withb[i,j]=255
            withoutb[i,j]=255
        else:
            withb[i,j]=img4[i][j]
        

cv2.imshow("orignal img",img4)

cv2.imshow("with background",withb)
cv2.imshow("with out background",withoutb)

cv2.imshow("orignal img4",img4)

cv2.waitKey(0)
cv2.destroyAllWindows()