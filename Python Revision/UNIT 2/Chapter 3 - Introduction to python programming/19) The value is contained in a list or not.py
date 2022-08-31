# Python program to check whether a specified value is contained in a group of values

list_items = input("Enter a list values : ").split(",")  # Get the list items from the user

number = input("Enter a number : ")  # Get the number value from the user

if number in list_items:  # Check if number is present in the list
    print(f"The number '{number}' is present in the list {list_items}")  # Print the result
else:  # If number is not present in the list
    print(f"The number '{number} is not present in the list {list_items}")  # Print the result
