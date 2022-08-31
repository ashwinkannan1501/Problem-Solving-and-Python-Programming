# Python Program to get the OS name, platform and release information
from os import name
from platform import system, release
print(f'Name of the OS : {name}')
print(f'Platform of the OS : {system()}')
print(f'Release of the OS({system()}) : {release()}')
