# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 20:24:00 2023

@author: Admin
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt



img=cv2.imread("nois.jfif",0)
unique_values, counts = np.unique(img, return_counts=True)
 
most_common_index = np.argmax(counts)
most_common = unique_values[most_common_index]
frequency = counts[most_common_index]
print("val=",frequency) 

img_median = cv2.medianBlur(img, 3)
 
ori_hist=cv2.calcHist([img],[0],None,[256],[0,256])






plt.plot(ori_hist)
plt.title("orignal img")
plt.xlabel("pixel value")
plt.ylabel("frequency")
plt.show()

cv2.imshow("orignal img ",img)
cv2.imshow("removie noice",img_median)











cv2.waitKey(0)
cv2.destroyAllWindows()