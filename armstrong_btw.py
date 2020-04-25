# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 20:41:47 2020

@author: bhara_5sejtsc
"""

lower = int(input("Enter a lower number: "))
upper = int(input("Enter upper number: "))

for n in range(lower,upper+1):
	sum = 0
	temp = n
	while temp > 0:
		digit = temp % 10
		sum += digit**3
		temp //= 10
	    if n == sum:
			print(n)

   
		