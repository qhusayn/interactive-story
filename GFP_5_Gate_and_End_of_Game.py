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
