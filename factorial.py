# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 19:42:50 2020

@author: bhara_5sejtsc
"""

num = int(input("Enter a number: "))
factorial = 1

if num < 1:
	print("Factorial does not exist")
elif num == 0:
	print("Factorial is %d"%factorial)
else:
	for i in range(1,num+1):
		factorial = factorial*i
		print(factorial)
	
	  