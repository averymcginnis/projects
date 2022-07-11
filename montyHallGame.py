# This program allows the user to choose a door to open and attempt
# to beat the odds predicted by the Monty Hall problem.
#
# Author: Avery McGinnis

# Import the random module.
from random import *

# Explain how the game works.
print('\n Hello! Welcome to the Monty Hall Game. In this game, you\'ll choose '
      'one of three doors; only one door contains a prize.\n After you choose '
      'your door, one of the doors with no prize will be eliminated, leaving '
      'your door and one additional door.\n At that point, you can choose to switch '
      'doors or keep your original door. Try to win the prize! If you\'re'
      ' interested,\n research the Monty Hall Problem to get an understanding '
      'of the probabilities associated with the game.\n Have fun!\n')

# Ask the user for their name and begin the game.
name = input('What\'s your name? ')
play = input('Press enter to begin')
wins = 0
losses = 0

while play == "":

# Obtain the user's door choice.
    while True:
        try:
            firstChoice = int(input('Alright ' + name + ', go ahead and choose door 1, 2, or 3: '))
            if (firstChoice < 1) or (firstChoice > 3):
                    raise ValueError
        except ValueError:
            continue
        else:
            break

# Select the door that contains the prize.
    availableDoors = [1, 2, 3]
    prizeDoor = randint(1,3)
    #print('Prize door:',prizeDoor)

# Choose a door to eliminate.
    options = [1, 2, 3]
    options.remove(prizeDoor)
    if prizeDoor != firstChoice:
        options.remove(firstChoice)
    #print('List without firstChoice and prizeDoor:',options)

    num = len(options)
    if len == 2:
        eliminateDoor = choice([options[0],options[1]])
    else:
        eliminateDoor = options[0]
    #print('Door to eliminate:',eliminateDoor)

# Eliminate the door.
    availableDoors.remove(eliminateDoor)
    #print('Available doors:',availableDoors)

    if availableDoors[0] == firstChoice:
        otherDoor = availableDoors[1]
    else:
        otherDoor = availableDoors[0]
# Tell the user which door was eliminated.
    print('\nWe\'re going to eliminate door '+str(eliminateDoor)+'! Would you like to keep door',
         firstChoice,'or switch to door '+str(otherDoor)+'?')
    choice = input("\nEnter 'keep' to keep door "+str(firstChoice)+", enter 'switch' to switch to door "+str(otherDoor)+": ")

# Determine the user's final choice.
    if choice == 'keep':
        finalChoice = firstChoice
    elif choice == 'switch':
        finalChoice = otherDoor
    else:
    # Figure out the exception needed here.
        print('You did not follow instructions. Start over.')
        break
    #print('Final choice:',finalChoice)

# Determine if the user selected the correct door.
    if finalChoice == prizeDoor:
        print('\nCONGRATULATIONS! You won the prize!')
        wins = wins + 1
    else:
        print('\nSorry, you chose the wrong door.')
        losses = losses + 1

# Ask the user if they want to play again.
    play = input('Press enter to play again, type "stop" to stop playing: ')

else:
    if (wins == 0) & (losses == 0):
        print('')
    else:
        wp = wins/(wins + losses)
        print('\nYou won the prize ',round((wp*100),1),' percent of the time.')
        if wp > .666:
            print('You beat the odds predicted by the Monty Hall problem!')
        else:
            print('You didn\'t beat the odds predicted by the Monty Hall Problem.')


