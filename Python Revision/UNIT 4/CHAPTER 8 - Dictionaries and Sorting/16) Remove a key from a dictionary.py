# Python program to remove a key from a dictionary

dictionary = {1:10,2:20,3:30}
print("Old Dictionary : ", dictionary)
key = int(input("Enter a key : "))

if key in dictionary.keys():
    dictionary.pop(key)
    print("New Dictionary : ", dictionary)
    
else:
    print(f"The key '{key}' is not in the dictionary")
