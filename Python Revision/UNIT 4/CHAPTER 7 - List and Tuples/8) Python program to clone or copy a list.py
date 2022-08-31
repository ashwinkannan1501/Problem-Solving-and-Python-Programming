# Python program to clone or copy a list

original_list = list(input("Enter the list values : ").split(","))
cloned_list = original_list.copy()

print("Original List : ", original_list)
print("Cloned List : ", cloned_list)
print("Original_list == Cloned_list : ", original_list is cloned_list)
