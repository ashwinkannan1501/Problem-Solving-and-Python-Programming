# Python program to find the common items from two lists
color1 = ["Red", "Green", "Blue", "White"]
color2 = ["Black", "Green", "Red"]
print(f"Color 1 : {color1}")
print(f'Color 2 : {color2}')
print(f"Common colors are : {set(color1) & set(color2)}")