# File: Student.py
# Student: Eloragh Espie
# UT EID: eae2273
# Course Name: CS303E
# 
# Date: 03/12/2022
# Description of Program: This program defines a student class that can return information about a student and their grades.

class Student:

    def __init__(self, name, Exam1 = None, Exam2 = None):
        self.__name = name
        self.__Exam1 = Exam1
        self.__Exam2 = Exam2
    
    def getName(self):
        return self.__name

    def setExam1Grade(self, Exam1):
        self.__Exam1 = Exam1
    
    def setExam2Grade(self, Exam2):
        self.__Exam2 = Exam2
    
    def getExam1Grade(self):
        if self.__Exam1 == None:
            pass
        else:
            print(self.__Exam1)
    
    def getExam2Grade(self):
        if self.__Exam2 == None:
            pass
        else:
            print(self.__Exam2)
    
    def getAverage(self):
        if self.__Exam1 == None or self.__Exam2 == None:
            print("Some exam grades not available.")
        else:
            print((self.__Exam1 + self.__Exam2)/2)

    def __str__(self):
        return "Student: " + str(self.__name) + "\n" + \
        "  Exam1: " + str(self.__Exam1) + "\n" + \
        "  Exam2: " + str(self.__Exam2)