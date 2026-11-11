# ==========================================
# ESCAPE THE CASTLE - SCENE 1: THE CELL
# ==========================================
 
# Introduce the scene to the player
print("You wake up in a dark castle cell.")
print("You can see a door, a window and an old bed")
 
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
 
else:
    print("You decide not to investigate")
 
 
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
