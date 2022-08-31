# Python program to remove duplicates from a list

string_values = input("Enter the list values : ").title()
lists = list(string_values.split(","))

new_list = []

for item in lists:
    if(item not in new_list):
        new_list.append(item)
        
print(new_list)
        
