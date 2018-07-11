VALID_COLORS = ['blue', 'yellow', 'red']


def print_colors():
    """Ask for color, lowercase it, check if 'quit' is entered, if so print
       'bye' and break, next check if given color is in VALID_COLORS, if not,
       continue, finally if that check passes, print the color"""
    while True:
        user_input = input("Please enter a color").lower()
        if user_input == "quit":
            print("bye")
            break
        elif user_input in VALID_COLORS:
            print(user_input)
        else:
            print("Not a valid color")
            continue
