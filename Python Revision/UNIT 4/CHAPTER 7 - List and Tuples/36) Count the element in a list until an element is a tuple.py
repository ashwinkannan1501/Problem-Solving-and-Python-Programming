# Python program to count the element in a list until an element is a tuple

num = [10,20,(30,40), 50, 60]
ctr = 0
for n in num:
    if(isinstance(n, tuple)):
        break
    ctr += 1
print(ctr)
