#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 11:39:10 2023

@author: bmiit202006100110086
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt


img3=cv2.imread("3.jpg",0)
img1=cv2.imread("1.jpg",0)
img=cv2.imread("2.png",0)


size=(700,466)

img2=cv2.resize(img,size)

orihist=cv2.calcHist([img3],[0],None,[256],[0,256])
orihist1=cv2.calcHist([img1],[0],None,[256],[0,256])
orihist2=cv2.calcHist([img2],[0],None,[256],[0,256])

equ_img=cv2.equalizeHist(img3)
equhist=cv2.calcHist([equ_img],[0],None,[256],[0,256])

#power_img=np.array(255*(img/255)**0.5,dtype='uint8')


equ_img1=cv2.equalizeHist(img1)




equ_img2=cv2.equalizeHist(img2)
equhist2=cv2.calcHist([equ_img2],[0],None,[256],[0,256])

img_normalized = cv2.normalize(img1, None, 0.5, 1.9, cv2.NORM_MINMAX, dtype=cv2.CV_32F)

power_low=np.array(255*(img1/255)**3.6,dtype='uint8')
equhist1=cv2.calcHist([power_low],[0],None,[256],[0,256])

print(255*(237/255)**3.6)


plt.plot(orihist)
plt.title("orignal img3 histogram")
plt.xlabel("pixel value")
plt.ylabel("frequncy")
plt.show()


plt.plot(equhist)
plt.title("equalize img3 histogram")
plt.xlabel("pixel value")
plt.ylabel("frequncy")
plt.show()

plt.plot(orihist1)
plt.title("orignal img1 histogram")
plt.xlabel("pixel value")
plt.ylabel("frequncy")
plt.show()

plt.plot(equhist1)
plt.title("equalize img1 histogram")
plt.xlabel("pixel value")
plt.ylabel("frequncy")
plt.show()


plt.plot(orihist2)
plt.title("orignal img2 histogram")
plt.xlabel("pixel value")
plt.ylabel("frequncy")
plt.show()

plt.plot(equhist2)
plt.title("improve img2 histogram")
plt.xlabel("pixel value")
plt.ylabel("frequncy")
plt.show()

cv2.imshow("orignal img3",img3)
cv2.imshow("improve img3",equ_img)
cv2.imshow("orignal img1",img1)
cv2.imshow("improve img1",equ_img1)
cv2.imshow("orignal img2",img2)
cv2.imshow("improve img2",equ_img2)


cv2.imshow("power low 1 img",power_low)



cv2.waitKey(0)
cv2.destroyAllWindows()