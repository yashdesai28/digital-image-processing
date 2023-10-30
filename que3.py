#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 12:28:30 2023

@author: bmiit202006100110086
"""


import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("9.jpg",0) 

#structur element for detect words 
kernel=np.ones((1,1),np.uint8)
otsu_threshold, image_result = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU,)

invert = cv2.bitwise_not(image_result)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.imshow("orignal",img)
#6u tapadva mate object 
lines=cv2.erode(invert, kernel)

kernel1=np.ones((6,6),np.uint8)
dailate=cv2.dilate(lines, kernel1)


#connected componets 
totallabel,labels,stats,centrois=cv2.connectedComponentsWithStats(dailate, 8, cv2.CV_32S)

#applye color for diffrent objects 
colors=np.random.randint(0,255,size=(totallabel,3),dtype=np.uint8)

#backgound is black 
colors[0]=[0,0,0]
#applye a color for labels 
colors_componet=colors[labels]

print("total words=",totallabel-1)


cv2.imshow("orijnal", img)
cv2.imshow("erosion",lines)
cv2.imshow("color img", colors_componet)
cv2.imshow("dailation", dailate)




 


cv2.waitKey()
cv2.destroyAllWindows()
