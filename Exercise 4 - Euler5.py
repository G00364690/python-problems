# Declan Reidy - 23-02-2018
#
# Updated with factorial function 03-03-2018
#
# Updated with factorial function 08-04-2018
#
# Euler problem 5 - Exercise 4
#
# 2520 is the smallest number divisible by all numbers 1 to 10

from math import factorial
i = 2520

for i in range(i,factorial(20),20):
    if (i % 20 ==0) and (i % 19 ==0) and (i % 18 ==0) and (i % 17 ==0) and (i % 16 ==0) and (i % 15 ==0) and (i % 14 ==0) and (i % 13 ==0) and (i % 12 ==0) and (i % 11 ==0):
      print("The smallest Euler number is:",i)
      break
