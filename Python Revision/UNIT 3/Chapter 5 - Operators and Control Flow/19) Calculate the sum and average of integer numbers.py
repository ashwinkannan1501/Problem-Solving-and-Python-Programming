# Python program to calculate the sum and average of n integer numbers

list_values = list(input("Enter the list values : ").split(","))

sum = 0

for number in list_values:
    sum = sum + int(number)

average = sum / len(list_values)

print("Sum : ", sum)
print("Average : ", average)
