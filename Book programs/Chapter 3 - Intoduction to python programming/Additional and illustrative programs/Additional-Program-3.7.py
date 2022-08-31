# Python program to display the first and last colors from the following list
colors = input("Enter the random colors : ")
list_elements = list(colors.split(","))
print(f'The list elements are {list_elements}')
print(f'The first color is {list_elements[0]}')
print(f'The last color is {list_elements[-1]}')
