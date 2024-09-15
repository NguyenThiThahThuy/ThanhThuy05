# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 13:35:46 2024

@author: Nguyễn Thị Thanh Thùy
"""

n=int(input("Nhập số n:"))
S=0
for i in range(2,2*n+1,2):
    S+=1/i
print(f"S=1/2+..+1/{2*n}=",S)