# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 19:20:16 2020

@author: bhara_5sejtsc
"""

lower = int(input("Enter lower range: "))  
upper = int(input("Enter upper range: "))  
  
for num in range(lower,upper + 1):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           print(num)  