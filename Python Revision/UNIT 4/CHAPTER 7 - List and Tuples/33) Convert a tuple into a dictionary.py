# 33) Python program to convert a tuple into a dictionary
tuples = ((1,'x'), (2,'y'))
print("Dictionary : ", dict((y,x) for (x, y) in tuples))
