# Aliasing list (copying)
"""1) Creating a list copy is called aliasing. When you create a copy, both list will have the same
memory locations. Changes in one list will affects the another list.
2) Aliasing refers to having different names for same list values
                        (or)
    When two identifiers refers to the same variable or value, it is known as aliasing."""

list_elements = list(input("Enter the list elements : ").split(","))
aliasing_list_elements = list_elements

print(f'List elements : {list_elements}')
print(f'Aliasing list elements : {aliasing_list_elements}')

# When you change in one list, it will also affectsthe another list
list_elements[1] = "reshma"
print(f'List elements : {list_elements}')
print(f'Aliasing list elements : {aliasing_list_elements}')
