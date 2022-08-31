# Python program to print star pattern
# creating star pattern from a list
print("------------Star pattern from a list------------------ ")
star_pattern = [15, 5, 7, 1, 20, 40, 6, 9]
star_pattern = reversed(star_pattern)
for x in star_pattern:
    print("*" * x)

# Creating star pattern using for-in range() loop
print("------------Printing star pattern using for-in range() loop-----------------")
for i in range(1, 21):
    print("*" * i)

for i in range(19, 0, -1):
    print("*" * i)
