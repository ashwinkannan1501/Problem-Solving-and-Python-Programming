# Python function that takes two lists and returns True if they have atleast one common member

def common_member(list1, list2):
    for x in list1:
        for y in list2:
            if(x == y):
                return True
            else:
                return False

list1 = list(input("Enter the first list values : ").split(","))
list2 = list(input("Enter the second list values : ").split(","))

print(common_member(list1, list2))
