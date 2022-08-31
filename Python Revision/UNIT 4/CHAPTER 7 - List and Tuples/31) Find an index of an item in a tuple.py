# Python program to find the index of an item in a tuple

tuples = tuple(input("Enter the tuple values : ").split(","))
word = input("Enter the word : ")

if(word in tuples):
    print(f"The element '{word}' was found in the tuple at index '{tuples.index(word)}'")
else:
    print(f"The element '{word}' was not found in the tuple")
