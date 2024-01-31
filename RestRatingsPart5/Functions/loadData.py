from Classes import Restaurant, Rating

def loadData(restaurants):
    """This function loads all the data from the text files and then stores that information into a list of restaurants.  This function takes in the list, that will be modified as a list is mutable, as a parameter.  This parameter is a list containing elements all of type Restaurant."""

    #declaration and initialization of variables
    names = []
    websites = []
    content = []
    information = user = ratingValue = comment = ""
    newRestaurant = Restaurant()
    newRating = Rating()

    #reading from file that already exists
    with open("TextFiles/RestaurantNamesWebsites.txt") as f:
        #reading from file and storing all of the files contents into a very long list
        information = f.read()

    #splitting the long list of information into smaller strings that will each be elements of the list called content
    content = information.split("\n")

    #for loop which iterates over each integer between zero, inclusive, and the integer value representing the total number of items in the list, exclusive
    for i in range(len(content)):
        #conditional statement which checks if a slice of a specified content's element is equal to the provided string
        if content[i][:17] == "Restaurant Name: ":
            #appending element slice to the list of names
            names.append(content[i][17:])
        #conditional statement which checks if a slice of a specified content's element is equal to the provided string    
        elif content[i][:9] == "Website: ":
            #appending element slice to the list of websites
            websites.append(content[i][9:])

    #for loop which iterates over each integer between zero, inclusive, and the integer value representing the total number of items in the list, exclusive
    for i in range(len(names)):
        #instantiating a new instance of Restaurant and appending this new instance to a list of objects of type Restaurant
        newRestaurant = Restaurant(names[i], websites[i])
        restaurants.append(newRestaurant)

    #for loop which iterates over each integer between zero, inclusive, and the integer value representing the total number of items in the list, exclusive
    for i in range(len(restaurants)):
        #clearing all indices of the list called content
        content.clear()

        #reading from file that already exists
        with open("TextFiles/" + restaurants[i].getWebsite()) as f:
            #reading from file and storing all of its contents into a very large string
            information = f.read()

        #splitting large string of information into smaller strings that are all individual indices within the list
        content = information.split("\n")
        
        #for loop which iterates over each integer between zero, inclusive, and the integer value representing the number of elements within content, exclusive
        for j in range(len(content)):
            #conditional statement which checks if a slice of the content at index j is equal to the provided string and also that the length of element at index j is not equal to six
            if content[j][:6] == "User: " and len(content[j]) != 6:
                #initializing user to slice of content at index j
                user = content[j][6:]

                #conditional statement which checks if a slice of the content at index j + 1 is equal to the provided string
                if content[j + 1][:14] == "Rating Value: ":
                    #initializing ratingValue to slice of content at index j + 1
                    ratingValue = int(content[j + 1][14:])

                #conditional statement which checks if a slice of the content at index j +2 is equal to the provided string  
                if content[j + 2][:9] == "Comment: ":
                    #initializing comment to slice of content at index j + 2
                    comment = content[j + 2][9:]

                    #instantiating new instance of Rating and adding rating to the specified restaurant at index i
                    newRating = Rating(user, ratingValue, comment)
                    restaurants[i].setRatings(newRating)
                    
                    j += 2            