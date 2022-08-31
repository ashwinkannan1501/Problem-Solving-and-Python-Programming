# Python program to find the common items from two lists

list1 = list(input("Enter the first list values : ").split(","))
list2 = list(input("Enter the second list values : ").split(","))

common_items = []

for i in list1:
    for j in list2:
        if(i == j):
            common_items.append(i)

print("Common items : ", common_items)
