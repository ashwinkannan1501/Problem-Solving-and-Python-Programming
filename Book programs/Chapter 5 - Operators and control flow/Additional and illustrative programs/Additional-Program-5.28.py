# Python program to find the sum of series : 1 + 1/2 + 1/3 + ....... + 1/N
number = int(input("Enter the number of terms : "))
total = 0
for i in range(1, number+1, 1):
    total += 1/i  # (or) total = total + (1/i)
print(f'The sum of series when a number of terms({number}) is : {total}')
