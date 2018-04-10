# Python Problems 2018
Python problems for GMIT module in Programming and Scripting as part of Higher Diploma in Data Analytics

## To use and test my various coding exercises:
1. Download & Install Anaconda
2. Launch Visual Studio Code
3. In repository follow syntax to identify various course exercises
4. Note all source code copied is declared in the open lines of the code

## The attached exercises have been created and refined several times over the past 10 weeks

1. Exercises 1 and 2 are submitted together and deal with the Fibonacci series assignments
    The basis of these submissions was to update existing code written by Ian McLoughlin to calculate various fibonacci outcomes as well as understand the concept of variables, strings and some basic commands in python. The resulting code is submitted here.
2. Exercise 3 is my proof of the Collatz conjecture
    The basis for this submission is the Collatz conjecture where you can reduce any integer to 1 following one of 2 steps depending on the state of the equation. Given that the solution requires that we continually apply one condition if the integer is even and another condition if the integer is odd, then initial investigation shows that the solution will revolve around an if statement. The program is improved by adding a user input, then assigning the input the name to call at the conclusion. The if statement is simply created by testing the state of the integer and applying 1 condition if the state of the integer is even and a different condition if the state of the equation is odd. Eventually the number 1 is reached, thus proving the Collatz conjecture to be true for the given input.
3. Exercise 4 is my solution to Euler problem 5
    The basis for this submission is Euler problem 5. This problem asks the programmer to calculate the lowest common multiple of the numbers (1,2,3,...,20). The problem states the lowest common multiple of the numbers (1,2,3,...,10) is 2520. Researching the problem and some critical thinking help to frame the problem at hand further. Any search for a solution can start at the number 2520 given its the lowest possible number to be divisible by both (1,2,3,...,10) and 20. Secondly the search for a solution can continue in increments of 20, given that any solution to the lowest common denominator of (1,2,3,...,20) would have to be divisible by 20. The next part of the solution is to test numbers starting at 2520 up to the factorial of 20 (which we know meets the criteria) in increments of 20 against a set of criteria. As soon as this criteria is met the loop should break and the result printed. The criteria is that the number being tested is itself tested that there is no remainder when divided by numbers (11,12,13,...,20). The solution is thus a for loop with an if and conditioned contained within. As an added functionality we can import the factorial function from math or indeed utilise the factorial function we've written for exercise 6 below.
4. Exercise 5 is my solution to the formatting exercise on the iris data file
    The basis for this submission is the iris data file compiled by Ronald Fisher. The task was to format the output in such a way as to make it readable. This is accomplished by insert spaces and align the data into 4 columns. The approach was to attempt to read a         file and then perform formatting on the contents in order to get the desired effect. The solution was created using the datafile as     the function and using a for loop function to apply the line.split() function to each data position in the string that constitutes       each row or line. Quickly the solution of adding spaces " ", or adding consistent number of character spaces for column alignment       (not required here based on the data set) becomes clear. Printing each line using the line.split() function applied to each data         position in the string [0] to [3] and spaces " " gives us the desired outcome.
5. Exercise 6 is my defined function to produce factorials
    The basis for this submission is the request to create a factorial function that will calculate the factorial of a given number by multiplying by every whole number less than it all the way down to 1. E.g. the factorial of 4 is 4x3x2x1 is 24. We also want this as a function that can be called at any time later. Once the problem is broken down into these terms the solution becomes simple to see that we need to apply a simple rule from 1 to an integer of our choice later. This rule is simply to start at 1 and multiply each test case from 1 to the integer by the running product of the previous numbers. Creating a function we can use "upto" as the varible representing the integer. The solution then quickly forms as a for loop from 1 to "upto+1" while tracking our running total of the product by muliplying each iteration by the previous product. Then output the result.
