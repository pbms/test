# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 17:41:34 2017
@author: mwu
"""
#
def factors(n):
    global result
    result = set()
    for i in range(1, int(n ** 0.5) + 1):
        div, mod = divmod(n, i)
        if mod == 0:
            result |= {i, div}
    return result

number_of_factors = factors(441)
print(number_of_factors)
count = len(number_of_factors)
print(str(count))

def print_factors(x):
    print("The factors of",x,"are:")
    for i in range(1, x + 1):
       if x % i == 0:
           print(i)

num = 441
print_factors(num)