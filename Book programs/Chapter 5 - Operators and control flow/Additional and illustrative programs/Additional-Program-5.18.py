# Python Program to count the number of even and odd numbers
def number_value(number):
    even_count = 0 ; odd_count = 0
    for i in range(1, number+1):
        if i % 2 == 0:
            print(f'The number {i} is an even number')
            even_count += 1
        else:
            print(f'The number {i} is an odd number')
            odd_count += 1
    print(f"There are {even_count} even numbers and {odd_count} odd numbers")


number = int(input("Enter a number : "))
number_value(number)
