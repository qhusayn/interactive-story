# -------------------------------------------------
# CORRIDOR - COPY DAY 3/4 CODE - Enter The Corridor
# -------------------------------------------------

import random
 
# SHARED GAME INFORMATION
inventory = []

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