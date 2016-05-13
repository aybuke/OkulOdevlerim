#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import time

def findNumberBinary(myArray, number):
    lower = 0
    upper = len(myArray)
    while lower < upper:
        x = lower + (upper - lower) // 2
        val = myArray[x]
        if number == val:
            return x
        elif number > val:
            if lower == x:
                break
            lower = x
        elif number < val:
            upper = x

def createArray(myArray, length):
    myArray = random.sample(range(1, 10000000), length)
    return myArray

length = int(input("Enter a array length:"))
myArray = []
createArray(myArray, length)
myArray = sorted(createArray(myArray, length))
number = int(input("Enter a number:"))
start_time=time.time()
print findNumberBinary(myArray, number)
print time.time()-start_time
