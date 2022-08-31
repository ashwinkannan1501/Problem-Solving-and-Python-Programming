# Python script to generate and print a dictionary that contains a number (between 1 and n) in
# the form (x, x*x)

n = int(input("Enter a number limit : "))
dictionary = {}

for key in range(1, n+1):
    dictionary[key] = key * key

print("Dictionary : ", dictionary)
