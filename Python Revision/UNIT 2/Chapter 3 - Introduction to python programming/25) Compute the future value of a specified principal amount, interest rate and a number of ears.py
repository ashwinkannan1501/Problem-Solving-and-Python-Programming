# Python program to compute the future value of a specified principal amount, interest rate and a number of years

principal_amount = float(input("Enter the principal amount : "))  # Get the principal amount from the user

interest_rate = float(input("Enter the interest rate : "))  # Get the interest rate from the user

years = int(input("Enter the number of years : "))  # Get the number of years from the user

future_value = principal_amount * (
            (1 + (0.01 * interest_rate)) ** years)  # Calculate the "future value" by using the formula

print("Future Value is : ", round(future_value, 2))  # Print the round of "future value"
