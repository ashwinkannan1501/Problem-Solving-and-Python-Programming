# Python function program, that prints out the first n rows of pascal's triangle

from math import factorial

def pascal(row):
    
    for i in range(row):
        for j in range(row - i + 1):
 
            # for left spacing
            print(end=" ")
 
        for j in range(i + 1):
 
            # nCr = n!/((n-r)!*r!)
            print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
 
        # for new line
        print() 


row = int(input("Enter the number of rows:"))

pascal(row)
  

