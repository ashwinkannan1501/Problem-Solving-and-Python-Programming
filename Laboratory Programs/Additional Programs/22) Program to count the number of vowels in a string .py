# Program to count the number of vowels in a string

string = input("Enter a string : ")
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
count = 0
for character in string:
    if character in vowels:
        count += 1
print(f'The Number of vowels in a word is : {count}')
