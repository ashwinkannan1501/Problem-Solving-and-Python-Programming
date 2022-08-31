# Example - 3
"""Python program to find the sum of natural numbers up to n using recursive function"""


def sum_of_natural_numbers(natural_number):
    if natural_number == 1:
        return natural_number

    else:
        return natural_number + sum_of_natural_numbers(natural_number - 1)


natural_number = int(input("Enter a natural number : "))
result = sum_of_natural_numbers(natural_number)
print(f'The sum of a number {natural_number} is : {result}')
