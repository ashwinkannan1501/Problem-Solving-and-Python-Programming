# Python program to count the number of even and odd numbers

limit = int(input("Enter a limit of a natural number : "))

array = []

for i in range(1, limit + 1):
    array.append(i)

print(array)

even_count = 0
odd_count = 0

for number in array:
    if(number % 2 == 0):
        even_count += 1
    else:
        odd_count += 1
else:
    print("No of even numbers : ", even_count)
    print("No of odd numbers : ", odd_count)
