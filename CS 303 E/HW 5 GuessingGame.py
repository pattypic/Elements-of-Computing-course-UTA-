# File: GuessingGame.py
# Student: Patrick Pichardo
# UT EID: pjp953
# Course: CS303E
#
# Date: 02/06/2023
# Description of Program: This is a guessing game, you input if you want to play or not then the game starts. Randomly creating a number for oyu to find. I don't kno whow much more I can say. 
import random

def main(initialAnswer = None):
    print("Welcome to the guessing game! Good luck!")
    while True:
        # I put lines in between most inputs to make thigs neater. 
        print("-----------------------------")
        ANS = input("Are you ready to play (Y/N):").lower()
        if ANS == 'y':
            if initialAnswer:
                thisGameAnswer = initialAnswer
            else:
                # For a while I forgot to put the .randint part of this code and I could not for the life of me figure out why my code wasn't working. 
                thisGameAnswer = random.randint(1, 999)
            print("-----------------------------")
            print("See if you can quess the 'Secret number'!")
            numG = 0
            while numG < 10:
                print("-----------------------------")
                guess = int(input("Enter an integer from 1 to 999: "))
# I spent like 30 minutes trying to figure out how to validate if the user didn't input an integer or not with out using a try block, and settled for using a list, but then realized it didnt have to check for that );
                if guess < 1 or guess > 999:
                    print("-----------------------------")
                    print("That's an illegal guess. Try again! You have", 10 - numG, "guesses left" )
                    continue
                if guess == thisGameAnswer:
                    print("-----------------------------")
                    print("Congratulations, you got it! you", numG + 1, "guesses!")
                    break
                elif guess < thisGameAnswer:
                    print("-----------------------------")
                    print("Your guess is too low. Try again! You have", 9 - numG, "guesses left.")
                else:
                    print("-----------------------------")
                    print("Your guess is too high. Try again! You have", 9 - numG, "guesses left.")
                numG += 1
            if numG == 10:
                print("-----------------------------")
                print("You didn't get it in 10 tries. The answer was", thisGameAnswer)
        elif ANS == 'n':
            print("-----------------------------")
            print("Well, come again later. Goodbye!")
            break 
        else:
            print("-----------------------------")
            print("Sorry, I didn't recognize your answer. Try again!")

if __name__ == "__main__":
    main()