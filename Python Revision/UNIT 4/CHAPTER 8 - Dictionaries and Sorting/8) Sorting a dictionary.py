# Python program to sort (ascending and descending) a dictionary by value

dictionary = {1:2, 3:4, 4:3, 2:1, 0:0}
print("Original Dictionary : ", dictionary)

ascending_sorting = sorted(dictionary.items(), reverse=False)
print("Sorting Dictionary in ascending order : ", ascending_sorting)

descending_sorting = sorted(dictionary.items(), reverse=True)
print("Sorting Dictionary in descending order : ", descending_sorting)
