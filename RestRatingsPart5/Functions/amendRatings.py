from Classes import Rating
import string

def amendRatings(restaurant, *arguments):
    """This function gets all the required information from the user in order to create a new rating for a specified restaurant.  The function takes in one argument, which is mutable, when it is called, an object of type Restaurant.  The function then appends the new rating to the restaurant's already existing ratings."""

    #declaration and initialization of variables
    user = comment = ""
    ratingValue = 0
    flag = False
    rating = Rating()

    #conditional statement checking if number of arbitrary arguments is zero
    if len(arguments) == 0:
        #prompting the user to enter his or her name
        print("Please enter in the user...")
        #while loop which runs until the user enters a valid name entry
        while flag == False:
            user = input("Please enter in a string with at least one character and at most ten characters: ")
            #conditional statement checking if user's name is valid
            if len(user) > 0 and len(user) <= 10:
                flag = True

    #conditional statement checking if length of arbitrary arguments is one 
    elif len(arguments) == 1:
        flag = True            
    
    #prompting the user to enter his or her rating value for the restaurant
    print("Please enter in the rating...")
    #while loop which runs until the user enters a valid rating index entry
    while flag == True:
        ratingValue = input("Please enter in a rating value between one and five: ")
        #conditional statement which checks if user's input contains only integers and input's maximum length is one
        if ratingValue not in string.digits or len(ratingValue) != 1:
            continue
        ratingValue = int(ratingValue)
        #conditional statement which checks if the user's input is valid
        if ratingValue > 0 and ratingValue < 6:
            flag = False

    #prompting the user to enter his or her comment for the rating
    print("Please enter in the comment...")
    #while loop which runs until the user enters a valid comment entry 
    while flag == False:
        comment = input("Please enter in a string with at least one character and at most five hundred characters: ")
        #conditional statement which checks if the input's comment is valid
        if len(comment) > 0 and len(comment) <= 500:
            flag = True

    #conditional statement which checks if number of arbitrary arguments is zero
    if len(arguments) == 0:
        #creating new instance of rating
        rating = Rating(user, ratingValue, comment)
        #adding new rating to end of list of restaurant's ratings
        restaurant.setRatings(rating)
        print("Rating successfully added\n")

    #conditional statement checking if length of arbitrary arguments is one
    elif len(arguments) == 1:
        #creating new instance of rating
        rating = Rating(restaurant.getRatings(arguments[0]).getUser(), ratingValue, comment)
        #changing restaurant's rating at specified index
        restaurant.changeRating(rating, arguments[0])
        print("Rating successfully changed\n")