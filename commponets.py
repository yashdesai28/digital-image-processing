# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 22:03:57 2023

@author: Admin
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 21:13:58 2023

@author: Admin
"""


import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("plus.png",0) 

#structur element for detect words 
kernel=np.ones((1,1),np.uint8)
print(kernel)



otsu_threshold, image_result = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU,)
#6u tapadva mate object 
lines=cv2.erode(image_result, kernel)

#connected componets 
totallabel,labels,stats,centrois=cv2.connectedComponentsWithStats(lines, 4, cv2.CV_32S)

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



 


cv2.waitKey()
cv2.destroyAllWindows()