# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 16:16:34 2023

@author: Admin
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt 


img=cv2.imread('home.png',0)
orihist=cv2.calcHist([img],[0],None,[256],[0,256])

new_img=cv2.normalize(img,None,0,255,cv2.NORM_MINMAX)

new_hist=cv2.calcHist([new_img],[0],None,[256],[0,256])




plt.plot(orihist)
plt.title("orignal img")
plt.xlabel("pixal value")
plt.ylabel("frequncy")
plt.show()

plt.plot(new_hist)
plt.title("normalization  img")
plt.xlabel("pixal value")
plt.ylabel("frequncy")
plt.show()



cv2.imshow("orignal ",img)
cv2.imshow("normalization",new_img)





cv2.waitKey(0)
cv2.destroyAllWindos()