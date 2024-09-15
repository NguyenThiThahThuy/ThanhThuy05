# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 13:35:41 2024

@author: Nguyễn Thị Thanh Thùy 
"""
n=int(input("Nhập số n:"))
S=sum(range(1,n+1,1))
if n>0:
        print("Tổng các số nguyên S=1+2+..+n là:",S)
else:
        print("Không hợp lệ")
        