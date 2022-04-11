#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 16:50:25 2022

@author: dalya
"""

import time

start=time.time()
sum=0
for i in range(1,100000001):
    sum=sum+i
    
end=time.time()

print('1+2+...+100000000',sum)
print('time:', end-start,'end')