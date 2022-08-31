"""continue statement - The continue statement in python returns the control to the beginning of the loop"""
"""Python program using continue control statement to print numbers"""
number = int(input("Enter a random number : "))
print("The elements are : ")
for random_number in range(1, number+1):
    if number // 2 == random_number:
        continue
    print(random_number)

