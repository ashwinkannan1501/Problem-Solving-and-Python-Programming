# Python program to work with list

list_values = list(input("Enter the list values : ").split(","))

print("list_values[0] = ", list_values[0])
print("list_values[-1] = ", list_values[-1])

print("list_values[1:2] = ", list_values[1:2])

list_values.sort()
print("Sorted List : ", list_values)
