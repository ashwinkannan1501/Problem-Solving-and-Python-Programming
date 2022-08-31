# python program to get a list, sorted in increasing order by the last element in each tuple
# from a given list of non-empty tuples

def last(n):
    return n[-1]

lists = [(5, 6), (78, 59), (0, 1), (1, 0), (10, 2), (23, 45)]

lists.sort(key = last)
print(lists)
