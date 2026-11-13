# ==========================================
# ESCAPE THE CASTLE - SCENE 1: THE CELL
# ==========================================
 inventory = []

def cell():
    # Introduce the scene to the player
    print("You wake up in a dark castle cell.")
    print("You can see a door, a window and an old bed")

    while has_key == False:

        # Ask the player what they want to investigate
        # .lower() converts their answer to lowercase
        choice = input("Do you want to investigate the door, window or bed?: ").lower()
        
        # Check whether the player chose the door
        if choice == "door":
            print("You walk towards the door.")
            print("You try the handle, but is it locked.")
        
        # Check whether the player chose the window
        elif choice == "window":
            print("You look through the window.")
            print("It is too small to escape through")
        
        # Check whether the player chose the bed
        elif choice == "bed":
            print("You look under the bed")
            print("You find a small Iron Key")
            inventory.append("Iron Key")
            has_key = True
        
        else:
            print("You decide not to investigate")

#end region

# ==========================================
# ESCAPE THE CASTLE - SCENE 2: THE CORRIDOR
# ==========================================
 
# Create a list to store the player's inventory
# We are assuming the player already found the key
inventory = ["Iron Key"]
 
 
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
 
print(f"\n Your Inventory: {inventory}")

# Define a function with a creature parameter
def encounter(creature):
    print("You hear footsteps approaching...")
    print(f"A {creature} appears!")
    print("Prepare yourself!")
 
 
# Call the function with different arguments
encounter("Guard")
encounter("Ghost")
 
 
 
def encounter(creature):
 
    print(f"\nA {creature} appears!")
 
    # Add selection to respond to the creature
    if creature == "Guard":
        print("The guard draws their sword!")
 
    elif creature == "Ghost":
        print("The ghost floats towards you!")
    elif creature == "draugr":
        print("the draugr wakes up and slowly walks towards you")
# Test each possible encounter
encounter("Guard")
encounter("Ghost")
encounter("draugr")

# ==========================================
# ESCAPE THE CASTLE - CORRIDOR ENCOUNTER
# ==========================================

import random
 
# Define a function to describe an encounter
def encounter(creature):
 
        # Different outcomes depending on the creature
    if creature == "Guard":
        print("The Guard draws their sword")
    elif creature == "Ghost":
        print("The ghost floats towards")
    elif creature == "Sphinx":
        print("the Sphinx wakes up and slowly walks towards you")
 
    print(f"A {creature} appears!!")
 
# Define the corridor scene
def corridor():
    print("You walk down a dark castle corridor.")
    print("You hear a strange noise ahead...")
     # Create a list of possible encounters
    creatures = ["Guard", "Ghost", "Sphinx"]
   
    # Randomly select a creature
    random_creature = random.choice(creatures)
 
     # Pass the chosen creature into the encounter function
    encounter(random_creature)
 
# Start the scene
corridor()

