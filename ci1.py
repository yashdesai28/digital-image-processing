# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 15:36:51 2023

@author: Admin
"""

import cv2
import numpy as np
import matplotlib.pyplot as pt

img=cv2.imread("home.png",0)

hid,wid=img.shape
cv2.imshow("orignal",img)

print(wid,"x",hid)

for i in range(0, hid):
    
    for j in range(0,wid):
        
        
        if img[i][j]<215:
            img[i][j]+=40
        
    

cv2.imshow("manipulet",img)

print("hii")

cv2.waitKey(0)
cv2.destroyAllWindows()