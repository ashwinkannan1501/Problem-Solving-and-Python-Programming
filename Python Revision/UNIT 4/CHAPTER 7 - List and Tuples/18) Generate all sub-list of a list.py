# Python program to generate all sub-lists of a list

lists = list(input("Enter the list values : ").split(","))
sublist = [[]]

for i in range(len(lists) + 1):
    for j in range(i):
        sublist.append(lists[j:i])
print(sublist)
