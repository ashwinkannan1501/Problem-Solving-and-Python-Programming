# Python Program to convert the temperature in celsius to fahrenheit and vice versa
temperature_celsius = float(input("Enter the temperature in celsius : "))
temperature_fahrenheit = float(input("Enter the temperature in fahrenheit : "))
fahrenheit = (temperature_celsius * 1.8) + 32
celsius = (temperature_fahrenheit - 32) * 1.8
print(f'The temperature in celsius({temperature_celsius}) to fahrenheit -> {fahrenheit}')
print(f'The temperature in fahrenheit({temperature_fahrenheit}) to celsius -> {celsius}')
