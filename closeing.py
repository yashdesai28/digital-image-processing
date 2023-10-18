# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 22:59:14 2023

@author: Admin
"""



import cv2
import numpy as np
import matplotlib.pyplot as plt 


#img=cv2.imread("bitwc.png",0)

img=cv2.imread("fnoise.jpg",0)


# binarize the image 
binr = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1] 
  
# define the kernel 
kernel = np.ones((3, 3), np.uint8)
print(kernel)
  
# invert the image 
invert = cv2.bitwise_not(binr) 



closeing = cv2.morphologyEx(invert, cv2.MORPH_CLOSE, kernel)
cv2.imshow("orignal",img)

cv2.imshow("invert", invert)
cv2.imshow("closing", closeing)




cv2.waitKey(0)
cv2.destroyAllWindows()