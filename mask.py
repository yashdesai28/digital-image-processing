# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 22:15:00 2023

@author: Admin
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 12:42:32 2023

@author: Admin
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt


img=cv2.imread("cat.png",0)
img2=cv2.imread("bitws1.png")
mask = np.ones_like(img) * 255
cv2.rectangle(mask, (100, 100), (200, 200),(0,0,0), -1)
cv2.imshow("mask",mask)
bit_xor=cv2.bitwise_xor(img,mask,mask=None)





cv2.imshow("mask",bit_xor)











cv2.waitKey()
cv2.destroyAllWindows()