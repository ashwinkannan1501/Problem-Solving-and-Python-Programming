# Python sorted() function
"""The sorted() function returns a sorted list from the given iterable. It is used to sorts the
elements of a given iterable in a specific order - Ascending (or) descending
SYNTAX : sorted(iterable, key, reverse)
         where iterable - sequence (string, tuple, list) or collection (set, dictionary, frozenset) or any iterator
               key (optional) - function that serves a key for the sort comparison
               reverse (optional) - If true, the sorted list is reversed (Descending order).
                                    By default it sets to false"""
list_elements = [50, 65, 48, 2, 0, 70, 52, 100, 6]
print(f'Sort of the list elements in ascending order is : {list(sorted(list_elements, reverse=False))}')
print(f'Sort of the list elements in descending order is : {list(sorted(list_elements, reverse=True))}')
