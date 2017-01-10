'''This code will allow the user to play an adventurous game. '''

#Game begins by giving the user an introduction to the game. 
print ("Imagine being introduced to a new world called Zootopia.\nYou are foreign to the land,\n"
       "the people, and the food. As you are walking along a trail of beautiful greenery, something\n"
       "catches your eye.It is a pink, shiny object onthe path.Although it was found on the ground, it\n"
       "seems edible. What do you do? (Enter \"Y\" or \"N\")")

#First user input. 
pinkCandy = input()

if pinkCandy == ('N'):
    print ("Sorry, your character has died! If you had eaten the pink candy, you could have moved on! However, you did not.")

elif pinkCandy == ('Y'):
    print ("Great! The pink candy contained a rare potion that gives you 1000 units of energy to complete your journey!\n"
           "As you continue on your path, you run into a tree. The tree intrigues you with its uncommon appearance.\n"
           "Do you choose to climb it? Enter \"Climb!\" or \"No thanks!\"")

#Second user input. 
    treeClimb = input()

    if treeClimb == ("No thanks!"):
        print ("Uh oh!A bear has come your way looking for dinner, and you were the first thing in sight! Your character has died.")

    elif treeClimb == ("Climb!"):
        print ("Well done! You dodged a bear that was coming your way! And while you were at it, you found a dragon hiding in the tree.\n"
               "Do you choose to hop on and go for the ride? Enter \"I'd love to!\" or \"Uh,no.\"")

#Third user input. 
        dragonRide = input ()

        if dragonRide == ("Uh,no."):
            print ("Whoops, look like your time in this adventure has ended early.\n"
                    "A huge tornado knocked you out of the tree\n"
                    "You should've hopped on the dragon!")

        elif dragonRide == ("I'd love to!"):
                print ("Phew! That dragon just let you escape from the worst tornado. However, the dragon drops \n"
                       "you off in a dungeon! Hmm, you should have reconsidered trusting th dragon.All the doors are \n"
                       "locked and there's no way to get out! However, beneath a fallen brick, you find a piece of metal\n"
                       "that you might be able to use to unlock a door. Do you choose to pick it up? Enter \"Yes, please!\" \n"
                       "or \"No,I'm fine!\"")

#Fourth user input.
                metalPiece = input()

                if metalPiece == ("Yes, please!"):
                    print ("You are very unlucky. You picked up the piece of metal, and it just so happened\n"
                           "to have a virus on it. You fell sick, and as a result, you have died.")

                elif metalPiece == ("No, I'm fine!"):
                    print ("Thank god you didn't pick up the metal! You protected yourself from a deadly virus! You look around\n"
                           "and see a slightly open window. If you push hard enough, it looks like you might be able to open it\n"
                           "enough to jump out. If you jump out, you risk your life, but if you have a safe landing, you will be\n"
                           "fre. Do you jump? Enter \"Yes, I'll take my chances.\" or \"No, I'd rather be stuck in the dungeon.\"")

#Fifth user input. 
                    windowJump = input()

                    if windowJump == ("No, I'd rather be stuck in the dungeon."):
                        print ("Well, it's unfortunate that you chose to not jump. Due to the lack of food and water, you died.\n"
                               "Please try again!")

                    elif windowJump == ("Yes, I'll take my chances."):
                        print ("Good for you! You took your chances, and it was worth it! Not only did you land on a pile of pillows,\n"
                               "you also found 1000 gold coins waiting for you! Congratulations, you have won the game!")
                        
                    
'''The game has ended. The user will have won if they reached the end.'''
                


    
