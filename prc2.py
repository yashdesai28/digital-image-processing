# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 20:10:36 2023

@author: Admin
"""

import cv2

img=cv2.imread('js2.png',0)
imgB=cv2.imread('js2.png',0)

cv2.imshow('origanl-grayscale',img)

wid,hig=img.shape

print(wid,hig)


for i in range(0,hig):
    
    for j in range(0,wid):
        
        if(img[i][j]==125):
                
            img[i][j]=255
        else:
            
            img[i][j]=125
                
                




cv2.imshow('Manipulate-img',img)



for i in range(0,hig):
    
    for j in range(0,wid):
        
        if(imgB[i][j]>125):
                
            imgB[i][j]=255
        else:
            
            imgB[i][j]=0

cv2.imshow('border-img',imgB)

cv2.waitKey(0)
# Window shown waits for any key pressing event
cv2.destroyAllWindows()