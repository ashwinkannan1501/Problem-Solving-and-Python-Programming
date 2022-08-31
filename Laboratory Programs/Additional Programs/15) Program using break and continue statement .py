# Program using break and continue statement

number = int(input("Enter the number : "))
for i in range(1, number+1):
    if i == 3:
        continue
    elif i == 6:
        break
    print(i)
