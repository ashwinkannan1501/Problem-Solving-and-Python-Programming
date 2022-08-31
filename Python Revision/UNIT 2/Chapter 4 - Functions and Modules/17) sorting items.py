# Python program that accepts a hyphen-seprated sequence of words as input and prints the word
# in a hyphen-separated sequence after sorting them alphabetically

def sort(items):
    items.sort()
    return items


items = [n for n in input().split("-")]

sort(items)

print("-".join(items))
