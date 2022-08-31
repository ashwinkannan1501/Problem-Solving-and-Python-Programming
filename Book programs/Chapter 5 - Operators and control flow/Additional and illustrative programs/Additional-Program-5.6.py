# Python program for generating fibonacci series less than 200
print("----------------Fibonacci series--------------------------")
(a, b) = (0, 1)
while a < 200:
    print(a)
    (a, b) = (b, (a + b))

"""for i in range(12):
    print(b)
    (a, b) = (b, (a + b))"""

