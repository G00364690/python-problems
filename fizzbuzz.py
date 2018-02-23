# Declan Reidy - Fizzbuzz coding - 23-2-2018
# 
# https://en.wikipedia.org/wiki/Fizz_buzz

i = 1 

while i <= 100:
  if (i % 3 == 0) and (i % 5 == 0):
    print("Fizzbuzz")
  elif i % 3 == 0:
    print("Fizz")
  elif i % 5 == 0:
    print("Buzz") 
  else:
    print(i)
  i = i + 1

print("the final number is",i)
