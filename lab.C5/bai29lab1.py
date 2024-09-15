# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:16:30 2024

@author: Nguyễn Thị Thanh Thùy 
"""
s =int(input ("Nhập số nguyên dương có 4 chữ: "))
n=s//1000
t=(s%1000)//100
c=(s%1000%100)//10 
v=s%1000%100%10 
print("Tổng các chữ số:", n+t+c+v)
