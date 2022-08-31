# Python program for word count

try:
    file = open('C:/Users/ASHWINKANNAN/OneDrive/Desktop/Demo text.txt', 'rt')
        
except FileNotFoundError:
    print("The file is not found in the specified directory")

else:
    contents = file.read()

    print("The content of a file is : ", contents)

    word = input("Enter a word to be searched : ")

    count = 0

    
    for sentence in contents.split():
        if(sentence == word):
            count += 1

    print(f"The word '{word}' is {count} times repeated")

finally:
    file.close()
