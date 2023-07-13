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

    while play_again:
        os.system("clear")
        # Print the Welcome Message
        print(f"\n\t\t\t\t{yellow}Welcome to Lost in the Woods\n")

        # Print the Back Story
        print(f"{green}You wondered away from your camp site and have become lost and are trying to find your way back.")
        print("Beware, there are obstacles in the way of a safe return. You have only three lives to try and make it back safely!\n")

        # The main loop of the game and continues until either the user runs out of lives or wins the game.
        while (lives_left > 0) and (not game_over):

            # Prompt user for initial direction to take and user comes back to this spot after each death
            direction_taken = input(f"{white}While walking the path you come to a fork, do you go ({blue}L{white})eft or ({blue}R{white})ight?> ")
            print("")

            if direction_taken.strip().upper() == "L":
                print(f"{green}You have chosen to take the path to the left.")
                print("You see an adorable white bunny sitting on the path.\n")

                # Will stay in this loop until the user choices correct responses
                while not correct_choice:

                    # Prompt the user on what to do with the bunny
                    bunny_choice = input(f"{white}Do you ({blue}P{white})et the adorable white bunny or go ({blue}A{white})round it?> ")

                    if bunny_choice.strip().upper() == "P":
                        print(f"\n{green}You have chosen to pet the bunny and it turns out to be the killer rabbit of Caerbannog!")
                        print(f"{red}You are now dead!\n")
                        lives_left -= 1
                        if lives_left == 1:
                            print(f"{green}You have only {red}one{green} life left, choose wisely!\n")
                        else:
                            print(f"{green}You have {red}{lives_left}{green} lives left!\n")
                        break
                    elif bunny_choice.strip().upper() == "A":
                        print(f"\n{green}You have chosen to go around the adorable bunny and stepped off the edge of a cliff!")
                        print(f"{red}You are now dead!\n")
                        lives_left -= 1
                        if lives_left == 1:
                            print(f"{green}You have only {red}one{green} life left, choose wisely!\n")
                        else:
                            print(f"{green}You have {red}{lives_left}{green} lives left.\n")
                        break
                    else:
                        print(f"{red}Invalid choice! {white} Please enter a {blue}P{white} to pet or {blue}A{white} to go around the bunny.\n")

            elif direction_taken.strip().upper() == "R":
                print(f"{green}You have chosen to take the path to the right.")
                print("You see a ferocious, snarling, 180lb Cane Corso blocking the path!\n")
            
                # Will stay in this loop until the user choices correct responses
                while not correct_choice:

                    # Prompt the user on what to do about the dog
                    dog_choice = input(f"{white}Do you ({blue}P{white})et the ferocious, snarling, 180lb dog or go ({blue}A{white})round it?> ")

                    if dog_choice.strip().upper() == "P":
                        print(f"\n{green}You have chosen to pet the ferocious, snarling, 180lb dog and it starts licking your hand!")
                        print("Cane Corsos crave affection and it escorts you along the path for protection!")
                        print("You make it safely back to camp with a new found friend for life!\n")
                        game_over = True
                        break
                    elif dog_choice.strip().upper() == "A":
                        print(f"\n{green}You have chosen to go around the ferocious, snarling, 180lb dog and it turns and shreds you to pieces!")
                        print(f"{red}You are now dead!\n")
                        lives_left -= 1
                        if lives_left == 1:
                            print(f"{green}You have only {red}one{green} life left, choose wisely!\n")
                        else:
                            print(f"{green}You have {red}{lives_left}{green} lives left!\n")
                        break
                    else:
                        print(f"{red}Invalid choice! {white}Please enter a {blue}P{white} to pet or {blue}A{white} to go around the dog.\n")
            else:
                print(f"{red}Invalid choice! {white}Please enter a {blue}L{white} for left or {blue}R{white} for right.\n")

        print(f"{blue}Game Over\n")
        again = input(f"{white}Do you want to play again? Enter {blue}Y{white} for Yes or anything else to exit> ")
        
        # User wants to play or not to play again
        if again.strip().upper() == "Y":
            lives_left = 3
            game_over = False
        else:
            play_again = False
            print(f"\n{blue}Goodbye!{white}\n")

if __name__ == "__main__":
    main()

