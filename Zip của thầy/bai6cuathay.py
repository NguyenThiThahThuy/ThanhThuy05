# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 15:36:12 2024

@author: Nguyễn Thị Thanh Thùy 
"""

n = int(input("Nhập số lần in 'Hello': "))
if n <= 0 or n > 1000:
    print("Số lần lặp không hợp lệ. Vui lòng nhập số nguyên dương nhỏ hơn 1000.")
else:
    for _ in range(n):
      print("Hello")
