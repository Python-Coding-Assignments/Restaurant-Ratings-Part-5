from Classes import Restaurant

def addRestaurant(restaurants):
    """This function will add a new restaurant to the list of restaurants, only if the restaurant does not already exist within that list.  The function takes in one parameter, which is a list of type Restaurant, that is mutable."""

    #declaration and initialization of variables
    flag = False
    name = website = ""
    emptyList = []
    counter = 0
    newRestaurant = Restaurant()

    #prompting the user to enter the restaurant's name
    print("Please enter in the name...")
    #while loop which runs until the user enters a valid name entry
    while flag == False:
        name = input("Please enter in a string with at least one character and at most ten characters: ")
        #conditional statement checking if input is valid
        if len(name) > 0 and len(name) <= 10:
            flag = True

    #prompting the user to enter the restaurant's website
    print("Please enter in the website...")
    #while loop which runs until the user enters a valid website entry 
    while flag == True:
        website = input("Please enter in a string with at least one character and at most one hundred and fifty characters: ")
        #conditional statement which checks if the input's website is valid
        if len(website) > 0 and len(website) <= 150:
            flag = False

    #instantiating a new instance of Restaurant
    newRestaurant = Restaurant(name, emptyList, website)

    #for loop which iterates over each element of the list restaurants
    for i in range(0, len(restaurants)):
        #conditional statement which checks if the new instance of Restaurant has the same website name as an already existing instance of Restaurant
        if newRestaurant.getWebsite() == restaurants[i].getWebsite():
            counter += 1

    #conditional statement which checks if value of counter is equal to zero
    if counter == 0:        
        #appending it to list of existing restaurants
        restaurants.append(newRestaurant)   
        print("Restaurant added successfully.\n")

    #conditional statement which checks if value of counter is not equal to zero
    else:
        print("Restaurant website already exists.\n")             