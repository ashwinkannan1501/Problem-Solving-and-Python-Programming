# Python program to display the first and last colors from the list

# Get the colors list from the user (separated by comma)using "split()" function.
colors_list = input("Enter the colors list (seprated by comma): ").split(",")

print("Colors List : ", colors_list)  # Print the list
print("First color in the list is : ", colors_list[0])  # Print the first color from the list
print("Last color in the list is : ", colors_list[-1])  # Pint the last color from the list
