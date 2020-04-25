# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 19:50:24 2020

@author: bhara_5sejtsc
"""

num = int(input("Enter a number: "))

if num == 0:
	print("Table does not exist")
else:
	for i in range(1,11):
		d = num * i
		print("%d * %d = %d"%(num,i,d))
	