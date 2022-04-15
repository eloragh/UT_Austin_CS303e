# File: WordleAssistant.py
# Student: Eloragh Espie
# UT EID: eae2273
# Course Name: CS303E
# 
# Date: 04/12/2022
# Description of Program: This program contains several functions that return a list of words to the users specifications.

def createWordlist(filename): 
    """ Read words from the provided file and store them in a list.
    The file contains only lowercase ascii characters, are sorted
    alphabetically, one word per line. Filter out any words that are
    not 5 letters long, have duplicate letters, or end in 's'.  Return
    the list of words and the number of words as a pair. """
    ...

    file1 = open(filename, "r")
    file = file1.read()
    file_list = [word for word in file.split("\n")]

    word_check_1 = []

    #this for loop checks if the word is 5 or less letters and if it ends in an s
    for word in file_list:
        #To-Do FIX THIS SO THAT IT CHECKS FOR DUPLICATES
        if len(word) == 5:
            if word[-1] != "s":
                word_check_1.append(word)
                continue
            else:
                continue
        else:
            continue
    
    new_file_list = []

    #for each word in the set we have already checked
    for word in word_check_1:
        #first convert the word to a set
        word_set = set(word)
        #if the length of the set is equal to the length of the word, that means there were no duplicates
        #and this word can be included in the final wordle list.
        if len(word_set) == len(word):
            new_file_list.append(word)
    
    return new_file_list, len(new_file_list)
    
def containsAll(wordlist, include):
    """ Given your wordlist, return a set of all words from the wordlist
    that contain all of the letters in the string include.  
    """
    
    #create an empty set to add applicable words to
    word_set = set()
    
    #convert the include letters into a set for comparison
    include_set = set(include)

    for word in wordlist:
        #convert the word to a set
        set_word = set(word)

        #if the set of the word is a superset of the include set
        #add it to the empty set
        if set_word > include_set:
            word_set.add(word)
    
    return(word_set)

def containsNone(wordlist, exclude):
    """ Given your wordlist, return a set of all words from the wordlist
    that do not contain any of the letters in the string exclude.  
    """

    wordlist_set = set()
    
    #create a list of all the excluded letters
    list_exclude = [item for item in exclude]

    for word in wordlist:
        counter = 0 
        for letter in list_exclude:
            if letter in word:
                counter += 1
        
        if counter == 0:
            wordlist_set.add(word)
        
        counter = 0
    return wordlist_set
    
    '''
    excluded_words = []

    #loop through the words in the word list
    for word in wordlist:
        for i in range(len(list_exclude)):
            #check if any elements of the exclude list are in the words
            if list_exclude[i] in word:
                #if they are append them to a holding list
                excluded_words.append(word)
    
    final_set = set()

    #loop through the words again
    for word in wordlist:
        #if the word is not among the words that had the excluded letters, add it to the final set
        if word not in excluded_words:
            final_set.add(word)
    
    #return the set
    return final_set
    '''

def containsAtPositions(wordlist, posInfo):
    """ posInfo is a dictionary that maps letters to positions.
    You can assume that the positions are in [0..4].  Return a set of
    all words from the wordlist that contain the letters from the
    dictionary at the indicated positions. For example, given posInfo
    {'a': 0, 'y': 4}.   This function might return the set:
    {'angry', 'aptly', 'amply', 'amity', 'artsy', 'agony'}. """
    
    final_set = set()

    #loop through the words
    for word in wordlist:
        #initialize a counter
        count = 0
        #loop through the keys
        for key in posInfo:
            #if the word at the correct index is equal to the key
            if word[posInfo[key]] == key:
                #add to the count
                count += 1

        #if the word satisfies all the requirements of posInfo, the count should equal the length of posInfo   
        if count == len(posInfo):
            #if it does, append the word to final set
            final_set.add(word)
        
        #reset the counter, continue the loop
        count = 0
    
    return final_set

def getPossibleWords(wordlist, posInfo, include, exclude):
    """ Finally, given a wordlist, dictionary posInfo, and
    strings include and exclude, return the set of all words from 
    the wordlist that contains the words that satisfy all of 
    the following:
    * has letters in positions indicated in posInfo
    * contains all letters from string include
    * contains none of the letters from string exclude.
    """

    posInfo_set = containsAtPositions(wordlist, posInfo)

    include_set = containsAll(posInfo_set, include)

    exclude_set = containsNone(include_set, exclude)

    return exclude_set
