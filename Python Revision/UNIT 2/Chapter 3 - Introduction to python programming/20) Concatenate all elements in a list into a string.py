# Python program to concatenate all elements in a list into a string

list_items = input("Enter a list items : ").split(",")  # Get the list items from the user

result = ''  # Define result as ''

for values in list_items:  # Loop the list items
    result += values  # Concatenate the values in the list items

print(f'The concatenation of {list_items} is : {result}')  # Print the result
