# Python program to get the 4th element and the 4th element from the last of tuple

tuples = tuple(input("Enter the tuple values : ").split(","))

if(len(tuples) >= 4):
    print("4th element is : ", tuples[3])
    print("-4th element is : ", tuples[-4])
else:
    print("The length of the tuple must be atleast 4")
