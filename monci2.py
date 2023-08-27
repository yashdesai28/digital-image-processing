# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 00:21:19 2023

@author: Admin
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt


def power_low(img,hid,wid0):
    
     
    # Create zeros array to store the stretched image
    img1 = np.zeros((img.shape[0],img.shape[1]),dtype = 'uint8')
    
    for i in range(0,hid):
        
        for j in range(0,wid):
            
            if j>358:
                img1[i,j]=255*(img[i,j]/255)**0.30
            else:
                img1[i,j]=img[i,j]
    return img1

def log_transformation(img,hid,wid):
    
    img2=np.zeros((img.shape[0],img.shape[1]),dtype='uint8')
    
    # Apply log transform.
    c = 255/(np.log(1 + np.max(img)))
    log_transformed = c * np.log(1 + img)
    
    log_transformed=np.array(log_transformed,dtype='uint8')
    
    return log_transformed
    
    





img=cv2.imread("haf.jpg",0)
hid,wid=img.shape

print(hid,"x",wid)
orihist=cv2.calcHist([img],[0],None,[256],[0,256])


power_low_img=power_low(img,hid,wid)
power_hist=cv2.calcHist([power_low_img],[0],None,[256],[0,256])

log_transformed_img=log_transformation(img, hid, wid)
log_hist=cv2.calcHist([log_transformed_img],[0],None,[256],[0,256])






plt.plot(orihist)
plt.title("orignal ")
plt.xlabel("pixel value")
plt.ylabel("frequency ")
plt.show()


plt.plot(power_hist)
plt.title("power_law ")
plt.xlabel("pixel value")
plt.ylabel("frequency ")
plt.show()


plt.plot(log_hist)
plt.title("logtransformation ")
plt.xlabel("pixel value")
plt.ylabel("frequency ")
plt.show()

cv2.imshow("orignal",img)
cv2.imshow("power",power_low_img)
cv2.imshow("log",log_transformed_img)




cv2.waitKey(0)
cv2.destroyAllWindows()