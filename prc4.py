# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 13:53:06 2023

@author: Admin
"""


import cv2

img=cv2.imread('js2.png',0);


print("-------enter the  P  postion-------")

x=int(input("enter the x = "))
y=int(input("enter the y= "))

print()

wid,hid=img.shape

print("x=",x,"y=",y)

print("size=",wid,"x",hid)

print()

print("-------enter the  Q  postion-------")

a=int(input("enter the a = "))
b=int(input("enter the b= "))

print()
 
print("a=",a,"b=",b)



flg=int(0)

r=range(0,50)

print()

print("--------program 4-adjacent-------")

for i in range(y-1,y+2):
    
    for j in range(x-1,x+2):
        
        if i==y and j==x:
            
            if i-1==b and j==a:
                print("a and b val=",img[i-1][j],"  = ","x and y val =",img[i][j])
                
                if img[i-1][j] in r:
                    flg=1
                    print("1")
                    
            elif i==b and j-1==a:
                print("a and b val=",img[i][j-1],"  = ","x and y val =",img[i][j])
                
                if img[i][j-1] in r:
                    flg=1
                    print("2")
                    
            elif i+1==b and j==a:
                print("a and b val=",img[i+1][j],"  = ","x and y val =",img[i][j])
                
                if img[i+1][j] in r:
                    flg=1
                    print("3")
                    
            elif i==b and j+1==a:
                print("a and b val=",img[i][j+1],"  = ","x and y val =",img[i][j])
                
                if img[i][j+1] in r:
                    flg=1
                    print("4")
                
    
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
            
            if i-1==b and j==a:
                #print("a and b val=",img[i-1][j],"  = ","x and y val =",img[i][j])
                
                if img[i-1][j] in r:
                    flg=1
                    print("1")
                    
            elif i==b and j-1==a:
                #print("a and b val=",img[i][j-1],"  = ","x and y val =",img[i][j])
                
                if img[i][j-1] in r:
                    flg=1
                    print("2")
                    
            elif i+1==b and j==a:
                #print("a and b val=",img[i+1][j],"  = ","x and y val =",img[i][j])
                
                if img[i+1][j] in r:
                    flg=1
                    print("3")
                    
            elif i==b and j+1==a:
                #print("a and b val=",img[i][j+1],"  = ","x and y val =",img[i][j])
                
                if img[i][j+1] in r:
                    flg=1
                    print("4")
                
            elif i-1==b and j-1==a:
                
                if img[i-1][j-1] in r:
                    flg=1
                    print("5")
                
            elif i-1==b and j+1==a:
                
                if img[i-1][j+1] in r:
                    flg=1
                    print("6")
                
            elif i+1==b and j-1==a:
                
                if img[i+1][j-1] in r:
                    flg=1
                    print("7")
                
            elif i+1==b and j+1==a:
                
                if img[i+1][j+1] in r:
                    flg=1
                    print("8")
                
            else:
                print("ee ")
                flg=0
                
             
                
print()         

if flg==1:
    
    print("8 adjacent")
else:
    print("not 8 adjacent")
    
    

print()
flg=0

for i in range(y-1,y+2):
    
    for j in range(x-1,x+2):
        
        if i==y and j==x:
            
            if i+1==b and j==a or i-1==b and j==a or i==b and j+1==a or i==b and j-1==a:
                
                flg=1
                print("mm")
            else:
                
                if i+1==b and j+1==a:
                    
                    print("i+1 and j+1 = ",img[i+1][j+1],i,j)
                    
                    if img[i+1][j] not in r:
                        
                        print("++")
                        flg=1
                        break
                        
                    elif img[i][j+1] not in r:
                        
                        print("++el")
                        flg=1
                        break
                    else:
                        print("++else")
                        flg=0
                        break
                    
                    
                elif i+1==b and j-1==a:
                    
                    print("i+1 and j-1 = ",img[i+1][j-1])
                    
                    if img[i][j-1] not in r:
                        
                        print("+-")
                        flg=1
                        break
                        
                    elif img[i+1][j] not in r:
                        
                        print("+-el")
                        flg=1
                        break
                    else:
                        print("+-else")
                        flg=0
                        break
                
                elif i-1==b and j+1==a:
                
                    print("i-1 and j+1 = ",img[i-1][j+1])
                    
                    if img[i-1][j] not in r:
                        
                        print("-+")
                        flg=1
                        break
                        
                    elif img[i][j+1] not in r:
                        
                        print("-+el")
                        flg=1
                        break
                    else:
                        print("-+else")
                        flg=0
                        break
                
                elif i-1==b and j-1==a:
                    
                    print("i-1 and j-1 = ",img[i-1][j-1])
                    
                    if img[i][j-1] not in r:
                        
                        print("--")
                        flg=1
                        break
                        
                    elif img[i-1][j] not in r:
                        
                        print("--el")
                        flg=1
                        break
                    else:
                        print("--else")
                        flg=0
                        break
                    
               
    

print()



if flg==1:
    
    print("m adjacent")
else:
    print("not m adjacent")



cv2.imshow("gray",img)





cv2.waitKey(0)
# Window shown waits for any key pressing event
cv2.destroyAllWindows()