# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:09:44 2024

@author: Nguyễn Thị Thanh Thùy 
"""
n=int(input ("Nhấp giá trị n:"))
while n<0:
    n=int(float ("Nhấp lại giá trị:"))
else:
    print("giá trị n là:")
for i in range(1,n+1,1):
  divisors=[]
  if n%i==0 :
     print (i,end=",")
     
          
