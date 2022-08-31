# Python program that will accept the base and height of a triangle and compute the area

height = int(input("Enter the height value : "))  # Get the height value from the user

base = int(input("Enter the base value : "))  # Get the base value from the user

area_of_triangle = (height * base) / 2  # Calculate the "area of a triangle" by using it's formula

print(f"Area of triangle of height '{height}' and base '{base}' is : '{area_of_triangle}'")  # Display the result
