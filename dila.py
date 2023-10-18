# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 21:46:25 2023

@author: Admin
"""


import cv2
import numpy as np
import matplotlib.pyplot as plt 


#img=cv2.imread("bitwc.png",0)

img=cv2.imread("abc.jpg",0)


# binarize the image 
binr = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1] 
  
# define the kernel 
kernel = np.ones((7, 7), np.uint8)
print(kernel)
  
# invert the image 
invert = cv2.bitwise_not(binr) 


dilation=cv2.dilate(invert, kernel)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
cv2.imshow("orignal",img)
cv2.imshow("dilation", dilation)
cv2.imshow("invert", invert)
cv2.imshow("gradient", gradient)




cv2.waitKey(0)
cv2.destroyAllWindows()