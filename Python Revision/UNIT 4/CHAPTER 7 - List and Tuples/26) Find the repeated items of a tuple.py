# Python programs to find the repeated items of a tuple

tuples = tuple(input("Enter the tuple values : ").split(","))
lists = []; new_list = []

for item in tuples:
    total = tuples.count(item)
    if(total > 1):
        lists.append(int(item))

for element in lists:
    if(element not in new_list):
        new_list.append(element)
        
print('The repeated items in a tuple is : ', new_list)

