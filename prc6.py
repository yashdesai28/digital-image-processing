# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 22:42:11 2023

@author: Admin
"""

import cv2

img=cv2.imread("home.png")

cv2.imshow("origanl", img)




for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        for c in range(img.shape[2]):
            if img[y,x,c]<215:
                img[y,x,c]+=40
            

cv2.imshow("britness", img)
cv2.waitKey(0)
# Window shown waits for any key pressing event
cv2.destroyAllWindows()
