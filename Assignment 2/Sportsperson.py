from abc import abstractmethod


# BASE CLASS 1
# EXAMPLE of ABSTRACT CLASS
class Sportsperson:
    """
    Class Name: Sportsperson
    Description: This is the Base Abstract class which will ensure that basic
               methods(behaviour) and attributes(properties) about a
               sportsperson irrespective of their choice of sport are modelled
               by inherited classes.
    """

    def __init__(self, name, nationality, age):
        """
        Method Name: __init__
        Description: This method is the constructor for Sportsperson class. It
                     initializes class variables which are important for any
                     sportsperson
        params: - name - Name of the Sportsperson
                - nationality - Country to which the sportsperson belongs to
                - age - Age of the sportsperson
        """
        self.name = name
        self.nationality = nationality
        self.age = age

    # EXAMPLE of DECORATOR
    @abstractmethod
    def store_details(self):
        """
        Method Name: print_details
        Description: This abstract method ensures that any class which inherits
                     from Sportsperson class will print relevant details about the
                     sportsperson object which is created.
        """
        pass

    # EXAMPLE of DECORATOR
    @abstractmethod
    def print_details(self):
        """
        Method Name: print_details
        Description: This abstract method ensures that any class which inherits
                     from Sportsperson class will print relevant details about the
                     sportsperson object which is created.
        """
        pass

    # EXAMPLE of DECORATOR
    @abstractmethod
    def estimated_salary(self):
        """
        Method Name: estimated_salary
        Description: This abstract method ensures that any class which inherits
                     from Sportsperson class will calculate what that sportsperson
                     should earn based on his/her performance.
        """
        pass
