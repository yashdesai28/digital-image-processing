# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 22:02:59 2023

@author: Admin
"""

import cv2
import math 

def d3(x,y,s,t):
    
    return math.sqrt((x-s)**2+(y-t)**2)


def d4(x,y,s,t):
    
    return abs(x-s)+abs(y-t)


def d8(x,y,s,t):

    return max((x-s),abs(y-t))
    

x =int(input("enter the x= "))
y =int(input("enter the y= "))

s=int(input("enter the s = "))
t=int(input("enter the t = "))




print("D3 =",d3(x, y, s, t))

print("D4 =",d4(x, y, s, t))

print("D8 =",d8(x, y, s, t))



