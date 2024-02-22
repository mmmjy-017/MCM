# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 23:01:17 2023

@author: ushop
"""
import numpy as np

pi = 3.14159265358979

p = -2 * 1852
num = 0
pre_dis = 0
theta = 120 * pi / 180
alpha = 1.5 * pi / 180
D = 110

def Cal_x(x):
    return np.tan(theta/2) * D + x * (1 - np.tan(alpha) * np.tan(theta/2))

def Next_x(x):
    return (x + np.tan(theta/2) * D) / (1 + np.tan(alpha) * np.tan(theta/2))

while p < 2 * 1852:
    x0 = Cal_x(p)
    q = Next_x(x0)
    dis = q - p
    if dis * 2 < pre_dis:
        print("OUT!")
    pre_dis = dis
    p = q - 0.1 * dis
    num += 1

print(num)