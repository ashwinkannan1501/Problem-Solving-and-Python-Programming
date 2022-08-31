# Python program to generate and print a list except for the first 5 elements, where the values
# are square of numbers between 1 and 30 (both included)

lists = []

for number in range(1, 31):
    if(number > 5):
        lists.append(number ** 2)

print("The List values are : ", lists)
