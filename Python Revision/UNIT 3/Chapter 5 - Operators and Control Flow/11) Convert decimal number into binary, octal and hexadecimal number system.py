# Python program to convert decimal number into binary, octal and hexadecimal number system

decimal = int(input("Enter a decimal number : "))

binary = bin(decimal)
octal = oct(decimal)
hexadecimal = hex(decimal)

print("Decimal : ", decimal)
print("Binary : ", binary)
print("Octal : ", octal)
print("Hexadecimal : ", hexadecimal)
