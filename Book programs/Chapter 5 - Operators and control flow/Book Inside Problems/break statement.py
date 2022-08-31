"""break statement - The break statement brings control out of loop"""
"""Python program using break statement"""
random = int(input("Enter a random number : "))
print("The numbers are : ")
for random_number in range(1, random+1):
    if random_number == 5:
        break
    else:
        print(random_number)
