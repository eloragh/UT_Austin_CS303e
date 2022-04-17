# File: MinMax.py
# Student: Eloragh Espie
# UT EID: eae2273
# Course Name: CS303E
# 
# Date: 02/23/2022
# Description of Program: This program prompts the user for an undefined amount of integers and returns the minimum and maximum values.

def main():

    # get initial value from user
    min_max_value = input("Enter an integer or \'stop\' to end: ")

    #if the value is not "stop", convert it to an int
    if min_max_value != "stop":
        min_max_value = eval(min_max_value)
    
    #if the value is stop, print the string
    else:
        print("You didn't enter any numbers")

    #these are initially set to the first value since that value will be both the maximum and minimum until another value is entered
    maximum = min_max_value
    minimum = min_max_value

    #this while statement will iterate if the first value of min_max_value is not "stop"
    while min_max_value != "stop":
        
        #continues to prompt user for an integer input
        min_max_value = input("Enter an integer or \'stop\' to end: ")

        #when the user decides to enter "stop" it will print the final max and min values
        if min_max_value == "stop":

            print("The maximum is", maximum)
            print("The minimum is", minimum)
            return

        min_max_value = int(min_max_value)

        #this block of code checks if each value of min_max_value is greater than the maximum variable or less than the minimum variable
        if min_max_value > maximum:
            maximum = min_max_value

        if min_max_value < minimum:
            minimum = min_max_value

main()

