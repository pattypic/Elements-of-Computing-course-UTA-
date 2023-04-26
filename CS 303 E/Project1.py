# File: Project1.py
# Student: Patrick Pichardo
# UT EID: pjp953
# Course Name: CS303E
# 
# Date: 02/25/2023
# Implementing the Rock, Paper, Scissors game in
# Rules:
# Rock beats scissors
# Scissors beats paper
# Paper beats rock
# If both players choose the same response, it is a draw (there is no winner).

import random

def main():
    # convers the play [1,2,3] into there respective choices. 
    def playName( play ):
        if play == '1':
            return 'rock'
        elif play == '2':
            return 'paper'
        elif play == '3':
            return 'scissors'
        else:
            return None
    
    # defines what a defeat is.
    def defeats( play1, play2 ):
        return ( play1 == '1' and play2 == '3' ) or ( play1 == '2' and play2 == '1' ) or ( play1 == '3' and play2 == '2' )

    # prints the game stats, takes the entire games played and divided it by whats being getting the percentage out of. looking at it now I can see something that can be changed but I'm too tired to change it since it still works. 
    def printStats( plays, wins, losses, draws ):
        games = wins + losses + draws
        if plays == 0:
            print("No games were completed.")
        else:
            print('Game statistics:')
            print('  Games played: {}'.format(plays))
            print('  You won:      {} ({:.1f}%)'.format(wins, 100*wins/games))
            print('  You lost:     {} ({:.1f}%)'.format(losses, 100*losses/games))
            print('  No winner:    {} ({:.1f}%)'.format(draws, 100*draws/games))

    # The machine chooses one of the three moves randomly. 
    def machinePlay ():
        play = random.choice(['1', '2', '3'])
        return play

    # This is what is actually running, if this was my own project I would put the definitions on another file and just import it pero no. 
    print("Welcome to a game of Rock, Paper, Scissors!")
    # Defining the varables
    plays = 0
    wins = 0
    losses = 0 
    draws = 0
    # Starting the loop. 
    while True:
        print()
        print('Choose your play:')
        print('  Enter 1 for rock;')
        print('  Enter 2 for paper;')
        print('  Enter 3 for scissors;')
        play = input('  Enter 4 to exit:')
        print()
        # starting the if statement that runs all the def fucitons above. 
        if play == '4':
            printStats(plays, wins, losses, draws)
            print('Thanks for playing. Goodbye!')
            break
        elif play not in ['1', '2', '3']:
            print('Illegal play entered. Try again!')
            continue
        else:
            plays += 1
            x = machinePlay()
            print("You played {}; your opponent played {}".format(
                    playName(play), playName(x)))
            if play == x:
                print("There's no winner. Try again!")
                draws += 1
            elif defeats(play , x):
                print("Congratulations, you won!")
                wins += 1
            else:
                print("Sorry, you lost!\n")
                losses += 1

if __name__ == "__main__":
    main()
