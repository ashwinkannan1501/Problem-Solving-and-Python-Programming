# Python program to generate and print a list of first and last 5 elements where the values are
# the square of number between 1 and 20 (both included)

lists = []

for number in range(1, 21):
    if((number >= 1 and number <=5) or (number >= 15 and number <= 20)):
        lists.append(number ** 2)

print("List Values are : ", lists)
