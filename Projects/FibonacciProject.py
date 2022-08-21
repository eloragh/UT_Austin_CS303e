# File: Project2.py
# Student: Eloragh Espie
# UT EID: eae2273
# Course Name: CS303E
# 
# Date: 03/30/2022
# Description of Program: This program displays several different functions the user can enact using the Fibbonaci sequence

#IMPORTS

#GLOBALS
COMMAND_ERROR = "ERROR: Illegal command. Try again."
VALUE_ERROR = "ERROR: Illegal value entered."
GOODBYE = "Thanks for using the Fibonnaci Laboratory!  Goodbye."

#FUNCTIONS
def welcomeMessage():
    print("" + "\n" + "Welcome to the Fibonnaci Number laboratory!" + "\n")

def helpMessage():
    #prints the initial help message that gives the user the input options
    print("The following commands are available:" + "\n" + "  0: Exit" \
        + "\n" + "  1: List the first N Fibonnaci numbers." + "\n" + "  2: Display the ith Fibonnaci number (0-based)." \
        + "\n" + "  3: List the Fibonnaci numbers less or equal to N." + "\n" + "  4: How many Fibonnaci numbers are less or equal to N?" \
        + "\n" + "  5: Find a list of the largest Fibonnaci numbers that add up to N." + "\n" + "  6: Display this help message. " + "\n" + "")

def firstNFibNumbers(n):
    """ Return a list of the first n Fibonnaci numbers.  If 
        n < 0, return the empty list. """
    
    fibs = []
    
    if n <= 0:
        return fibs

    # Handle the cases of n == 1 and n == 2 specially.
    elif n == 1:
        fibs.append(0)
        return fibs
    elif n == 2:
        fibs.append([ 0, 1 ])
        return fibs

    # Here we know that n is at least 2.
    else:

        # Initialize fib1 and fib2 with the first 
        # two Fibonnaci numbers.
        fib1, fib2 = 0, 1

        # Initialize our list of Fibonnaci numbers
        # found so far.
        fibs = [ 0, 1 ]

        # Use the previous two values to generate 
        # and record the next value.
        for counter in range( 2, n ):

            # Update fib1 and fib2 with their new
            # values.
            fib1, fib2 = fib2, fib1 + fib2

            # Add the newest value to the list we're
            # creating.
            fibs.append( fib2 )

        return fibs

def organizeInput(value):

    if int(value) == 1:
        #get user input
        n = int(input("You've asked for the first N Fibonnaci numbers. What is N? "))
        #validate input
        if n < 0:
            return VALUE_ERROR
        #if input passes validation check,
        #return the first n numbers in the fibbonaci sequence
        else:
            return firstNFibNumbers(n)
    
    if int(value) == 2:
        #get user input
        i = int(input("You've asked for the ith Fibonnaci number. What is i? "))
        #validate input
        if i < 0:
            return VALUE_ERROR
        #if input passes validation check, 
        #return the desired i index of the list of first n numbers 
        #in the fibbonaci sequence
        else:
            fib_list = firstNFibNumbers(i+1)
            return fib_list[i]
    
    if int(value) == 3:
        #get user input
        n = int(input("You've asked for the Fibonnaci numbers less than or equal to N. What is N? "))
        #no need to validate input here, it's specified as an int in the input request
        #and the user can ask for positive or negative integers here
        #get the list of the first n numbers in the fibbonaci sequence
        fib_list = firstNFibNumbers(n + 1)
        #create a new list
        new_fib_list = []
        #loop through the first list
        for fib in fib_list:
            #if the fib is less than the input, add it to the new list
            if fib <= n:
                new_fib_list.append(fib)
        #return the new list
        return new_fib_list
    
    if int(value) == 4:
        #get user input
        n = int(input("You've asked how many Fibonnaci numbers are less than or equal to N. What is N? "))
        #same situation here, as in value 3 statement, no need to validate input
        #create a new list variable to loop through
        fib_list = firstNFibNumbers(n + 1)
        #initialize a counter
        count = 0
        #loop through the list
        for fib in fib_list:
            #if the fib is less than n, add one to the counter
            if fib <= n:
                count += 1
        #return the number of fibbonaci sequence numbers that are less than n
        return count
    
    if int(value) == 5:
        #Zeckendorf's Theorem says that every positive integer can be written uniquely 
        #as a sum of one or more non-consecutive Fibonacci numbers.

        #get user input
        n = int(input("You've asked for Fibonnaci numbers that sum to N. What is N? "))

        #validate input
        if n < 0:
            return VALUE_ERROR
        
        if n == 0:
            return [0]

        #use the for loop from value 3 equation to find list of fibs less than or equal to n
        fib_list = firstNFibNumbers(n)
        new_fib_list = []
        for fib in fib_list:
            if fib <= n:
                new_fib_list.append(fib)
        
        #create a new list we can use to check if fibbonaci numbers = n
        max_fib_to_n = []
        #the maximum fib = the max fib from the list from the value three loop
        max_fib = max(new_fib_list)
        #append the max fib to the new list
        max_fib_to_n.append(max_fib)
        #remove that max fib so we can check the next highest fib, attempting to reduce the number of numbers needed to equal n
        new_fib_list.remove(max_fib)

        #this loop will continue until the sum of the elements of the new list is equal to n
        while sum(max_fib_to_n) != n:
            #if the sum of the elements of the new list is still less than n
            if sum(max_fib_to_n) < n:
                #find a new maximum from the value 3 loop to check
                new_max = max(new_fib_list)
                #and if the sum of the new list plus the new max is less than or equal to n
                if sum(max_fib_to_n) + new_max <= n:
                    #and the new maximum is greater than zero
                    if new_max > 0:
                        #append the new max to the new list and remove it from the old one
                        max_fib_to_n.append(new_max)
                        new_fib_list.remove(new_max)
                #if the new max + sum of list is not <= n, remove that max since we can't use it anyway
                else:
                    new_fib_list.remove(new_max)
        #the loop will break when the new list = n, and the statement will return that list
        return max_fib_to_n
     
#MAIN

def main():

    value = (input("Please enter a command (0, 1, 2, 3, 4, 5 or 6): "))

    if (value == "6") or (value == "help") or (value == "?"):
        print("\n")
        helpMessage()
        main()
    elif int(value) == 0:
        print("\n" + GOODBYE + "\n")
    elif int(value) < 0:
        print(COMMAND_ERROR + "\n")
        main()
    elif int(value) > 6:
        print(COMMAND_ERROR + "\n")
        helpMessage()
        main()
    else:
        print(organizeInput(value))
        print("")
        main()
        
welcomeMessage()
helpMessage()
main()
