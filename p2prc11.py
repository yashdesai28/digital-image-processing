# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 15:43:18 2023

@author: Admin
"""

import cv2
import numpy as py 
import matplotlib.pyplot as plt 


img1=cv2.imread("img4.jpg",0)
size=(500,500)

img=cv2.resize(img1,size)
orihist=cv2.calcHist([img],[0],None,[256],[0,256])

#equalization function 
normal_img=cv2.equalizeHist(img)
normal_hist=cv2.calcHist([normal_img],[0],None,[256],[0,256])







plt.plot(orihist)
plt.title("orignal image")
plt.xlabel("pixal value ")
plt.ylabel("fercuency")
plt.show()


plt.plot(normal_hist)
plt.title("normalaize image")
plt.xlabel("pixal value ")
plt.ylabel("fercuency")
plt.show()


cv2.imshow("orignal ",img)
cv2.imshow("normalization ",normal_img)


cv2.waitKey(0)
cv2.destroyAllWindows()