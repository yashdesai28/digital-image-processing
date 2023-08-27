# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 23:04:32 2023

@author: Admin
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt


img=cv2.imread("city.jpg",0)

orihist=cv2.calcHist([img],[0],None,[256],[0,256])


equimg=cv2.equalizeHist(img)
equhist=cv2.calcHist([equimg],[0],None,[256],[0,256])







# histogram of orijnal img 
plt.plot(orihist)
plt.title("orignal img")
plt.xlabel("pixel value ")
plt.ylabel("frequency")
plt.show()

#histogram of equalize histogram 
plt.plot(equhist)
plt.title("equalize hist")
plt.xlabel("pixel value")
plt.ylabel("frequency ")
plt.show()

#orignal img show
cv2.imshow("orignal img",img)


#using equalizeHist function after img show 
cv2.imshow("equalize hist",equimg) 





cv2.waitKey(0)
cv2.destroyAllWindows()