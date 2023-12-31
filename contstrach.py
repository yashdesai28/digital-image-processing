# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 13:43:44 2023

@author: Admin
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt 


img1=cv2.imread("img4.jpg",0)

size=(500,500)

img=cv2.resize(img1,size)


orihist=cv2.calcHist([img],[0],None,[256],[0,256])

min_percent = 2   # Low percentile
max_percent = 99  # High percentile
lo, hi = np.percentile(img, (min_percent, max_percent))

print(lo,hi)

# Apply linear "stretch" - lo goes to 0, and hi goes to 1
res_img1 = (img.astype(float) - lo) / (hi-lo)

cv2.imshow('res_img1', res_img1)

#Multiply by 255, clamp range to [0, 255] and convert to uint8
res_img = np.maximum(np.minimum(res_img1*255, 255), 0).astype(np.uint8)

rehisto=cv2.calcHist([res_img],[0],None,[256],[0,256])



plt.plot(orihist)
plt.title("orignal img") 
plt.xlabel("pixal value ")
plt.ylabel("frequncy")
plt.show()


plt.plot(rehisto)
plt.title("contrast  img")
plt.xlabel("pixal value ")
plt.ylabel("frequncy")
plt.show()

#Display images before and after linear "stretch":

cv2.imshow('res_img', res_img)
cv2.imshow("orignal",img)













cv2.waitKey(0)
cv2.destroyAllWindows()