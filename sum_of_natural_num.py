# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 20:52:40 2020

@author: bhara_5sejtsc
"""

n = int(input("Enter a number: "))  
  
if n < 0:  
   print("Enter a positive number")  
else:  
   sum = 0  
   # use while loop to iterate un till zero  
   while(n > 0):  
       sum += n  
       n -= 1  
   print("The sum is",sum)  
		