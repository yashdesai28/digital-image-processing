# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 00:35:31 2023

@author: Admin
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 21:57:15 2023

@author: Admin
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt 



def apply_contrast_stretching(image):
    min_intensity = np.min(image)
    max_intensity = np.max(image)
    
    stretched_image = ((image - min_intensity) / (max_intensity - min_intensity)) * 255
    stretched_image = np.clip(stretched_image, 0, 255).astype(np.uint8)
    
    return stretched_image

img=cv2.imread("lowcont.jpg",0)



cont=cv2.calcHist([img],[0],None,[256],[0,256])

cont_img=apply_contrast_stretching(img)

contmain=cv2.calcHist([cont_img],[0],None,[256],[0,256])

cv2.imshow("orignal",img)
cv2.imshow("contimg",cont_img)


plt.plot(cont)
plt.title("orignal")
plt.xlabel("pixal value")
plt.ylabel("frecuncy")
plt.show()

plt.plot(contmain)
plt.title("cont_img")
plt.xlabel("pixal value")
plt.ylabel("frecuncy")
plt.show()





cv2.waitKey(0)
cv2.destroyAllWindows()