# Python program to check whether two list list are circularly identical
list1 = [10, 10, 10]
list2 = [10, 10, 10]
print(f"Compare list1 and list2 : {''.join(map(str, list2)) in ''.join(map(str, list1 * 2))}")
