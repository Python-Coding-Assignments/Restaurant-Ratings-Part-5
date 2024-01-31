from Classes import User
from Functions import promptAction, implementAction, login, loadData, saveData

#declaration and initialization of variables
restaurants = []
flag = False
userAction = ""
user = User("Garrett", "Gege", 20, "garrettbovo")

#prompting the user to login into application
login(user, restaurants )

#welcoming user
print("Welcome to my Restaurant Ratings App!\n")

#while loop which runs until the user decides to quit the program
while flag == False:
    #getting user menu selection input
    userAction = promptAction()

    #determining how the program should run based on user's input
    implementAction(restaurants, userAction)

    #conditional statement checking if user's menu selection is either "q" or "Q"
    if userAction == "q" or userAction == "Q":
        saveData(restaurants)
        flag = True        