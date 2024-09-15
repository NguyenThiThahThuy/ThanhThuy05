# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:18:38 2024

@author: Admin
"""
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
# Nhập vào số nguyên dương
n = int(input("Nhập vào số nguyên dương n: "))
# iểm tra và in kết quả
if is_prime(n):
    print(f"{n} là số nguyên tố.")
else:
    print(f"{n} không phải là số nguyên tố.")
