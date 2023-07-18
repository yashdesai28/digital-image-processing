#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 05:57:28 2023

@author: bmiit202006100110086
"""

import cv2

img=cv2.imread('js2.png',0);

x=int(input("enter the x = "))
y=int(input("enter the y= "))

wid,hid=img.shape

print(x,y)

print(wid,"x",hid)


flg=int(0)

r=range(0,130)

print()

print("--------program 4-adjacent-------")

for i in range(y-1,y+2):
    
    for j in range(x-1,x+2):
        
        if i==y and j==x:
            
            if img[i][j] in r and  img[i-1][j] in r and img[i][j-1] in r and img[i+1][j] in r and img[i][j+1] in r:
                
                flg=1
                print("ff")
            else:
                print("ee ")
                flg=0
                
             
                
            
print()         


if flg==1:
    
    print("4 adjacent")
else:
    print("not 4 adjacent")
    
    

print("------- program 8-adjacent-------------")

flg=0

for i in range(y-1,y+2):
    
    for j in range(x-1,x+2):
        
        if i==y and j==x:
            
            if img[i][j] in r and  img[i-1][j] in r and img[i][j-1] in r and img[i+1][j] in r and img[i][j+1] in r and img[i-1][j-1] in r and img[i-1][j+1] in r and img[i+1][j-1] in r and img[i+1][j+1] in r:
                
                flg=1
                print("ff")
            else:
                
                flg=0
                
             

if flg==1:
    
    print("8 adjacent")
else:
    print("not 8 adjacent")


cv2.imshow("gray",img)





cv2.waitKey(0)
# Window shown waits for any key pressing event
cv2.destroyAllWindows()