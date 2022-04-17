# File: MyStringFunctions.py
# Student: Eloragh Espie
# UT EID: eae2273
# Course Name: CS303E
# 
# Date: 03/28/2022
# Description of Program: A series of functions for the string class.

def myAppend( str, ch ):
    #returns a new string with the ch character appended to the end
    return str + ch

def myCount( str, ch ):
    #returns the number of times the ch character appears in the string
    count = 0
    index = 0

    for i in range(len(str)):

        if str[index] == ch:
           count += 1
           index += 1
           i += 1
        
        else:
            index += 1
            i += 1
    return count

def myExtend( str1, str2 ):
    #returns a new string that is the concatenation of str1 and str2
    str3 = str1 + str2
    return str3

def myMin( str ):
    #returns the character within the given string with the lowest ASCII value
    if str == "":
        return "Empty string: no min value"

    minimum = ord(str[0])

    for i in range(len(str)):
        if ord(str[i]) < minimum:
            minimum = ord(str[i])
        
        i += 1
    return chr(minimum)

def myInsert( str, i, ch ):
    #returns a new string with the ch inserted at the ith position
    if i >= len(str):
        return "Invalid Index"
    else:
        new_str = str[:i] + ch + str[i:]
        return new_str

def myPop( str, i ):
    #returns two new results: a string without the character at index i 
    #and a string that is the character at index i
    if i >= len(str):
        print("Invalid Index")
        print("(\'" + str + "\', None)")
    else:
        return str[:i] + str[i + 1:], str[i]

def myFind( str, ch ):
    #returns the index of the first occurence of the character in the string
    #if the character is not in the string, myFind returns -1
    for i in range(len(str)):
        if str[i] == ch:
            return i
    else:
        i += 1
    return -1

def myRFind( str, ch ):
    #returns the index of the last occurence of ch in str
    if ch not in str:
        return -1

    index = 0

    for i in range(len(str)):
        if str[i] == ch:
            if i > index:
                index = i
                i += 1
            else:
                i += 1
        else: 
            i += 1
    return index

def myRemove( str, ch ):
    #returns a new string with the first occurense of ch removed
    if ch in str:
        index = myFind(str, ch)
        return str[:index] + str[index+1:]
    else:
        return str

def myRemoveAll( str, ch ):
    #removes all the instances of ch within the given string
    if ch not in str:
        return str

    result = myRemove(str, ch)

    for i in range(len(result)):
        result = myRemove(result, ch)
        i += 1
    return result

def myReverse( str ):
    #returns the reverse of the str provided
    new_string = ""

    for i in range(1, (len(str) + 1)):
        new_string += str[-i]
        i += 1
    return new_string
