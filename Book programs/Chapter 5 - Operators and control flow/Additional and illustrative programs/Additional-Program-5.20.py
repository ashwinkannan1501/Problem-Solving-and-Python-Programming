# Python program that prints all the numbers from 0 to 6 except 3 and 6
for i in range(6+1):
    if (i != 3) and (i != 6):
        print(i)
    else:
        continue

""" (or)
for i in range(6+1):
    if (i == 3) aor (i == 6):
        continue
    else:
        print(i)
        
        (Both implementation gives the same answers)
"""
