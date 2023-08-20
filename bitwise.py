# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 19:43:51 2023

@author: Admin
"""

import cv2
import numpy as py
import matplotlib.pyplot as plt 

img1=cv2.imread("bitwc.png")
img2=cv2.imread("bitws1.png")

bit_and=cv2.bitwise_and(img1, img2)
bit_or=cv2.bitwise_or(img1, img2)
#bit_not=cv2.bitwise_not(img1, img2)
bit_xor=cv2.bitwise_xor(img1, img2,mask=None)


cv2.imshow("bitwc",img1)
cv2.imshow("bitws",img2)
cv2.imshow("bit_and",bit_and)
cv2.imshow("bit_or",bit_or)
cv2.imshow("bit_xor",bit_xor)











cv2.waitKey(0)
cv2.destroyAllWindows()