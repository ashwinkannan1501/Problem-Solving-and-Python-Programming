# Python program to print a specified list after removing the 0th, 4th and 5th elements

lists = list(input("Enter the list values : ").split(","))

if(len(lists) >= 7):
    for index in range(len(lists)):
        if(index == 0 or index == 4 or index == 5):
            del lists[index]
    else:
        print("List values : ", lists)

else:
    print("The length of the list must be 7 or above")
