from Classes import User
from Functions import initRestaurants, loadData

def login(user, restaurants):
    """This function logs the user into the restaurant application.  The function takes in two arguments: one is an instance of type User, and the other is a list containing objects of type Restaurant."""

    #declaration and initialization of variables
    entry = contentStr = ""
    flag1 = flag2 = False
    loginAttempts = 0
    entries = []
    newUser = User()
    
    #while loop which runs until flag is True
    while flag1 == False:
        #for loop which iterates over the integers one and two
        for i in range(1, 3):
            #conditional statement checking whether the index value i is equal to one
            if i == 1:
                print("Login\nName: ")
            #conditional statement checking whether the index value i is equal to two    
            elif i == 2:
                print("Password: ")

            #while loop which runs until flag is True    
            while flag2 == False:
                #getting either name or password from user
                entry = input("Please enter in a string with at least one character and at most " + str(i * 10) + " characters: ")

                #conditional statement checking whether the length of the user entry is valid
                if len(entry) > 0 and len(entry) <= i * 10:
                    #appending entry to a list of entries of type string
                    entries.append(entry)   
                    flag2 = True

            flag2 = False

        #creating a new instance of User    
        newUser = User(entries[0], "Gege", 20, entries[1])

        #clearing all elements of entries
        entries.clear()
        print()

        #conditional statement checking whether the new user created by the user matches the already defined user
        if newUser == user:
            flag1 = True   
        #conditional statement which evaluates to True if the new instance of User does not match the existing instance of User    
        else:
            print("Invalid login.  Try again.\n")

    #reading from file that already exists
    with open("TextFiles/loginAttempts.txt") as f:
        #reading all content from file and storing it into a string
        contentStr = f.read()

    #splitting the list of content from the file into smaller strings, all connected in a list
    content = contentStr.split("\n")

    #for loop which iterates over the integers between zero, inclusive, and the integer value representing the total number of elements in content, exclusive
    for i in range(len(content)):
        #conditional statement which checks if slice of list is equivalent to another defined string
        if content[i][:9] == user.getName() + ": ":
            loginAttempts = int(content[i][9:])    

    #conditional statement checking if the user's number of login attempts is equal to zero
    if loginAttempts == 0:
        #calling the initRestaurants function
        initRestaurants(restaurants)
    #conditional statement checking if the user's number of login attempts is any integer other than zero    
    else:
        #calling the loadData function
        loadData.loadData(restaurants)
    
    #overwriting the contents of the file with the updated content
    with open("TextFiles/loginAttempts.txt", "w") as f:
        #writing to file
        f.write(user.getName() + ": " + str(loginAttempts + 1))    