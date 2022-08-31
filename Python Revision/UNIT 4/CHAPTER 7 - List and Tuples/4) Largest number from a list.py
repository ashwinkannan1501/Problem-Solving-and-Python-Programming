# Python program to get the largest number from a list

lists = list(input("Enter the list values : ").split(","))

new_list = []

for number in lists:
    new_list.append(int(number))

print("List values : ", new_list)

print("Largest element from a list : ", max(new_list))
