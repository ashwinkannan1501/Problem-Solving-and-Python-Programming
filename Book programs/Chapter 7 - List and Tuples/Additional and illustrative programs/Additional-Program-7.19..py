# Python program to generate all the sub-list of a list
def sub_list(my_list):
    subset = [[]]
    for i in range(len(my_list)):
        n = i+1
        while n <= len(my_list):
            sub = my_list[i:n]
            subset.append(sub)
            n += 1
            return subset


list1 = [10, 20, 30, 40]
list2 = ["x", "y", "z"]
print(f"Sub List of list 1 : {sub_list(list1)}")
print(f'Sub list of list 2 : {sub_list(list2)}')
