#!/usr/bin/python
# -*- coding: utf-8 -*-

"""myArray: entered ordered array"""
"""number: searched number in myArray"""

def findNumber(number, myArray):
    for i in range(len(myArray)):
	if number == myArray[i]:
	    return i

myArray = [1,2,3,4]

number = int(input("Enter a number:"))
print findNumber(number, myArray)
