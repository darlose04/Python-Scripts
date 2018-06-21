# -*- coding: utf-8 -*-
"""
Created on Mon May 28 21:54:07 2018

@author: zsmit
"""

def factorial(num):
    '''
    recursion
    '''
    
    if num < 1:
        return 1
    else:
        answer = num * factorial(num-1)
        return answer
    
    '''
    non-recursion
    '''
    '''
    r = 1
    i = 1
    while i <= num:
        r *= i
        i += 1
    return r
    '''
print(factorial(10))