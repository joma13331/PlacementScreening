# Placement Screening Assignment 2

**Problem: Demonstrate use of abstract class, multiple inheritance and decorator in python using examples.**

* The solution to the above problem is implemented through three python files: 'Sportsperson.py', 'Team.py' and 'Footballer.py'.
1. The abstract class is implemented through 'Sportsperson.py' where class Sportsperson is an abstract class with thre abstract methods: 'store_details', 'print_details' and 'estimated_salary'.
2. Multiple Inheritance is implemented through 'Footballer.py' in which class 'Footballer' inherites from 'Sportsperson' and 'Team' class.
3. Decorators are implemented in two python files 'Sportsperson.py' and 'Footballer.py'. 
    * In 'Sportsperson.py' decorator '@abstractmethod' is used to create abstract method. 
    * In 'Footballer.py' decorator '@staticmethod' is used create static methods which are independent of the object.

* Try and Except blocks are used to prevent any errors to distrupt the flow of execution.

* Logging is implemented to keep track of significant result or execution of commands.