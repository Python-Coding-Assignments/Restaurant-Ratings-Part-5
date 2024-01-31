from Functions import menu

def promptAction():
    """This function gets the user's input for his or her desired menu selection.  This function then returns a string call userInput which is the user's input."""

    #declaration and initialization of variable
    userInput = ""

    #calling menu function, printing menu to screen, and getting user's input
    menu()
    userInput = input("What would you like to do?\n")

    #returning user's input
    return userInput