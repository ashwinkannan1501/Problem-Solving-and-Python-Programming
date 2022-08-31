# Python program to count the number 4 in a list

list_items = input("Enter the list values : ").split(",")  # Get a list items from the user

count = 0  # Initialize count as 0

for number_of_counts in list_items:  # Loop the items in the list
    if number_of_counts == '4':  # Check if the number '4' is in the list
        count += 1  # Assign it to the "count" variable

print(f"The number 4 in a list is {count} times repeated")  # Print the "count" value
