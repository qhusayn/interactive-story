# ---------------------------------
# LIBRARY - NEW SCENE - The Library
# ---------------------------------


def library():
    # TODO:
    # Create a Library scene.
    #
    # The player discovers a clue to the
    # password needed to escape the castle.
    #
    # Use:
    # - print()
    # - input()
    # - if/elif/else
    # - A while loop

    print("You enter a dusty castle library. You see a desk, a bookshelf, and a door.")

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