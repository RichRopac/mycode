#!/usr/bin/env python3
"""A simple game to demonstrate the use of while loops and If Elif Else 
   statements for checking user input and reacting to that input"""

# Used to clear the screen
import os

def main():

    # Set up variables for text colors
    blue = "\033[1;34;40m"
    red = "\033[1;31;40m"
    green = "\033[1;32;40m"
    white = "\033[1;37;40m"
    yellow = "\033[1;33;40m"

    # Initialize the control variables for lives left, if the game is 
    # over, if correct input, and if user wants to play again
    lives_left = 3
    game_over = False
    correct_choice = False
    play_again = True

    #First loop for the entire game for initializing and playing again
    while play_again:
        
        # Clear the screen to begin
        os.system("clear")

        # Print the Welcome Message
        print(f"\n\t\t\t\t{yellow}Welcome to Lost in the Woods\n")

        # Print the Back Story
        print(f"{green}You wondered away from your camp site and have become "\
               "lost and are trying to find your way back.")
        print("Beware, there are obstacles in the way of a safe return. You " \
              "have only three lives to try and make it back safely!\n")

        # The second loop of the game and continues until either the user runs 
        # out of lives or wins the game.
        while (lives_left > 0) and (not game_over):

            # Prompt user for initial direction to take and user comes back to 
            # this spot after each death
            direction_taken = input(f"{white}While walking the path you come "\
                                    f"to a fork, do you go ({blue}L{white})eft"\
                                    f" or ({blue}R{white})ight?> ")
            print("")

            # Go to the left at the fork
            if direction_taken.strip().upper() == "L":
                print(f"{green}You have chosen to take the path to the left.")
                print("You see an adorable white bunny sitting on the path.\n")

                # Will stay in this loop until the user choices correct 
                # responses
                while not correct_choice:

                    # Prompt the user on what to do with the bunny
                    bunny_choice = input(f"{white}Do you ({blue}P{white})et "\
                                         f"the adorable white bunny or go "  \
                                         f"({blue}A{white})round it?> ")

                    # Pet the bunny
                    if bunny_choice.strip().upper() == "P":
                        print(f"\n{green}You have chosen to pet the bunny "\
                              "and it turns out to be the killer rabbit of "\
                              "Caerbannog!")
                        print(f"{red}You are now dead!")
                        lives_left -= 1
                        if lives_left == 1:
                            print(f"{green}You have only {red}one{green} "\
                                  "life left, choose wisely! Back to the fork!\n")
                        else:
                            print(f"{green}You have {red}{lives_left}{green} "\
                                  "lives left! Back to the fork!\n")
                        break
                    # Go around the bunny
                    elif bunny_choice.strip().upper() == "A":

                        print(f"\n{green}You have chosen to go around the "\
                              "adorable bunny and stepped off the edge of a cliff!")
                        print(f"{red}You are now dead!")
                        lives_left -= 1
                        if lives_left == 1:
                            print(f"{green}You have only {red}one{green} life "\
                                  "left, choose wisely! Back to the fork!\n")
                        else:
                            print(f"{green}You have {red}{lives_left}{green} "\
                                  "lives left! Back to the fork\n")
                        break
                    # Invalid entry for action with bunny
                    else:
                        print(f"\n{red}Invalid choice! {white} Please enter a "\
                              f"{blue}P{white} to pet or {blue}A{white} to "\
                              f"go around the bunny.\n")

            # Go to the right at the fork
            elif direction_taken.strip().upper() == "R":
                print(f"{green}You have chosen to take the path to the right.")
                print("You see a ferocious, snarling, 180lb Cane Corso blocking "\
                      "the path!\n")
            
                # Will stay in this loop until the user choices correct responses
                while not correct_choice:

                    # Prompt the user on what to do about the dog
                    dog_choice = input(f"{white}Do you ({blue}P{white})et the ferocious, "\
                                       f"snarling, 180lb dog or go ({blue}A{white})round it?> ")
                    
                    # Pet the dog
                    if dog_choice.strip().upper() == "P":
                        print(f"\n{green}You have chosen to pet the ferocious, snarling, "\
                              f"180lb dog and it starts licking your hand!")
                        print("Cane Corsos crave affection and it escorts you along the "\
                              "path for protection!")
                        print("You make it safely back to camp with a new found friend "\
                              "for life!\n")
                        game_over = True
                        break
                    # Go around the dog
                    elif dog_choice.strip().upper() == "A":
                        print(f"\n{green}You have chosen to go around the ferocious, "\
                              "snarling, 180lb dog and it turns and shreds you to pieces!")
                        print(f"{red}You are now dead!")
                        lives_left -= 1
                        if lives_left == 1:
                            print(f"{green}You have only {red}one{green} life left, "\
                                  f"choose wisely!\n")
                        else:
                            print(f"{green}You have {red}{lives_left}{green} lives left!\n")
                        break
                    # Invalid Entry
                    else:
                        print(f"\n{red}Invalid choice! {white}Please enter a {blue}P{white} "\
                              f"to pet or {blue}A{white} to go around the dog.\n")
            # Invalid Entry for going left or right at the fork           
            else:
                print(f"{red}Invalid choice! {white}Please enter a {blue}L{white} for left "\
                      f"or {blue}R{white} for right.\n")

        # Prompt user to play again
        print(f"{blue}Game Over\n")
        again = input(f"{white}Do you want to play again? Enter {blue}Y{white} for Yes or "\
                      f"anything else to exit> ")
        
        # User wants to play or not to play again
        if again.strip().upper() == "Y":
            lives_left = 3
            game_over = False
        else:
            play_again = False
            print(f"\n{blue}Goodbye!{white}\n")

if __name__ == "__main__":
    main()
