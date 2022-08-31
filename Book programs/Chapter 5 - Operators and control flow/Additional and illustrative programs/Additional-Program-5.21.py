# Python program using pass statement to print letters from a word
list_element = list(input("Enter a list word : "))
for letter in list_element:
    if letter == list_element[2]:
        print(f'The element {list_element[2]} is passed')
        pass
    else:
        print(letter)
