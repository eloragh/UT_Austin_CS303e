# File: DaysInMonth.py
# Student: Eloragh Espie
# UT EID: eae2273
# Course Name: CS303E
# 
# Date: 02/17/2022
# Description of Program: This program takes a year and a month as input and returns the number of days in that month for the given year.

def main():
    year = eval(input("Please enter a year: "))
    month = eval(input("Please enter a month: "))

    LeapYear = (year % 4 == 0) and (not (year % 100 == 0) or (year % 400 == 0))

    if month == 1:
        print("January " + str(year) + " has 31 days")
    
    if month == 2 and LeapYear:
        print("February " + str(year) + " has 29 days")
    elif month == 2:
        print("February " +str(year) + " has 28 days")

    if month == 3:
        print("March " + str(year) + " has 31 days")
    
    if month == 4:
        print("April " + str(year) + " has 30 days")
    
    if month == 5:
        print("May " + str(year) + " has 31 days")
    
    if month == 6:
        print("June " + str(year) + " has 30 days")
    
    if month == 7:
        print("July " + str(year) + " has 31 days")
    
    if month == 8:
        print("August " + str(year) + " has 31 days")
    
    if month == 9:
        print("September " + str(year) + " has 30 days")
    
    if month == 10:
        print("October " + str(year) + " has 31 days")
    
    if month == 11:
        print(" November " + str(year) + " has 30 days")
    
    if month == 12:
        print("December " + str(year) + " has 31 days")

main()