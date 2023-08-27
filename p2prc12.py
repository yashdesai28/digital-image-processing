# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 12:42:32 2023

@author: Admin
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt


img=cv2.imread("ots.jpg",0)


midalvalue=(np.min(img)+np.max(img))/2
print("midal value=",midalvalue)

mid,midimg=cv2.threshold(img,midalvalue,255,cv2.THRESH_BINARY)


avg=np.mean(img)

mtb,avgimg=cv2.threshold(img,avg,255,cv2.THRESH_BINARY)

print("avg =",avg)

otsu_threshold, image_result = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU,)
print("Obtained threshold: ", otsu_threshold)





cv2.imshow("orignal ",img)
cv2.imshow("MID",midimg)
cv2.imshow("ots",image_result)
cv2.imshow("avg",avgimg)











cv2.waitKey()
cv2.destroyAllWindows()