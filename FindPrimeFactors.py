# File: FindPrimeFactors.py
# Student: Eloragh Espie
# UT EID: eae2273
# Course Name: CS303E
# 
# Date: 03/31/2022
# Description of Program: 

#IMPORTS

from math import *

#GLOBALS

#FUNCTIONS
def isPrime(num):
    ''' Return if n is prime or not '''
    
    if num < 2:
        return False
    elif num % 2 == 0:
        if num == 2:
            return True
        else:
            return False
            
    divisor = 3
    
    while divisor <= sqrt(num):
        if (num % divisor == 0):
            return False
        else:
            divisor += 2
    return True

def findNextPrime (num):
    """ Find the first prime > num. """
    if ( num < 2 ):
        return 2
    # If (num >= 2 and num is even ), the
    # next prime after num is at least
    # (num - 1) + 2 , which is odd.
    guess = num + 2
    if ( num % 2 == 0) :
        num -= 1
        guess = num + 2

    while (isPrime (guess) == False):
        guess += 2
    return guess

def primeFactors(num, factors):

    d = 2

    #as long as num is greater than 1 do the following:
    while num > 1:
        #check if d divides num
        if num % d == 0:
            #if it does, add d to the end of the list of factors
            factors.append(d)
            #and divide num by d
            num = num // d
            #iterate again, checking if the current divisor divides into the new number
        else:
            d = findNextPrime(d)
    return

#MAIN

def main():

    num = int(input("Enter a positive integer (or 0 to stop): "))

    if num == 0:
        print("Goodbye!")
        return

    elif num == 1:
        print("  1 has no prime factorization." + "\n")
        main()

    elif num < 0:
        print("  Negative integer entered. Try again." + "\n")
        main()

    else:
        if isPrime(num) == True:
            print("  The prime factorization of " + str(num) + " is: " + str([num]) +  "\n")
                
            
        else:
            factors = []
            primeFactors(num, factors)
            print("  The prime factorization of " + str(num) + " is: " + str(factors) + "\n")

        main()
    return
 
print("Find Prime Factors:")
main()