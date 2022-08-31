# Python programs which accepts a sequence of comma-separated numbers from user and generate a list and tuple

list_items = list(input("Enter the list values : ").split(","))  # Get the list of comma-separated values from the user and convert it into list

tuple_items = tuple(list_items)  # Convert the list items into tuple items

print("List Items : ", list_items)  # Print the list items
print("Tuple Items : ", tuple_items)  # Print the tuple items
