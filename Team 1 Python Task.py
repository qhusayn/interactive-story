#Ask the player for their name and store it as a variable
print("Hi traveller! We'll be creating your character today")
charName = input("What is your character's name? ")
print(f"Welcome, {charName}!")

#Ask the player for their age and store it as a variable
charAge = int(input("What is your character's age? "))

#Ask the player for their character class and store it as a variable
charClass = input("What is your character's class? (e.g., Warrior, Mage, Rogue) ")

#Ask the player for their favourite skill and store it as a variable
charSkill = input("What is your character's favourite skill? ")

#Ask the player for their character's weapon of choice and store it as a variable
charWeapon = input("What is your character's weapon of choice? ")

#Display the character's information to the console
print(f"Your character {charName} is a {charAge}-year-old {charClass} wielding a {charWeapon}.")
print(f"They are skilled in {charSkill} and ready for adventure!")
