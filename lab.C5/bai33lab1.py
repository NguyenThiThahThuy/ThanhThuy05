# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:18:38 2024

@author: Nguyễn Thị Thanh Thùy 
"""
n=int (input("Nhập vào 1 số: "))
for i in range(1,n+1):
   while  i**2==n:
       print(n,"là số chính phương ")
   else:
        n=int (input("Nhập lại vào 1 số: "))