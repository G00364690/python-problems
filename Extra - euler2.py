# Declan Reidy - 03-03-2018 - Euler Problem 2

# By considering the terms in the Fibonacci sequence whose values 
# do not exceed four million, find the sum of the even-valued terms.

# source fib(n) - Ian McLoughlin fibname.py exercise 2

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

# Test the function with the following value.
# z = 4
# ans = fib(z)
# print("Fibonacci number", z, "is", ans)

x = 0
sum = 0
limit = 4000000

while fib(x) <= limit:

    if (fib(x) % 2 == 0):
      sum = sum + fib(x)
    x = x + 1

print("The sum of the even valued terms is:",sum)
