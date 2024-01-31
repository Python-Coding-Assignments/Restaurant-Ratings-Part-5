def saveData(restaurants):
    """This function saves all the data regarding restaurants and their respective ratings into a text file.  The function takes in one parameter, which is a list containing elements of type Restaurant."""

    #declaration and initialization of variable
    restaurantNamesWebsites = []

    #for loop which runs through each integer between zero, inclusive, and the number of restaurants, exclusive
    for i in range(len(restaurants)):
        #adding elements of type string to the list
        restaurantNamesWebsites.append("Restaurant Name: " + restaurants[i].getName())
        restaurantNamesWebsites.append("Website: " + restaurants[i].getWebsite()) 

    #writing to a file that either exists or does not exist, giving the file all the information about the restaurants within the application
    with open("TextFiles/RestaurantNamesWebsites.txt", "w") as f:
        #for loop which runs through each integer between zero, inclusive, and the length of the list of, exclusive
        for i in range(len(restaurantNamesWebsites)):
            #conditional statement which checks if the value of i is one less than the length of the list containing all of the restaurants' information
            if i + 1 == len(restaurantNamesWebsites):
                #writing to file
                f.write(restaurantNamesWebsites[i])
            #conditional statement which checks if the value of i is anything other than one less than the length of the list    
            else:
                #writing to file
                f.write(restaurantNamesWebsites[i] + "\n")    

    #for loop which runs through each integer between zero, inclusive, and the number of restaurants, exclusive
    for i in range(len(restaurants)):
        #writing to a file that either exists or has yet to be created
        with open("TextFiles/" + restaurants[i].getWebsite(), "w") as f:
            #conditional statement checking if the number of restaurants in the provided list is greater than zero
            if restaurants[i].getRatingsSize() > 0:
                #for loop which runs through each of the restaurant's ratings
                for j in range(restaurants[i].getRatingsSize()):
                    #writing to file regarding rating information
                    f.write("User: " + restaurants[i].getRatings(j).getUser() + "\n")
                    f.write("Rating Value: " + str(restaurants[i].getRatings(j).getRatingValue()) + "\n")

                    #conditional statement which checks if the current j index is one less than the total number of ratings the restaurant has
                    if j + 1 == restaurants[i].getRatingsSize():
                        #writing to file
                        f.write("Comment: " + restaurants[i].getRatings(j).getComment())        
                    #conditional statement which checks if the current j index is not one less than the total number of ratings the restaurant has
                    else:
                        #writing to file
                        f.write("Comment: " + restaurants[i].getRatings(j).getComment() + "\n")
            
            #conditional statement which checks if the number of the number of restaurants in the list is equal to zero
            else:
                #writing to file
                f.write("User: \nRating Value: \nComment: ")            
