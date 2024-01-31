from Classes import Rating, Restaurant

def initRestaurants(restaurants):
    """This function initializes five restaurants and appends each instance of the class Restaurant to a mutable list.  This mutable list is the function's only argument that is passed to the parameter."""

    #declaration and initialization of variables
    ratings = []
    rating = Rating()
    restaurant = Restaurant()

    #creating two instances of Rating and appending them to a list of ratings
    rating = Rating("Sally Jo", 4, "I love their vanilla ice cream!")
    ratings.append(rating)
    rating = Rating("Mike Smith", 2, "Their chocolate ice cream is just okay.")
    ratings.append(rating)
    #creating an instance of Restaurant and appending it to a list of restaurants
    restaurant = Restaurant("Val's Ice Cream", ratings, "www.val'sIceCream.com")
    restaurants.append(restaurant)
    #clearing list of ratings
    ratings.clear()

    #creating two instances of Rating and appending them to a list of ratings
    rating = Rating("Selena Gomez", 1, "No hamburgers.  Only chicken.")
    ratings.append(rating)
    rating = Rating("Cher", 5, "The fries are amazing!")
    ratings.append(rating)
    #creating an instance of Restaurant and appending it to a list of restaurants
    restaurant = Restaurant("Chick-fil-a", ratings, "www.chick-fil-a.com")
    restaurants.append(restaurant)
    #clearing list of ratings
    ratings.clear()

    #creating two instances of Rating and appending them to a list of ratings
    rating = Rating("Demi Lovato", 2, "The food was too greasy!")
    ratings.append(rating)
    rating = Rating("Halsey", 4, "I love their milkshakes.")
    ratings.append(rating)
    #creating an instance of Restaurant and appending it to a list of restaurants
    restaurant = Restaurant("McDonald's", ratings, "www.mcDonald's.com")
    restaurants.append(restaurant)
    #clearing list of ratings
    ratings.clear()

    #creating two instances of Rating and appending them to a list of ratings
    rating = Rating("Trippie Redd", 4, "I love their salads.")
    ratings.append(rating)
    rating = Rating("YNW Melly", 3, "Their food was decent.")
    ratings.append(rating)
    #creating an instance of Restaurant and appending it to a list of restaurants
    restaurant = Restaurant("Applebee's", ratings, "www.applebee's.com")
    restaurants.append(restaurant)
    #clearing list of ratings
    ratings.clear()

    #creating two instances of Rating and appending them to a list of ratings
    rating = Rating("Wendy Williams", 4, "They have the same name as me")
    ratings.append(rating)
    rating = Rating("Lil Durk", 2, "The wait was so long for food.")
    ratings.append(rating)
    #creating an instance of Restaurant and appending it to a list of restaurants
    restaurant = Restaurant("Wendy's", ratings, "www.wendy's.com")
    restaurants.append(restaurant)
    #clearing list of ratings
    ratings.clear()