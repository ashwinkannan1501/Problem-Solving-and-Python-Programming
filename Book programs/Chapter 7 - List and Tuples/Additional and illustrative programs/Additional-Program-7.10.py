# Python program to find the list of words that are longer than n from a given list of words
def words(list_words, number):
    for element in list_words:
        if len(element) > number:
            return list(element.split(" "))


list_words = input("Enter a statement : ")
list_words = list_words.split(" ")
number = int(input("Enter the minimum character : "))
print(words(list_words, number))
