# Python program to remove an item from a tuple

tuples = tuple(input("Enter the tuple values : ").split(","))

lists = list(tuples)

item = input("Enter an item to be removed : ")

if(item in lists):
    lists.remove(item)
    tuples = tuple(lists)
    print(tuples)
else:
    print(f"The item '{item}' is not found in the tuple")
