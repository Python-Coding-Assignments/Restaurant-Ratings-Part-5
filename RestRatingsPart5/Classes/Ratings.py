class Rating:
    """Class definition for Rating"""

    def __init__(self, *arguments):
        """This is a constructor which defines three instance variables: user, ratingValue, and comment."""

        #conditional statement which checks if the number of arguments within the method's call is equal to zero
        if len(arguments) == 0:
            self.__user = "null"
            self.__ratingValue = "null"
            self.__comment = "null"

        #conditional statement which checks if the number of arguments within the method's call is equal to three    
        elif len(arguments) == 3:    
            self.__user = arguments[0]
            self.__ratingValue = arguments[1]
            self.__comment = arguments[2]

    def setUser(self, user):
        """This method is a setter which sets the instance variable user."""

        self.__user = user

    def getUser(self):
        """This method is a getter which returns the instance variable user."""

        return self.__user

    def setRatingValue(self, value):
        """This method is a setter which sets the instance variable ratingValue."""

        self.__ratingValue = value

    def getRatingValue(self):
        """This method is a getter which returns the instance variable ratingValue."""

        return self.__ratingValue

    def setComment(self, comment):
        """This method is a setter which sets the instance variable comment."""

        self.__comment = comment

    def getComment(self):
        """This method is a getter which returns the instance variable comment."""

        return self.__comment       

    def printRating(self):
        """This method prints information about the rating to the screen."""

        #printing information about the rating's user, rating value, and comment
        print("User: " + self.__user)
        print("Rating Value: " + str(self.__ratingValue))
        print("Comment: " + self.__comment)
        print("******************\n")         