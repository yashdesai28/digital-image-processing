# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 16:14:49 2023

@author: Admin
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt



def calbri(img):
    
    britness=np.mean(img)
    return britness

def calcon(img):
    
    contrast=np.std(img)
    return contrast

def histo(img):
    
    histogram=cv2.calcHist([img],[0],None,[256],[0,256])
    return histogram

def minmax(img):
    
    min_color=np.min(img)
    max_color=np.max(img)
    return min_color,max_color

    
    
    


img=cv2.imread("home.png",0)

britness=calbri(img)
contrast=calcon(img)
histogram=histo(img)
min_color,max_color=minmax(img)
print("britness =",britness)
print("contrast =",contrast)
print("min_clor=",min_color," ","max_color=",max_color)

#ret,img1=cv2.threshold(img, 127, 100, cv2.THRESH_BINARY)

#cv2.imshow("helo",img1)

adjusted = cv2.convertScaleAbs(img, alpha=1, beta=40)

contrast = 5. # Contrast control ( 0 to 127)
brightness = 2. # Brightness control (0-100)
out = cv2.addWeighted( img, contrast, img, 0, brightness)

plt.plot(histogram)
plt.title("histogram")
plt.xlabel("pixal value")
plt.ylabel("frecuncy")
plt.show()

cv2.imshow("convertscale",adjusted)
cv2.imshow("addweighted",out)
cv2.imshow("orignal",img)






cv2.waitKey(0)
cv2.destroyAllWindows()