# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 13:35:45 2024

@author: nguyễn Thịn Thanh Thùy
"""

n=int(input("Nhập n:"))
S=0 
for i in range(1,n+1):
  S+=1/i
print("S=1+ 1/2 + 1/3+..+ 1/n =",S)
 