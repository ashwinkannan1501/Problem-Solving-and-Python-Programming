# 20) Python program that prints all the numbers from 0 to 6 except 3 and 6

for number in range(7):
    if(number == 3 or number == 6):
        continue
    
    print(number)
