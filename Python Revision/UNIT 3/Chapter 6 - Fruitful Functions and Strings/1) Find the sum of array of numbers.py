# Python program to find the sum of array of numbers

array = list(input("Enter the array values : ").split(","))

total = 0

for value in array:
    total += int(value)

print(f"The sum of {array} is : {total}")
        
