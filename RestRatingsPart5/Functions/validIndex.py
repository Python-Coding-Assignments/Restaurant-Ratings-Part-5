import string

def validIndex(restaurant, guide):
    """This function gets a valid restaurant index from the user.  When the user is prompted to enter a restaurant index, the index needs to be checked to ensure a restaurant at that index exists.  This function takes in one mutable argument, which is an instance of Restaurant.  The function then returns the user's valid restaurant index as a variable of type integer."""

    #declaration and initialization of variables
    x = nonNumCounter = 0
    flag = False
    index = ""

    #conditional statement checking if guide is equal to one
    if guide == "length of restaurant":
        x = len(restaurant)
    #conditional statement checking if guide does not equal one    
    else:
        x = restaurant.getRatingsSize()    

    #while loop which runs until the user enters a valid restaurant index
    while flag == False:
        #conditional statement checking if guide is equal to one
        if guide == "length of restaurant": 
            #getting index input from user
            index = input("Please enter in a Restaurant Index: ")
        #conditional statement checking if guide does not equal one
        else:
            #getting index input from user
            index = input("Please enter in a Rating Index: ")    

        #conditional statement which checks if the length of the user's input is greater than zero
        if len(index) > 0:
            #for loop which iterates over each character of the user's input
            for i in range(0, len(index)):
                #conditional statement which checks if each character is a digit
                if index[i] not in string.digits:
                    nonNumCounter += 1

        #conditional statement checking whether the number of non-digit characters is equal to zero
        if nonNumCounter == 0:             
            index = int(index)
            #conditional statement which checks if the user's input is valid
            if index < x:
                flag = True
        #conditional statement checking whether the number of non-digit characters is not equal to zero
        else:
            nonNumCounter = 0          

    #returning the valid restaurant index as an integer
    return index            