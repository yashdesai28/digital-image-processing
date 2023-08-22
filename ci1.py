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


new_image = np.zeros((img.shape[0],img.shape[1]), dtype='uint8')

print(wid,"x",hid)


new_image = cv2.convertScaleAbs(img, alpha=1, beta=80)
        
    

cv2.imshow("orignal",img)
cv2.imshow("manipulat",new_image)

print("hii")

cv2.waitKey(0)
cv2.destroyAllWindows()