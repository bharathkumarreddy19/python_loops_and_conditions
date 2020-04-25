# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 19:56:27 2020

@author: bhara_5sejtsc
"""

def fibonacci(n):
	if n <= 1:
		return n
	else:
		return (fibonacci(n-1)+fibonacci(n-2))
	 
nterms = int(input("Enter: "))
	 
if nterms <= 0:
	 print("Please enter a positive number")
else:
	 for i in range(nterms):
		  print(fibonacci(i))