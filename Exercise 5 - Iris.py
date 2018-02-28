# Declan Reidy - Exercise 5 - 28-02-2018

# Please complete the following exercise this week. 

# Write a Python script that reads the Iris data set in and prints 
# the four numerical values on each row in a nice format. That is, 
# on the screen should be printed the petal length, petal width, sepal 
# length and sepal width, and these values should have the decimal places 
# aligned, with a space between the columns.

with open("data/iris.csv") as f:
  for line in f:
    
   print(line.split(",")[0],"",line.split(",")[1],"",line.split(",")[2],"",line.split(",")[3])
