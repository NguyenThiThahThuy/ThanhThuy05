# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 13:35:45 2024

@author: Nguyễn Thị Thanh Thùy
"""
n=int(input("Nhập số n:"))
S=sum(range(2,n+1,2))
if n>0:
  print(f"Tổng 2+4+6+..+{n} =",S)
else:
  print("Không hợp lệ")