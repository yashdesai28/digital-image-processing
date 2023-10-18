# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 21:28:58 2023

@author: Admin
"""



import cv2
import numpy as np
import matplotlib.pyplot as plt 


#img=cv2.imread("bitwc.png",0)

img=cv2.imread("mero.jpg",0)


# binarize the image 
binr = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1] 
  
# define the kernel 
kernel = np.ones((7, 7), np.uint8)
print(kernel)
  
# invert the image 
invert = cv2.bitwise_not(binr) 

erosion=cv2.erode(invert, kernel,iterations=1)

cv2.imshow("orignal",img)
cv2.imshow("ersion", erosion)
cv2.imshow("invert", invert)



cv2.waitKey(0)
cv2.destroyAllWindows()