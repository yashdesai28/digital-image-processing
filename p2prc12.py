#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 11:58:38 2023

@author: bmiit202006100110086
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 12:42:32 2023

@author: Admin
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt


img=cv2.imread("boat1.jpg",0)

orihist=cv2.calcHist([img],[0],None,[256],[0,256])


midalvalue=(np.min(img)+np.max(img))/2
print("midal value=",midalvalue)

mid,midimg=cv2.threshold(img,midalvalue,255,cv2.THRESH_BINARY)


avg=np.mean(img)

mtb,avgimg=cv2.threshold(img,avg,255,cv2.THRESH_BINARY)

print("avg =",avg)



otsu_threshold, image_result = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU,)
print("Obtained threshold: ", otsu_threshold)


ret,histo = cv2.threshold(img,50,255,cv2.THRESH_BINARY)

binarydata=np.where(image_result>0,0,1)
img2=img*binarydata
cv2.imwrite('color_img1.jpg', img2)
img4=img2
img3=cv2.imread('1.jpg',0)
#img3=cv2.resize(img3,(325,445))
for i in range(0,324):    
    for j in range(0,444):
        
        if img2[i][j]==0:
            img4[i][j]=img3[i][j]
        else:
            img4[i][j]=img2[i][j]



#img2=np.where(img2==0,img3,img2)
cv2.imwrite('color_img.jpg', img4)

cv2.imshow("object extracted", cv2.imread('color_img1.jpg'))
cv2.imshow("object", cv2.imread('color_img.jpg'))

plt.plot(orihist)
plt.title("orignal img") 
plt.xlabel("pixal value ")
plt.ylabel("frequncy")
plt.show()



#cv2.imshow("orignal ",img)
#cv2.imshow("MID",midimg)
#cv2.imshow("ots",image_result)
#cv2.imshow("avg",avgimg)

#cv2.imshow("histo",histo)



cv2.waitKey()
cv2.destroyAllWindows()