# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 20:23:15 2023

@author: Admin
"""

import cv2

img=cv2.imread('js2.png',0)

wid,hid=img.shape

print(wid,"x",hid)

x=int(input("enter the x = "))
y=int(input("enter the y ="))


print()
print("4-neighbors pixel positions and values")

for i in range(y-1,y+2):
    
    for j in range(x-1,x+2):
        
        if i==y and j==x:
            
            print("positions: x=",j," y= ",i,"|","circle",img[i][j])
            print("positions: x=",j," y= ",i-1,"|","top",img[i-1][j])
            print("positions: x=",j-1," y= ",i,"|","left",img[i][j-1])
            print("positions: x=",j," y= ",i+1,"|","bottom",img[i+1][j])
            print("positions: x=",j+1," y= ",i,"|","right",img[i][j+1])
        
print()         
print("8-neighbors pixel positions and values")
    
for i in range(y-2,y+2):
    
    for j in range(x-2,x+2):
        
        if i==y and j==x:
            
            print("positions: x=",j," y= ",i,"|","circle",img[i][j])
            print("positions: x=",j-1," y= ",i-1,"|","cross left top",img[i-1][j-1])
            print("positions: x=",j," y= ",i-1,"|","top",img[i-1][j])
            print("positions: x=",j+1," y= ",i-1,"|","cross right top",img[i-1][j+1])
            print("positions: x=",j-1," y= ",i,"|","left",img[i][j-1])
            print("positions: x=",j-1," y= ",i+1,"|","cross left bottom",img[i+1][j-1])
            print("positions: x=",j," y= ",i+1,"|","bottom",img[i+1][j])
            print("positions: x=",j+1," y= ",i,"|","right",img[i][j+1])
            print("positions: x=",j+1," y= ",i+1,"|","cross right bottom",img[i+1][j+1]) 
            
    

cv2.imshow("gray",img)


cv2.waitKey(0)
# Window shown waits for any key pressing event
cv2.destroyAllWindows()