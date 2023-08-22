# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 15:41:12 2023

@author: Admin
"""

import cv2
import numpy as np


img1=cv2.imread("xrayh.jpg",0)

size=(600,600)

img=cv2.resize(img1,size)

withb=np.zeros((img.shape[0],img.shape[1]),dtype='uint8')
withoutb=np.zeros((img.shape[0],img.shape[1]),dtype='uint8')

for i in range(0,600):
    
    for j in range(0,600):
        
        if img[i,j]>=150 and img[i,j]<=255:
            withb[i,j]=255
            withoutb[i,j]=255
        else:
            withb[i,j]=img[i][j]
        

cv2.imshow("orignal img",img)

cv2.imshow("with background",withb)
cv2.imshow("with out background",withoutb)




cv2.waitKey(0)
cv2.destroyAllWindows()