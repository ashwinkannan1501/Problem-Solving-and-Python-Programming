# Python program that takes two list and returns True if they have at least one common member
def common_member(list_one, list_two):
    for x in list_one:
        for y in list_two:
            if x == y:
                return True
            else:
                return False


list_one = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
list_two = [[1, 2, 3, 4, 5], [5, 6, 7, 8, 9, 10]]
print(common_member(list_one, list_two))
