# Square root of a number by newton's method


def newtons_sqrt(number):
    root = number / 2
    for i in range(10):
        root = (root + number / root) * 0.5
        return f"The Newton's square root of an {number} is : {root}"

number = int(input("Enter an integer number : "))

print(newtons_sqrt(number=number))

