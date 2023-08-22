# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 11:50:15 2023

@author: Admin
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt


img=cv2.imread("img4.jpg",0)

size=(500,500)

reimg=cv2.resize(img,size)

histogram=cv2.calcHist([reimg], [0], None, [256], [0,256])

power_low1=np.array(255*(reimg/255)**0.7,dtype='uint8')
histogram1=cv2.calcHist([power_low1], [0], None, [256], [0,256])

nimg=np.multiply(reimg,2,dtype='uint8')

plt.plot(histogram)
plt.title("orignal img")
plt.xlabel("pixal value")
plt.ylabel("fequency")
plt.show()


plt.plot(histogram1)
plt.title("gama img")
plt.xlabel("pixal value")
plt.ylabel("fequency")
plt.show()



cv2.imshow("orignal",reimg)

cv2.imshow("gama",power_low1)


cv2.waitKey(0)
cv2.destroyAllWindows()