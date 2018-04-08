# Declan Reidy - Exercise 3 - 23-02-2018
# 
# Collatz conjecture program - https://en.wikipedia.org/wiki/Collatz_conjecture

n = int(input("Please enter an integer: "))
x = n #assign n to x so we can call it later without confusion

while n >= 2: #so long as n is not less than 2

  if n % 2 == 0: #test if n mod 2 is equal to 0
    n = n/2 #if true divide n by 2
    print(int(n))
  else:
    n = (n*3)+1 #if not true multiply by 3 and add 1.
    print(int(n))
  
print("Declan has proven the Collatz conjecture holds for the number", x) #x called
