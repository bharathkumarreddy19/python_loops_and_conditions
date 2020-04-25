# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 20:41:47 2020

@author: bhara_5sejtsc
"""

n = int(input("Enter a number: "))  
sum = 0  
temp = n  
  
while temp > 0:  
   digit = temp % 10  
   sum += digit ** 3  
   temp //= 10  
  
if n == sum:  
   print(n,"is an Armstrong number")  
else:  
   print(n,"is not an Armstrong number")  
   
		