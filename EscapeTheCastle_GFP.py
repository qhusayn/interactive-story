# ----------------------------------------------------------------------------------
#                                ESCAPE THE CASTLE - COMPLETE GAME - Group Full Plan
# ----------------------------------------------------------------------------------
 
#Impoer 'random' module for random encounters
import random
 
# Shared game information
inventory = []
 
# ----------------------------------------------------------------------------------
#              INTRODUCTION - COPY DAY 2 CODE - Character Creation & Welcome Message
# ----------------------------------------------------------------------------------

def introduction():
   
    #Welcome the player
    print("--- ESCAPE THE CASTLE! ---")
    print("Welcome, adventurer!")

 
    #Get player name, age and character class
    playerName = input("What is your name? ")
    playerAge = int(input("How old are you? "))
    playerClass = input("Choose a character class: ")

   
    #Set starting values
    health = 100
    gold = 20
 

    #Display the character profile
    print("\n--- YOUR CHARACTER ---")
    print(f"Name: {playerName}")
    print(f"Age: {playerAge}")
    print(f"Class: {playerClass}")
    print(f"Health: {health}")
    print(f"Gold: {gold}")

 
    #Begin the story
    print(f"\n{playerName}, you wake up in a dark castle.")
    print("You hear footsteps approaching...")
    print("Your adventure is about to begin!")

introduction()


# ----------------------------------------------------------------------------------
#                                       ESCAPE THE CASTLE - SCENE 1: Escape The Cell
# ----------------------------------------------------------------------------------


# Define the Cell scene
def cell():
    print("\nYou wake up in a dark castle cell.")
    print("You can see a door, a window and an old bed.")

 
# Create a variable to track whether the player has found the key
    has_key = False

 
# Repeat while the player has not found the key
    while has_key == False:

 
# Ask the player what to investigate
        choice = input("\nInvestigate the door, window or bed? ").lower()
 
        if choice == "door":
            print("The door is locked.")
            print("You need to find a key")
 
        elif choice == "window":
            print("The window is barred. You can't escape that way.")
 
        elif choice == "bed":
            print("You look underneath the bed.")
            print("You find a small Iron Key")

 
# Add the key to the inventory
            inventory.append("Iron Key")

 
# Update the variable to stop the loop
            has_key = True
 
        else:
            print("Invalid choice. Please choose 'door', 'window', or 'bed'.")

 
# Code runs once the player has found the key.
    print("\nYou unlock the cell door.")
    print("You step out into the corridor.")
    print(f"Your inventory: {inventory}")
 

cell()



# ----------------------------------------------------------------------------------
#                                   CORRIDOR - COPY DAY 3/4 CODE - Enter The Corridor
# ----------------------------------------------------------------------------------



def corridor():
 
    # Introduce the scene
    print("You enter a long, dark corridor")
    print("You notice an old wooden cabinet")
    
    choice = input("Do you open the cabinet? yes/no: ")
    
    if choice == "yes":
        print("You open the cabinet")
        print("Inside, you find a Rusty Dagger!")
    
        inventory.append("Rusty Dagger")
    
        print("You pick up the dagger")
    
    elif choice == "no":
        print("You leave the cabinet closed.")
    
  
corridor()


# ----------------------------------------------------------------------------------
#                           RANDOM ENCOUNTER - COPY DAY 4 CODE - Encounter Creatures
# ----------------------------------------------------------------------------------


# Define the encounter function
def encounter():

    choice = ["Guard", "Ghost", "Rat"]
    from random import choice
    creature = choice(["Guard", "Ghost", "Rat"])
    print(f"\nA {creature} appears!")
 
    # Add selection to respond to the creature
    if creature == "Guard":
        print("The guard draws their sword!")
    elif creature == "Ghost":
        print("The ghost floats towards you!")
    elif creature == "Rat":
        print("the Rat wakes up and slowly walks towards you")

 
encounter()


# ----------------------------------------------------------------------------------
#                                                  LIBRARY - NEW SCENE - The Library
# ----------------------------------------------------------------------------------


def library():


    print("Like a little girl - you scream and run away, and enter the castle library. You see a desk, a bookshelf, and a door.")

    while True:
        choice = input("Check [desk], [bookshelf], or [leave]? ").lower()

        if choice == "desk":
            print("Just empty parchment and a broken quill.")
        elif choice == "bookshelf":
            print("You pull a red book and find a note: 'The password is DRAGON.' You think to yourself, 'That was bloody easy!'")
        elif choice == "leave":
            print("You head back to the library door.")
            break
        else:
            print("Invalid choice. Try again.")


library()


# ----------------------------------------------------------------------------------
#                                    CASTLE GATE - NEW SCENE - Sprinting to The Gate
# ----------------------------------------------------------------------------------

def castle_gate():
 
  print("\n--- THE CASTLE GATE ---")
  print("You sprint out of the library, down the corridor, and stand before a massive iron gate. A fancy Temu AI door lock says: 'Speak the secret word to pass.'")

  while True:
    password = input("\nEnter the password (or type 'back' to return): ").upper()

    if password == "DRAGON":
      print("\nThe heavy iron lock clicks open! You push the gate wide and run to freedom.")
      print("CONGRATULATIONS! You have escaped the castle!\n")
      break

    elif password == "BACK":
      print("You step away from the gate to search the castle again.")
      break

    else:
      print("Nothing happens. The gate remains locked. Try again!\n")


castle_gate()


# ----------------------------------------------------------------------------------
#                                                                          MAIN GAME
# ----------------------------------------------------------------------------------
 
def play_game():
 
    introduction()
    cell()
    corridor()
    encounter()
    library()
    castle_gate()
 
 
# Start the game
play_game()