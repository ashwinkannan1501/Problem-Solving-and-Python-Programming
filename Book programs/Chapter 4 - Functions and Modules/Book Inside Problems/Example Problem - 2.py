# Calling a function
def person_details(name, age, gender):  # Function definition
    if gender == "Male":
        print(f'Hello Mr.{name}')
    else:
        print(f'Hello Mrs.{name}')
    print(f'Your age is : {age}')
    print(f'You are an {gender}')


name = input("Enter your name : ")
age = int(input("Enter your age : "))
gender = input('Enter your gender : ')
person_details(name, age, gender)  # Function call
