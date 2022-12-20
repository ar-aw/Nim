"""
Arika Awan
date: nov 13
desc: a game of nim against the computer
"""
#import random module
import random

#declare variables
total = 0

def drawStones():#the starting number of stones
    return random.randint(15,30)

def isValidEntry(takenStones,totStones): #checks for user's valid entry
    while takenStones > totStones:
        takenStones = int(input("That's too much, please try again: "))
    
def userTurn(totStones): #user's turn
    
    #make sure input is a number
    try:
        #user input
        inputStones = int(input(f"There are {totStones} stones. How many would you like?(1-3) "))
        
        
        #make sure number is between 1-3, prompt again if not
        while (inputStones < 1 or inputStones > 3):
            inputStones = int(input("Number must be between 1 and 3. Pick some stones: "))
        
    except:
        #if the input isn't a number, prompt for input again
        inputStones = int(input("That's not a number, try again. "))

    #check for valid entry
    isValidEntry(inputStones,totStones)
    #remove the user input stones from the total amount of stones left
    totStones = totStones - inputStones
    print(f"there are {totStones} stones left.")
    
    return totStones

def compTurn(totStones):
    
    #computer's turn is random from 1-3
    if (totStones > 3):
        take = random.randint(1,3)
        totStones = totStones - take
        print(f"The computer takes {take} stones.")
    #check for valid input once the total amount of stones is less than or equal to three
    elif (totStones <= 3):
        #make sure computer doesnt try to take more stones than there are
        try:
            take = random.randint(1,totStones)
            totStones = totStones - take
            print(f"The computer takes {take} stones.\n")
        #if it tries to, that means it is tryin to gp past the zero the player set, meaning player won
        except ValueError:
            print("you win!")

        
    return totStones


total = drawStones()

print("Welcome to Nim\n")
while (total>0):
    total = userTurn(total)
    total = compTurn(total)


