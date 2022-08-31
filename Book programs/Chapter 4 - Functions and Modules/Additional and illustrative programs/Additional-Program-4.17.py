"""Python program that accepts a hyphen-separated sequence of words as input and prints the words
in a hyphen-separated sequence after sorting them alphabetically"""
words = input("Enter a multiple strings : ")
list_words = list(words.split("-"))
list_words.sort()
print("-".join(list_words))
