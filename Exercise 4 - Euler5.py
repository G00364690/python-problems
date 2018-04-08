# Declan Reidy - 23-02-2018
#
# Updated with import math factorial function 03-03-2018
#
# Updated with defined factorial function 08-04-2018. Function defined for exercise 6 is more appropriate than using the import math function
#
# Euler problem 5 - Exercise 4
#
# 2520 is the smallest number divisible by all numbers 1 to 10

def factorial(upto): #defne factorial function
    product = 1
    for i in range(1, upto + 1): #perform operation for i values 1-20
      product = product * i #new product is given the value old product multiplied by i
    return (product)

i = 2520 #no need to start lower than 2520

for i in range(i,factorial(20),20): #every number divisible by 1-20 has to be divisible by 20. increments of 20 will find the solution quicker)
    if (i % 20 ==0) and (i % 19 ==0) and (i % 18 ==0) and (i % 17 ==0) and (i % 16 ==0) and (i % 15 ==0) and (i % 14 ==0) and (i % 13 ==0) and (i % 12 ==0) and (i % 11 ==0):
      print("The smallest number divisible by 1-20 is:",i)
      break
