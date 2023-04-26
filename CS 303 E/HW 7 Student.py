# File: Student.py
# Student: Patrick Pichardo
# UT EID: pjp953
# Course: CS303E
#
# Date: 02/28/2023
# Description of Program: This program defines a "Student" 
#class with private variables for name and exam grades. 
#It includes methods to get and set these variables, calculate the average, 
#and provide a string representation of the object. The code creates two instances 
#of the class and demonstrates the use of its methods.


class Student:
    # The double underscore before the names of the variables
    # indicates the private variables, which means they can only
    # be accessed from within the class itself, and not from outside the class
    def __init__(self, name, exam1=None, exam2=None):
        self.__name = name
        self.__exam1 = exam1
        self.__exam2 = exam2

    # pulls the defined self.__name
    def getName(self):
        return self.__name

    # pulls the defined self.__exam1
    def getExam1Grade(self):
        return self.__exam1
    # puts new exam 1 grade
    def setExam1Grade(self, grade):
        self.__exam1 = grade
    # pulls the defined self.__exam2
    def getExam2Grade(self):
        return self.__exam2
    # puts new exam 2 grade
    def setExam2Grade(self, grade):
        self.__exam2 = grade
    # averages the self.__exam1 & self.__exam2, & checks if any grades were input. 
    def getAverage(self):
        if self.__exam1 is None or self.__exam2 is None:
            return print("Some grades aren't available.")
        else:
            return (self.__exam1 + self.__exam2) / 2
    
    def __str__(self):
        return f"Student: {self.__name} \n  Exam1: {self.__exam1} \n  Exam2: {self.__exam2}"
    

# cool it works 
bob = Student("Bob, B", 85, 90)
print(bob)
print(bob.getName())
print(bob.getAverage())
print(bob.getExam2Grade())

clark = Student( "Clark K.", 100 )
print(clark)
print(clark.getName())
print(clark.getAverage())
print(clark.setExam2Grade(90))
print(clark)
print(clark.getAverage())
    
    
    
    
