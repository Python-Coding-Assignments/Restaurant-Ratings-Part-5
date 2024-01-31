def displayRestaurants(restaurants):
    """This function will print every restaurant that is in the system, along with some additional information about the restaurant.  This function also takes in a singular, mutable, argument from the function's call."""

    print("\nDisplay restaurants...")
    #for loop which iterates over each index of the list of restaurants
    for i in range(len(restaurants)):
        #printing information about each restaurant to the user
        print("Restaurant Index: " + str(i))
        restaurants[i].printRestaurant()