# Declan Reidy - 24/3/18 - Factorial Function

# Please complete the following exercise this week. Write a Python 
# script containing a function called factorial() that takes a single 
# input/argument which is a positive integer and returns its factorial. 
# The factorial of a number is that number multiplied by all of the 
# positive numbers less than it. For example, the factorial of 5 is 
# 5x4x3x2x1 which equals 120. You should, in your script, test the 
# function by calling it with the values 5, 7, and 10.


def factorial(upto):
    product = 1
    for i in range(1, upto + 1):
      product = product * i
    return (product)
print("The factorial of the input is",factorial(5))
print("The factorial of the input is",factorial(7))
print("The factorial of the input is",factorial(10))
