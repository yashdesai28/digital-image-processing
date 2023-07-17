# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 13:59:16 2023

@author: Admin
"""

# import opencv
import cv2

# Load the input image
img=cv2.imread('js2.png')
cv2.imshow('orignal', img)
image = cv2.imread('js2.png',0)
cv2.imshow('GRY', image)

ret,bin_img= cv2.threshold(image, 125, 255,cv2.THRESH_BINARY)




cv2.imshow('BINARY',bin_img)

#o display image resolutions.

wid = image.shape[1]
hgt = image.shape[0]

  

# displaying the dimensions
print(str(wid) + "x" + str(hgt))


cv2.waitKey(0)
# Window shown waits for any key pressing event
cv2.destroyAllWindows()
