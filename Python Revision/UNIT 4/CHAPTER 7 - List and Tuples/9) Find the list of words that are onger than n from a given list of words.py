# Python program to find the list of words that are longer than n from a given list of words

string = input("Enter the string of words : ")
limit = int(input("Enter the limit : "))

lists = list(string.split(" "))
new_list = []

for word in lists:
    if(len(word) >= limit):
        new_list.append(word)

print(new_list)
        
