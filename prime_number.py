# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 19:16:48 2020

@author: bhara_5sejtsc
"""

def isprime(n):
	n = int(input("Enter a number: "))
	if n<=1:
		return False
	
	for i in range(2,n):
		if (n%i==0):
			return False
		else:
			return True
		
if isprime(n):
	print("True")
else:
	print("False")
			
		