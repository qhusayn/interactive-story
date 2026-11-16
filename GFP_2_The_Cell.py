# ------------------------------------------------
# CELL - COPY DAY 3/4 CODE - ESCAPE THE CELL SCENE
# ------------------------------------------------
 

    # TODO:
    # Copy your Cell scene here.
    #
    # Include:
    # - Door, window and bed choices
    # - While loop
    # - Finding the Iron Key
    # - Adding the key to inventory
    #
    # Remove any separate inventory = []
    # from your original scene.
 
# ==========================================
# ESCAPE THE CASTLE - SCENE 1: THE CELL
# ==========================================

import random
 
# SHARED GAME INFORMATION
inventory = []


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