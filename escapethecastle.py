#Welcome the player!
print("=== ESCAPE THE CASTLE ==")
print("Welcome, adventurer!")
 
#Get player name, age and character class
playerName = input("What is your name? ")
characterClass = input("What type of adventurer are you? ")
characterAge = int(input("How old is your character? "))
 
 #Set starting values
health = 100
gold = 20
hasKey = False

#Display the character profile
print(f"\n=== CHARACTER PROFILE ===")
print(f"Name: {playerName}")
print(f"Class: {characterClass}")
print(f"Age: {characterAge}")
print(f"Health: {health}")
print(f"Gold: {gold}")
print(f"Has Key: {hasKey}")

#Begin the story
print(f"\n{playerName}, you find yourself in a dark and mysterious castle. Your goal is to escape, but beware of the dangers that lie ahead!")
print("You hear footsteps approaching...")
print("Your adventure is about to begin!")

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

 