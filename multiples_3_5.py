# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 00:22:00 2018

@author: zsmit
"""

def multiple_3_5():
    num_list = []
    for num in range(1,1000):
        if num % 5 == 0 or num % 3 == 0:
            num_list.append(num)
    print(num_list)
    print(sum(num_list))

multiple_3_5()
