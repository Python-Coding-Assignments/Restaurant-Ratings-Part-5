from Classes import Rating

class Restaurant:
    """Class definition for Restaurant."""

    def __init__(self, *arguments):
        """This is a constructor the defines the public member attributes (instance variables) of the class: name, ratings, and website."""

        #conditional statement which checks if the number of arguments within the method's call is equal to zero
        if len(arguments) == 0:
            self.__name = "null"
            self.__ratings = "null"
            self.__website = "null"

        #conditional statement which checks if the number of arguments within the method's call is equal to two
        elif len(arguments) == 2:
            self.__name = arguments[0]
            self.__ratings = []
            self.__website = arguments[1]

        #conditional statement which checks if the number of arguments within the method's call is equal to three    
        elif len(arguments) == 3:
            self.__name = arguments[0]

            #declaration and initialization of local variables
            rating = Rating()
            ratings = []

            #for loop which runs through each iteration of the list contained in index one of the tuple
            for i in range(len(arguments[1])):
                #initializing rating and appending it to a list of ratings
                rating = (arguments[1][i])
                ratings.append(rating)

            self.__ratings = ratings    
            self.__website = arguments[2]

    def setName(self, name):
        """This method is a setter that sets the public instance variable name.""" 

        self.__name = name

    def getName(self):
        """This method is a getter that returns the public instance variable name."""

        return self.__name

    def setRatings(self, rating):
        """This method is a setter that appends a new rating to the instance variable containing all of the restaurant's ratings."""

        #creating instance of Rating, and then appending this new instance to the instance variable called ratings
        rating = Rating(rating.getUser(), rating.getRatingValue(), rating.getComment())
        self.__ratings.append(rating)

    def getRatings(self, index):
        """This method is a getter that returns a rating from a restaurant at a defined index."""

        return self.__ratings[index]
    
    def getRatingsSize(self):
        """This method returns the total number of ratings that a restaurant has."""
        
        return len(self.__ratings)
    
    def changeRating(self, rating, index):
        """This method changes the rating of a restaurant at a specified index."""

        self.__ratings[index] = rating

    def setWebsite(self, website):
        """This method is a setter which sets the name of the restaurant's website."""

        self.__website = website

    def getWebsite(self):
        """This method is a getter which returns the name of the restaurant's website."""

        return self.__website  

    def printRestaurant(self):
        """This method prints information about the restaurant's name and website."""

        #printing information about restaurant to user
        print("Restaurant Name: " + self.__name)
        print("Website: " + self.__website)
        print("******************\n")   

    def __eq__(self, other):
        """This method overloads the equality operator and compares two instances of type Restaurant."""

        #conditional statement which checks if two member private member attributes are the same
        if self.__name.strip() == other.__name.strip() and self.__website.strip() == other.__website.strip():
            return True
        #conditional statement which checks if two member private member attributes are not the same
        else:
            return False          