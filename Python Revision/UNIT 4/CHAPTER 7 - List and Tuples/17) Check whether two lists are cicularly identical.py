# Python program to check whether two list are circularly identical

list1 = [59, 36, 12, 78, 10, 0, 5, 9]
list2 = [10, 10, 0, 0, 10]
list3 = [10, 10, 10, 0, 0]

print("Compare list 1 and list 2 : ", ''.join(map(str, list2)) in ''.join(map(str, list1 * 2)))
print("Compare list 2 and list 3 : ", ''.join(map(str, list3)) in ''.join(map(str, list2 * 2)))
