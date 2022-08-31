# Python program to find the maximum of three numbers

def maximum(first_number, second_number, third_number):
    result = max(first_number, second_number, third_number)
    return result


first_number = int(input("Enter the first number : "))
second_number = int(input("Enter the second number : "))
third_number = int(input("Enter the third number : "))

result = maximum(first_number, second_number, third_number)

print(f"The maximum of {first_number}, {second_number}, {third_number} is : {result}")
