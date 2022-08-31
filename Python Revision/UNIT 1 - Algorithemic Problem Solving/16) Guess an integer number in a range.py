# Guess an integer number in a range

import random # Import a "random" module for number guessing game

# Sub-Program
def number_guess(): # Define a "number_guess" function 
    human = int(input("Guess a number between 1 to 10 : ")) # Taking int value as a input from the user

    CPU = random.randint(1, 10) # The 'randint()' function generates a pseudo-random number between 1 to 10

    print("Human Guess : ", human)
    print("CPU Guess : ", CPU)

    if(human == CPU): 
        print("Guess is correct") 
    else: 
        print("Guess is wrong") 

# Main Program
number_guess() # Calling the "number_guess()" function

while(True):
    play = input("Do you want to try again (Y/N) : ").upper() # Asking the user to play again 
    if(play == "Y"): 
        number_guess() 
    elif (play == "N"): 
        break
    else:
        print("Wrong Input !!! :(")
        
print("Thank you for playing this game!! ... :)") 
