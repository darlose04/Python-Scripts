# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 21:39:40 2018

@author: zsmit
"""


# count evens

def count_evens(nums):
    count = 0
    for item in nums:
        if item % 2 == 0:
            count += 1
    return count


print(count_evens([1, 2, 3, 4, 5, 6]))
