# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 14:47:16 2023

@author: ushop
"""
import numpy as np
import math

# 利用相似计算已测量的区域
def Cal_S(len,p,l,s):           
    return ((len+p)/l)**2*s

# 累加前六个区域的计算结果
Area_lens = [14159, 58291, 82189, 9821, 60068, 10161];
total_lens = sum(Area_lens)
print(total_lens) 

# 计算漏测面积百分比
S2 = (2759.3-2673.9)*(3067.96-0)
print(S2)
S3 = (2170-2156.2)*(7482.83-0)
print(S3)
S4 = (982.12-839.0872)*(3067.96-0)
print(S4)

xh1=4875.0; yh1=987.94;
x0=7408;y0=0;
l1 = math.sqrt((x0 - xh1)**2 + (y0 - yh1)**2)
Sk1 = (7408-4489.7)*7482.83/2
len1 = 1359.4
q1 = 1306.1
S1 = Cal_S(len1,q1,l1,Sk1)
S1 = Sk1-S1
print(S1)

S5 = 0

xh6 = 403.15; yh6 = 7579.5;
x9 = 0; y9 = 9260;
l6 =  math.sqrt((x9 - xh6)**2 + (y9 - yh6)**2)
len6 = 864.07
Sk6 =(9260-7482.83)*7483.2/2
q6 = 672.63
S6 = Cal_S(len6,q6,l6, Sk6)
S6 = Sk6-S6
print(S6)

S_tol = 7408*9260
SS = S1+S2+S3+S4+S5+S6
# print(SS)

Rate = SS/S_tol
print(Rate)

# 不存在重复率超过20%的布线
Cl = 0