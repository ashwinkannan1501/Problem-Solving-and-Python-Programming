# Program that accepts a character string and character as arguments and deletes all the occurrences of this
# character in the string and display the result
def word(letters):
    character = input("Enter the character to delete : ")
    list_elements = list(letters)
    for i in list_elements:
        if i == character:
            list_elements.remove(i)
    print(list_elements)


letters = input("Enter the letters : ")
word(letters=letters)
