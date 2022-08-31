# Python program to test whether a passed letter is a vowel or not
vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
vowel_character = input("Enter a vowel character : ")
print(f'Vowel character({vowel_character}) inside vowel({vowel}) is : {vowel_character in vowel}')
