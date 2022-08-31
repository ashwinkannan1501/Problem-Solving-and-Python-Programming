# Histogram

pattern = input("Enter the pattern that you want to draw : ")
limit = int(input("Enter the limit : "))

print(f"Print '{pattern}' pattern in ascending order")
for i in range(1, limit+1):
    print(pattern * i)

print(f"Print '{pattern}' pattern in descending order")
for j in range(limit, 0, -1):
    print(pattern * j)

lists = list(input("Enter the list items : ").split(","))
list_items = []
for value in lists:
    list_items.append(int(value))

print(f"Print '{pattern}' pattern in array order")
for k in list_items:
    print(pattern * k)
