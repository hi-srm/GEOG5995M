# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 10:55:41 2022

@author: gysmo
"""

import random


#random.seed(0)
r = random.random()
print(r)
r2 = random.randint(0,5)
print(r2)

y0 = 50
x0 = 50
y1 = 40
x1 = 40


if random.random() < 0.5:
    y0 = y0 + 1
else:
    y0 = y0 - 1
    
if random.random() < 0.5:
    x0 = x0 - 1
else:
    x0 = x0 + 1
    
print("y0",y0)
print("x0",x0)

if random.random() > 0.5:
    y1 = y1 + 1
else:
    y1 = y1 - 1
    
    
if random.random() < 0.5:
    x1 = x1 - 1
else:
    x1 = x1 + 1
    
print("y1",y1)
print("x1",x1)

x0 = y0 = 0
x1 = -3
y1 = -4
y_diff = (y0 - y1)
y_diffsq = y_diff * y_diff
x_diff = (x0 - x1)
x_diffsq = x_diff * x_diff
sum2 = y_diffsq + x_diffsq
answer = sum2**0.5
print(answer)


# if(random.randint(0,1) ==0):
#     x0 = x0 + 1
# else:
#     x0 = x0 - 1
    
# print("x0",x0)
    