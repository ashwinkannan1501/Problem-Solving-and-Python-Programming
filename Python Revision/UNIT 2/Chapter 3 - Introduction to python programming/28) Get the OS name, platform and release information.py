# Python program to get the OS name, platform and release information

import os  # import the "os" module
import platform  # Import the "platform" module

print("Operating System : ", os.name)  # Print the OS name using "os.name" function
print("Platform : ", platform.system())  # Print the OS Platform using "platform.system()" function
print("Release : ", platform.release())  # Print the OS release using "platform.release()" function
