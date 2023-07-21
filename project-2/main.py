#!/usr/bin/python3
"""Command Line Driving Game 
   a dictionary object"""

# Using os for clearing the screen
import os

# Where all the ASCII images are stored (e.g., maps, banner)
# color.py was imported in images and doesn't need to be in here to use
from images import *

def main():

    # Formatting variables
    tabs = "\t" * 5

    # Line separators
    stars = "*" * 68

    # Number of lives
    num_lives = 6

    # Dictionary for player and contains all vital information
    player = {
        "name" : "",
        "current_room" : "entrance",
        "maps" : {"entrance" : map_entrance, 
            "fouyer" : map_fouyer, 
            "library" : map_library, 
            "reception" : map_reception,  
            "living" : map_living, 
            "dining" : map_dining,
            "kitchen" : map_kitchen},
        "description" : {"entrance" : "You are standing on the Front Porch of Murder Manson and\n"
                         "\t    see nothing around you.", 
            "fouyer"    : "You are standing in the Fouyer and the front door has \n"
                          "\t    disappeared. You see a coat rack with a coat.", 
            "library"   : "You are standing in the Library and see a desk by the \n"
                          "\t    fireplace.", 
            "reception" : "You are standing in the Reception Room and see some\n"
                          "\t    armour over in the corner.",  
            "living"    : "You are standing in the Living Room and see a\n"
                          "\t    Hellhound by the Dining Room door.", 
            "living2"   : "You are standing in the Living Room and see a\n"
                          "\t    Cane Corso puppy running around playing.",
            "dining"    : "You are standing in the Dining Room and see a\n"
                          "\t    Ghoul by the Kitchen Door.",
            "dining2"   : "You are standing in the Dining Room and see\n"
                          "\t    bloody Ghoul pieces all over.",
            "kitchen"   : "You are standing in the Kitchen and see a locked\n"
                          "\t    cabinet with the words 'Open Me'."},
        "inventory" : [],
        "monsters" : [],
        "lives" : num_lives,
        "in-play" : True
     }
    # Print the initial banner
    os.system("clear")
    print(banner)
    input(f"{tabs}{red}Press any key to being......{white}")

    # Get the user name
    os.system("clear")
    name = input("What's your name?> ").strip().lower()
    if not name:
        print(f"\n{blue}You left the name field empty, so I will call you {green}Bob{white}.")
        name = "Bob"
        input("\nPress any key to continue......")

    # Assign the official formatted name
    player["name"] = name.capitalize()

    # Main loop for play
    play_again = "y"
    while play_again == "y":
        os.system("clear")
        print(player["maps"][player["current_room"]])
        print(blue + player["name"] +", here is your current scenario:")
        print(green + stars)
        if player["current_room"] == "living" and "hellhound" in player["monsters"]:
            print(blue + " Situation: " + green + player["description"]["living2"])
        elif player["current_room"] == "dining" and "ghoul" in player["monsters"]:
            print(blue + " Situation: " + green + player["description"]["dining2"])
        else:
            print(blue + " Situation: " + green + player["description"][player["current_room"]])
        print(blue + "      Room: " + green + player["current_room"].capitalize())
        print(blue + " Inventory: " + green + str(player["inventory"]))
        print(blue + "Lives Left: " + green + str(player["lives"]))    
        # Actions depending up which room the player is in
        match player["current_room"]:
            case "entrance":
                print(f"{blue}   Options: {green}1{blue}-Move into the House; "
                      f"{green}2{blue}-Refresh Screen; {green}3{blue}-Quit")
                print(green + stars)
                while True:
                    response = input(f"{white}Please enter the option number > ")
                    if str(response).strip() == "1":
                        player["current_room"] = "fouyer"
                        break
                    if str(response).strip() == "2":
                        break
                    if str(response).strip() == "3":
                        player["in-play"] = False
                        print(red+"You Are Dead!!!")
                        break
            case "fouyer":
                print(f"{blue}   Options: {green}1{blue}-Move into Reception Room; "
                      f"{green}2{blue}-Move into Library;\n\t    {green}3{blue}-Inspect Coat; "
                      f"{green}4{blue}-Refresh Screen; {green}5{blue}-Quit")
                print(green + stars)
                while True:
                    response = input(f"{white}Please enter the option number > ")
                    if str(response).strip() == "1":
                        player["current_room"] = "reception"
                        break
                    if str(response).strip() == "2":
                        player["current_room"] = "library"
                        break
                    if str(response).strip() == "3":
                        if "key" in player["inventory"]:
                            print(red + "Coat is empty, time to move on")
                            input(blue + "Press any key to continue....")
                        else:
                            os.system("clear")
                            print(player["maps"][player["current_room"]])
                            print(f"{blue}While inspecting the coat you find a key")
                            print(green + stars)
                            print(f"{blue}   Options: {green}1{blue}-Take Key; "
                            f"{green}2{blue}-Ignore Key")
                            print(green + stars)
                            while True:
                                response = input(f"{white}Please enter the option number > ")
                                if str(response).strip() == "1":
                                    player["inventory"].append("key")
                                    break
                                if str(response).strip() == "2":
                                    break
                        break
                    if str(response).strip() == "4":
                        break
                    if str(response).strip() == "5":
                        player["in-play"] = False
                        print(red+"You Are Dead!!!")
                        break

            case "library":
                print(f"{blue}   Options: {green}1{blue}-Move into Fouyer; "
                      f"{green}2{blue}-Inspect Desk; {green}3{blue}-Refresh Screen; "
                      f"\n\t    {green}4{blue}-Quit")
                print(green + stars)
                while True:
                    response = input(f"{white}Please enter the option number > ")
                    if str(response).strip() == "1":
                        player["current_room"] = "fouyer"
                        break
                    if str(response).strip() == "2":
                        if "bottle" in player["inventory"] or "hellhound" in player["monsters"]:
                            print(red + "Desk is empty, time to move on")
                            input(blue + "Press any key to continue....")
                        else:
                            os.system("clear")
                            print(player["maps"][player["current_room"]])
                            print(f"{blue}While inspecting the desk you find a bottle whose "
                                  "label says 'Just a Pup'")
                            print(green + stars)
                            print(f"{blue}   Options: {green}1{blue}-Take Bottle; "
                            f"{green}2{blue}-Ignore Bottle")
                            print(green + stars)
                            while True:
                                response = input(f"{white}Please enter the option number > ")
                                if str(response).strip() == "1":
                                    player["inventory"].append("bottle")
                                    break
                                if str(response).strip() == "2":
                                    break
                        break
                    if str(response).strip() == "3":
                        break
                    if str(response).strip() == "4":
                        player["in-play"] = False
                        print(red+"You Are Dead!!!")
                        break
            case "reception":
                print(f"{blue}   Options: {green}1{blue}-Move into Living Room; "
                      f"{green}2{blue}-Move into Fouyer;\n\t    {green}3{blue}-Inspect Armour; "
                      f"{green}4{blue}-Refresh Screen; {green}5{blue}-Quit")
                print(green + stars)
                while True:
                    response = input(f"{white}Please enter the option number > ")
                    if str(response).strip() == "1":
                        player["current_room"] = "living"
                        break
                    if str(response).strip() == "2":
                        player["current_room"] = "fouyer"
                        break
                    if str(response).strip() == "3":
                        if "sword" in player["inventory"] or "ghoul" in player["monsters"]:
                            print(red + "Armour has no value, time to move on")
                            input(blue + "Press any key to continue....")
                        else:
                            os.system("clear")
                            print(player["maps"][player["current_room"]])
                            print(f"{blue}While inspecting the armour you find a sword")
                            print(green + stars)
                            print(f"{blue}   Options: {green}1{blue}-Take Sword; "
                            f"{green}2{blue}-Ignore Sword")
                            print(green + stars)
                            while True:
                                response = input(f"{white}Please enter the option number > ")
                                if str(response).strip() == "1":
                                    player["inventory"].append("sword")
                                    break
                                if str(response).strip() == "2":
                                    break
                        break
                    if str(response).strip() == "4":
                        break
                    if str(response).strip() == "5":
                        player["in-play"] = False
                        print(red+"You Are Dead!!!")
                        break
            case "living":
                print(f"{blue}   Options: {green}1{blue}-Move into Dining Room; "
                      f"{green}2{blue}-Move into Reception Room;\n\t    {green}3{blue}-Fight; "
                      f"{green}4{blue}-Refresh Screen; {green}5{blue}-Quit")
                print(green + stars)
                while True:
                    response = input(f"{white}Please enter the option number > ")
                    if str(response).strip() == "1":
                        if "hellhound" in player["monsters"]:
                            player["current_room"] = "dining"
                        else:
                            print(red+"The Hellhound is blocking your path...deal with it")
                            input(blue + "Press any key to continue....")
                        break
                    if str(response).strip() == "2":
                        player["current_room"] = "reception"
                        break
                    if str(response).strip() == "3":
                        if "hellhound" in player["monsters"]:
                            print(red + "Hellhound is a pup with no threat, time to move on")
                            input(blue + "Press any key to continue....")
                        else:
                            os.system("clear")
                            print(player["maps"][player["current_room"]])
                            print(f"{blue}The Hellhound's mighty fangs took a chunk out of you;"
                                  "  1 life lost!!!")
                            player["lives"] -= 1
                            if player["lives"] == 0:
                                player["in-play"] = False
                                print(red+"You are out of lives, GAME OVER!!!")
                                input(blue + "Press any key to continue....")
                                break
                            print(f"{blue}You have {red}{player['lives']}{blue} lives left!!!")
                            print(green + stars)
                            if len(player["inventory"]) == 0:  
                                print(f"{blue}   Options: {green}1{blue}-Take him on by yourself; "
                                        f"{green}2{blue}-Run Away")
                                print(green + stars)
                                while True:
                                    response = input(f"{white}Please enter the option number > ")
                                    if str(response).strip() == "1":
                                        print(f"{blue}The Hellhound's mighty fangs took a "
                                              "chunk out of you; 1 life lost!!!")
                                        player["lives"] -= 1
                                        if player["lives"] == 0:
                                            player["in-play"] = False
                                            print(red+"You are out of lives, GAME OVER!!!")
                                            break
                                        input(blue + "Press any key to continue....")
                                        break
                                    if str(response).strip() == "2":
                                        player["current_room"] = "reception"
                                        break
                            else:
                                print(f"{blue}   Options: ", end="")
                                for x in range(len(player["inventory"])):
                                    print(f"{green}{x+1}{blue}-Use "
                                          f"{player['inventory'][x].capitalize()}", end="; ")
                                print (green+str((len(player["inventory"])+1))+blue+"-Run Away")
                                print(green + stars)
                                while True:
                                    response = input(f"{white}Please enter the option "
                                                     "number > ").strip()
                                    if str(response).strip() == str((len(player["inventory"])+1)):
                                        player["current_room"] = "reception"
                                        print(blue+"Moving you back to the Reception Room")
                                    elif player["inventory"][int(response)-1] == "bottle":
                                        player["monsters"].append("hellhound")
                                        player["inventory"].remove("bottle")
                                        print(blue+"The potion turned the Hellhound into a "
                                              "Cane Corso puppy!!!\n"
                                             "The room is clear of monsters!!!")
                                        #input(blue + "Press any key to continue....")
                                        #break
                                    else:
                                        print(f"{blue}The "
                                              f"{player['inventory'][int(response)-1].capitalize()}"
                                              f" didn't help! The Hellhound's mighty fangs took"
                                              f" a chunk out of you; 1 life lost!!!")
                                        player["lives"] -= 1
                                        if player["lives"] == 0:
                                            player["in-play"] = False
                                            print(red+"You are out of lives, GAME OVER!!!")
                                    input(blue + "Press any key to continue....")
                                    break
                        break
                    if str(response).strip() == "4":
                        break
                    if str(response).strip() == "5":
                        player["in-play"] = False
                        print(red+"You Are Dead!!!")
                        break
            case "dining":
                print(f"{blue}   Options: {green}1{blue}-Move into Kitchen; "
                      f"{green}2{blue}-Move into Living Room;\n\t    {green}3{blue}-Fight; "
                      f"{green}4{blue}-Refresh Screen; {green}5{blue}-Quit")
                print(green + stars)
                while True:
                    response = input(f"{white}Please enter the option number > ")
                    if str(response).strip() == "1":
                        if "ghoul" in player["monsters"]:
                            player["current_room"] = "kitchen"
                        else:
                            print(red+"The Ghoul is blocking your path...deal with it")
                            input(blue + "Press any key to continue....")
                        break
                    if str(response).strip() == "2":
                        player["current_room"] = "living"
                        break
                    if str(response).strip() == "3":
                        if "ghoul" in player["monsters"]:
                            print(red + "Ghoul is all chopped up so no threat, time to move on")
                            input(blue + "Press any key to continue....")
                        else:
                            os.system("clear")
                            print(player["maps"][player["current_room"]])
                            print(f"{blue}The Ghouls's mighty claws took a chunk out of you;"
                                  "  1 life lost!!!")
                            player["lives"] -= 1
                            if player["lives"] == 0:
                                player["in-play"] = False
                                print(red+"You are out of lives, GAME OVER!!!")
                                input(blue + "Press any key to continue....")
                                break
                            print(f"{blue}You have {red}{player['lives']}{blue} lives left!!!")
                            print(green + stars)
                            if len(player["inventory"]) == 0:
                                print(f"{blue}   Options: {green}1{blue}-Take him on by yourself; "
                                        f"{green}2{blue}-Run Away")
                                print(green + stars)
                                while True:
                                    response = input(f"{white}Please enter the option number > ")
                                    if str(response).strip() == "1":
                                        print(f"{blue}The Ghoul's mighty claws took a "
                                              "chunk out of you; 1 life lost!!!")
                                        player["lives"] -= 1
                                        if player["lives"] == 0:
                                            player["in-play"] = False
                                            print(red+"You are out of lives, GAME OVER!!!")
                                            break
                                        input(blue + "Press any key to continue....")
                                        break
                                    if str(response).strip() == "2":
                                        player["current_room"] = "living"
                                        break
                            else:
                                print(f"{blue}   Options: ", end="")
                                for x in range(len(player["inventory"])):
                                    print(f"{green}{x+1}{blue}-Use "
                                          f"{player['inventory'][x].capitalize()}", end="; ")
                                print (green+str((len(player["inventory"])+1))+blue+"-Run Away")
                                print(green + stars)
                                while True:
                                    response = input(f"{white}Please enter the option "
                                                     "number > ").strip()
                                    if str(response).strip() == str((len(player["inventory"])+1)):
                                        player["current_room"] = "living"
                                        print(blue+"Moving you back to the Living Room")
                                    elif player["inventory"][int(response)-1] == "sword":
                                        player["monsters"].append("ghoul")
                                        player["inventory"].remove("sword")
                                        print(blue+"The sword sliced the Ghoul into a "
                                              "lot of pieces!!!\n"
                                             "The room is clear of monsters!!!")
                                        #input(blue + "Press any key to continue....")
                                        #break
                                    else:
                                        print(f"{blue}The "
                                              f"{player['inventory'][int(response)-1].capitalize()}"
                                              f" didn't help! The Ghoul's mighty claws took"
                                              f" a chunk out of you; 1 life lost!!!")
                                        player["lives"] -= 1
                                        if player["lives"] == 0:
                                            player["in-play"] = False
                                            print(red+"You are out of lives, GAME OVER!!!")
                                    input(blue + "Press any key to continue....")
                                    break
                        break
                    if str(response).strip() == "4":
                        break
                    if str(response).strip() == "5":
                        player["in-play"] = False
                        print(red+"You Are Dead!!!")
                        break
            case "kitchen":
                print(f"{blue}   Options: {green}1{blue}-Move into Dining Room; "
                      f"{green}2{blue}-Try to Unlock Cabinet;\n")
                print(green + stars)
                while True:
                    response = input(f"{white}Please enter the option number > ")
                    if str(response).strip() == "1":
                        player["current_room"] = "dining"
                        break
                    if str(response).strip() == "2":
                        if "key" not in player["inventory"]:
                            print(red + "You don't have anything to unlock it with")
                            input(blue + "Press any key to continue....")
                            break
                        else:
                            os.system("clear")
                            print(f"{blue}After unlocking the cabinet with your key,\n"
                                  f"you find an orange basketball in it with the latin\n"
                                  f"words '{green}ludere pila{blue}' on it. You say the words out\n"
                                  f"loud and after a blinding flash of light, you find\n"
                                  f"yourself on a basketball court with 11 other players\n"
                                  f"waiting for you to throw them the ball\n")
                        player["in-play"] = False
                        print(red+"GAME OVER - Congratulations, You Won!!!\n")
                        break
        if player["in-play"] is False:
            # Game has concluded due to a win/loss and player can choose to play again.
            play_again = input(white+"Do you wish to play again?"
                              "("+blue+"Y"+white+"/n)> ").lower().strip()
            if play_again == "y":
                # Reset game control variables
                player["current_room"] = "entrance"
                player["lives"] = num_lives
                player["inventory"] = []
                player["monsters"] = []
                player["in-play"] = True
            else:
                os.system("clear")
                break

if __name__ == "__main__":
    main()

