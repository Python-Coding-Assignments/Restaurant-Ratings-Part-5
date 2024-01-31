class User:
    """Class definition for User"""

    def __init__(self, *arguments):
        """This is a constructor that defines four instance variables: name, alias, age, and password."""

        #conditional statement which evaluates to True if the length of the arguments tuple is equal to zero
        if len(arguments) == 0:
            self.__name = "null"
            self.__alias = "null"
            self.__age = 0
            self.__password = "null"

        #conditional statement which evaluates to True if the length of the arguments tuple is equal to four    
        elif len(arguments) == 4:
            self.__name = arguments[0]
            self.__alias = arguments[1]
            self.__age = arguments[2]
            self.__password = arguments[3]

    def setName(self, name):
        """This method is a setter which sets the instance variable name."""   

        self.__name = name

    def getName(self):
        """This method is a getter which returns the instance variable name."""

        return self.__name

    def setAlias(self, alias):
        """This method is a setter which sets the instance variable alias."""

        self.__alias = alias

    def getAlias(self):
        """This method is a getter which returns the instance variable alias."""

        return self.__alias

    def setAge(self, age):
        """This method is a setter which sets the instance variable age."""

        self.__age = age

    def getAge(self):
        """This method is a getter which returns the instance variable age."""

        return self.__age

    def setPassword(self, password):
        """This method is a setter which sets the instance variable password."""

        self.__password = password

    def getPassword(self):
        """This method is a getter which returns the instance variable password."""

        return self.__password

    def __eq__(self, other):
        """This method overloads the operator == to enable a comparison between two instances of User."""

        #conditional statement which evaluates to True if both names and passwords of an instance are the same
        if self.__name == other.__name and self.__password == other.__password:
            return True
        
        #conditional statement which evaluates to True if previous conditional statement evaluates to False
        else:
            return False                            