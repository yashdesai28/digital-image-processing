# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 21:57:15 2023

@author: Admin
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt 


def nagative(img):
    
    nagativ=255-img
    return nagativ

def logtransformation(img):
    
    c = 255 / np.log(1 + np.max(img))
    print(c)
    log_img=c*(np.log1p(img))
    log_img=np.uint8(log_img)
    
      
# Apply log transformation method
    #c = 255 / np.log(1 + np.max(img))
    #log_image = c * (np.log(img + 1))
   
# Specify the data type so that
# float value will be converted to int
    #log_image = np.array(log_image, dtype = np.uint8)
    return log_img

def powerlow(img):
    
   # c = 255/(np.log(1 + np.max(img)))
    #print(c,"==",255/(img/255))
    power_low=np.array(255*(img/255)**1,dtype='uint8')
    power_low1=np.array(255*(img/255)**0.5,dtype='uint8')
    power_low3=np.array(255*(img/255)**0.7,dtype='uint8')
    
    return power_low,power_low1,power_low3
    

img=cv2.imread("open.jpg",0)
img1=cv2.imread("open.jpg",0)
img2=cv2.imread("open.jpg",0)

size=(500,500)

imgp=cv2.resize(img2,size)

nagative_img=nagative(img)
log_img=logtransformation(img1)
power_low,power_low1,power_low3=powerlow(imgp)


imgmain=cv2.hconcat([power_low1,power_low,power_low3])

cv2.imshow("a2",imgmain)
cv2.imshow("orijnal",imgp)
cv2.imshow("nagative",nagative_img)
cv2.imshow("logtransformation", log_img)
cv2.imshow("power_log",power_low)

logtrn=cv2.calcHist([log_img],[0],None,[256],[0,256])

orignal=cv2.calcHist([img],[0],None,[256],[0,256])
negative=cv2.calcHist([nagative_img],[0],None,[256],[0,256])
law1=cv2.calcHist([power_low],[0],None,[256],[0,256])

plt.plot(logtrn)
plt.title("logtransformation")
plt.xlabel("pixal value")
plt.ylabel("frecuncy")
plt.show()

plt.plot(orignal)
plt.title("orignal image")
plt.xlabel("pixal value")
plt.ylabel("frecuncy")
plt.show()


plt.plot(negative)
plt.title("negative image")
plt.xlabel("pixal value")
plt.ylabel("frecuncy")
plt.show()


plt.plot(power_low1)
plt.title("power_low1")
plt.xlabel("pixal value")
plt.ylabel("frecuncy")
plt.show()









cv2.waitKey(0)
cv2.destroyAllWindows()