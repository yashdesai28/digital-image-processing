#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 12:44:05 2023

@author: bmiit202006100110086
"""


import cv2
import numpy as np
import matplotlib.pyplot as plt 


img=cv2.imread("3.jpg",0)




cv2.imshow("orignal",img)




cv2.waitKey(0)
cv2.destroyAllWindows()