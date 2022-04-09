# File: ControlGame.py
# Student: Eloragh Espie
# UT EID: eae2273
# Course Name: CS303E
# 
# Date: 04/04/2022
# Description of Program: This program is a class that runs a game called the Control Game


class ControlGame:

    def __init__(self, turnsToPlay = 64):
        # This initializes the game with an empty board, the current
        # player set to 'Red' and the number of turns
        # specified by the user (defaults to 64).  turnsToPlay must
        # be an even number in the range [2..64].
        self.headerRow = HEADER_ROW = [" ", 0, 1, 2, 3, 4, 5, 6, 7]
        self.row0 = [0, ".", ".", ".", ".", ".", ".", ".", "."]
        self.row1 = [1, ".", ".", ".", ".", ".", ".", ".", "."]
        self.row2 = [2, ".", ".", ".", ".", ".", ".", ".", "."]
        self.row3 = [3, ".", ".", ".", ".", ".", ".", ".", "."]
        self.row4 = [4, ".", ".", ".", ".", ".", ".", ".", "."]
        self.row5 = [5, ".", ".", ".", ".", ".", ".", ".", "."]
        self.row6 = [6, ".", ".", ".", ".", ".", ".", ".", "."]
        self.row7 = [7, ".", ".", ".", ".", ".", ".", ".", "."]
        self.condenseList = [self.row0, self.row1, self.row2, self.row3, self.row4, self.row5, self.row6, self.row7]
        self.__currentPlayer = "Red"
        self.__turnsToPlay = turnsToPlay
        pass
    
    def __str__(self):
        # Permit displaying the header "Current board is:" following by the 
        # board.
        print("\n" + "Current board is:")
        print("", end = "")

        for element in self.headerRow:
            print(element, end = "  ")
        print("")

        for lst in self.condenseList:
            for element in lst:
                print(element, end = "  ")
            print("")
        return ""

    def getCurrentPlayer(self):

        return self.__currentPlayer

    def swapCurrentPlayer(self):
        # If the current player is 'Red', set it to 'Blue', and 
        # vice versa.

        if self.__currentPlayer == "Red":
            self.__currentPlayer = "Blue"
        elif self.__currentPlayer == "Blue":
            self.__currentPlayer = "Red"
    
    def getBoardState(self):
        print("", end = "")

        for element in self.headerRow:
            print(element, end = "  ")
        print("")

        for lst in self.condenseList:
            for element in lst:
                print(element, end = "  ")
            print("")
    
    def takeTurn(self, row, col):
        # This attempts to add the current player's token to cell
        # (row, col).  Check whether the cell is legal and is not
        # occupied.  If the checks pass add the current player's
        # token to that cell.  Finally, return a Boolean value 
        # indicating whether or not the turn occurred.

        if row > 7 or row < 0:
            print("Invalid turn. Location is out of bounds.")
            return False
        
        if col > 7 or col < 0:
            print("Invalid turn. Location is out of bounds.")
            return False
        
        if self.__currentPlayer == "Red":
            #check what the row is and find the appropriate list
            #then check what the column is and add one before replacing the . with an R or a B
            if row == 0:
                if self.row0[col + 1] == "B":
                    print("Invalid turn. Cannot place piece on occupied cell.")
                    return False
                else:
                    self.row0[col + 1] = "R"
            elif row == 1:
                if self.row1[col + 1] == "B":
                    print("Invalid turn. Cannot place piece on occupied cell.")
                    return False
                else:
                    self.row1[col + 1] = "R"
            elif row == 2:
                if self.row2[col + 1] == "B":
                    print("Invalid turn. Cannot place piece on occupied cell.")
                    return False
                else:
                    self.row2[col + 1] = "R"
            elif row == 3:
                if self.row3[col + 1] == "B":
                    print("Invalid turn. Cannot place piece on occupied cell.")
                    return False
                else:
                    self.row3[col + 1] = "R"
            elif row == 4:
                if self.row4[col + 1 ]== "B":
                    print("Invalid turn. Cannot place piece on occupied cell.")
                    return False
                else:
                    self.row4[col + 1] = "R"
            elif row == 5:
                if self.row5[col + 1] == "B":
                    print("Invalid turn. Cannot place piece on occupied cell.")
                    return False
                else:
                    self.row5[col + 1] = "R"
            elif row == 6:
                if self.row6[col + 1] == "B":
                    print("Invalid turn. Cannot place piece on occupied cell.")
                    return False
                else:
                    self.row6[col + 1] = "R"
            elif row == 7:
                if self.row7[col + 1] == "B":
                    print("Invalid turn. Cannot place piece on occupied cell.")
                    return False
                else:
                    self.row7[col + 1] = "R"

        elif self.__currentPlayer == "Blue":
            if row == 0:
                if self.row0[col + 1] == "R":
                    print("Invalid turn. Cannot place piece on occupied cell.")
                    return False
                else:
                    self.row0[col + 1] = "B"
            elif row == 1:
                if self.row1[col + 1] == "R":
                    print("Invalid turn. Cannot place piece on occupied cell.")
                    return False
                else:
                    self.row1[col + 1] = "B"
            elif row == 2:
                if self.row2[col + 1] == "R":
                    print("Invalid turn. Cannot place piece on occupied cell.")
                    return False
                else:
                    self.row2[col + 1] = "B"
            elif row == 3:
                if self.row3[col + 1] == "R":
                    print("Invalid turn. Cannot place piece on occupied cell.")
                    return False
                else:
                    self.row3[col + 1] = "B"
            elif row == 4:
                if self.row4[col + 1] == "R":
                    print("Invalid turn. Cannot place piece on occupied cell.")
                    return False
                else:
                    self.row4[col + 1] = "B"
            elif row == 5:
                if self.row5[col + 1] == "R":
                    print("Invalid turn. Cannot place piece on occupied cell.")
                    return False
                else:
                    self.row5[col + 1] = "B"
            elif row == 6:
                if self.row6[col + 1] == "R":
                    print("Invalid turn. Cannot place piece on occupied cell.")
                    return False
                else:
                    self.row6[col + 1] = "B"
            elif row == 7:
                if self.row7[col + 1] == "R":
                    print("Invalid turn. Cannot place piece on occupied cell.")
                    return False
                else:
                    self.row7[col + 1] = "B"
                
        self.swapCurrentPlayer()
        return True    
    
    def cellCounter(self):
        #to-do fix this
        r_cell_counter = 0
        b_cell_counter = 0

        for i in range(0, 7):
            #there are 7 sub lists in condenseList; each of them represent a row in the board
            #we loop through each of these to check for cell points
            row = self.condenseList[i]
            #there are nine total elements in each list, but we only want to check the periods
            #those are stored in elements 1-9
            for x in range(1,8):
                col = row[x]
                #rows 1 - 6 colums 2 - 8 will all have the same options
                #you can check up, down, left, and right on all of the elements within those rows
                #we'll build a statement for all of those rows first
                #first statement will include the columns with the most win conditions - 2 - 7
                #other two statements will address columns with the second most win conditions - 1 and 8
                if 0 < i < 7:
                    #this covers everything in rows 1 - 6
                    if 1 < x < 8:
                        #check if the point in question has an element
                        if col == "R":
                            #if the left and right rows are both the same as the column
                            if row[x + 1] == "R" and row[x - 1] == "R":
                                #add one to the counter variable and return to the top of the loop
                                #if the cell meets these requirements, it will have already proven ownership of the cell
                                #so there's no need to check the other if statements
                                r_cell_counter += 1
                                continue
                            #if either the left or right neighbor = R and either the top or bottom neighbor = R
                            elif ((row[x + 1] == "R") or (row[x-1] == "R")) and ((self.condenseList[i + 1][x] == "R") or (self.condenseList[i - 1][x] == "R")):
                                #this proves ownership of the cell, we add one to the counter and restart the loop
                                r_cell_counter += 1
                                continue
                            #if both the top and bottom neighbor == R
                            elif (self.condenseList[i + 1][x] == "R") and (self.condenseList[i - 1][x] == "R"):
                                #this proves ownership of the cell, we add one to the counter and restart the loop
                                r_cell_counter += 1
                                continue
                        if col == "B":
                            if row[x + 1] == "B" and row[x - 1] == "B":
                                #add one to the counter variable and return to the top of the loop
                                #if the cell meets these requirements, it will have already proven ownership of the cell
                                #so there's no need to check the other if statements
                                b_cell_counter += 1
                                continue
                            #if either the left or right neighbor = R and either the top or bottom neighbor = R
                            elif ((row[x + 1] == "B") or (row[x-1] == "B")) and ((self.condenseList[i + 1][x] == "B") or (self.condenseList[i - 1][x] == "B")):
                                #this proves ownership of the cell, we add one to the counter and restart the loop
                                b_cell_counter += 1
                                continue
                            #if both the top and bottom neighbor == R
                            elif (self.condenseList[i + 1][x] == "B") and (self.condenseList[i - 1][x] == "B"):
                                #this proves ownership of the cell, we add one to the counter and restart the loop
                                b_cell_counter += 1
                                continue
                    if x == 1:
                        if col == "R":
                            #if the right cell and the top or the bottom cell are equivalent to the initial cell
                            if row[x+1] == "R" and ((self.condenseList[i+1][x] == "R") or (self.condenseList[i-1][x] == "R")):
                                r_cell_counter += 1
                                continue
                            #the only other win condition, if the first one is not true, is that both the top and bottom neighbors are the same as the initial cell
                            elif self.condenseList[i+1][x] == "R" and self.condenseList[i-1][x] == "R":
                                r_cell_counter += 1
                                continue
                        if col == "B":
                            #if the right cell and the top or the bottom cell are equivalent to the initial cell
                            if row[x+1] == "B" and ((self.condenseList[i+1][x] == "B") or (self.condenseList[i-1][x] == "B")):
                                r_cell_counter += 1
                                continue
                            #the only other win condition, if the first one is not true, is that both the top and bottom neighbors are the same as the initial cell
                            elif self.condenseList[i+1][x] == "B" and self.condenseList[i-1][x] == "B":
                                r_cell_counter += 1
                                continue
                    if x == 8:
                        if col == "R":
                            #if the left cell and the top or the bottom cell are equivalent to the initial cell
                            if row[x-1] == "R" and ((self.condenseList[i+1][x] == "R") or (self.condenseList[i-1][x] == "R")):
                                r_cell_counter += 1
                                continue
                            #the only other win condition, if the first one is not true, is that both the top and bottom neighbors are the same as the initial cell
                            elif self.condenseList[i+1][x] == "R" and self.condenseList[i-1][x] == "R":
                                r_cell_counter += 1
                                continue
                        if col == "B":
                            #if the left cell and the top or the bottom cell are equivalent to the initial cell
                            if row[x-1] == "B" and ((self.condenseList[i+1][x] == "B") or (self.condenseList[i-1][x] == "B")):
                                r_cell_counter += 1
                                continue
                            #the only other win condition, if the first one is not true, is that both the top and bottom neighbors are the same as the initial cell
                            elif self.condenseList[i+1][x] == "B" and self.condenseList[i-1][x] == "B":
                                r_cell_counter += 1
                                continue    
                #in the first row, the first and last columns each only have one ownership condition
                elif i == 0:
                    #if we are working in the first column
                    if x == 1:
                        if col == "R":
                            #if the cell to the right and the cell below are the same as the original cell
                            #add one to the counter
                            if row[x+1] == "R" and self.condenseList[i+1][x] == "R":
                                r_cell_counter += 1
                                continue
                        elif col == "B":
                            if row[x+1] == "B" and self.condenseList[i+1][x] == "B":
                                b_cell_counter += 1
                                continue
                    #if we are working in the last column
                    elif x == 8:
                        #if the cell to the left and the cell below are the same as the original cell
                        #add one to the counter
                        if col == "R":
                            #if the left and right rows are the same as the initial row
                            if row[x-1] == "R" and self.condenseList[i+1][x] == "R":
                                #they meet the condition
                                r_cell_counter += 1
                                continue
                        elif col == "B":
                            if row[x-1] == "B" and self.condenseList[i+1][x] == "B":
                                b_cell_counter += 1
                                continue
                    elif 1 < x < 8:
                        if col == "R":
                            if row[x+1] == "R" and row[x-1] == "R":
                                r_cell_counter += 1
                                continue
                            elif self.condenseList[i+1][x] == "R" and ((row[x+1] == "R") or (row[x-1] == "R")):
                                r_cell_counter += 1
                                continue
                        if col == "B":
                            if row[x+1] == "B" and row[x-1] == "B":
                                b_cell_counter += 1
                                continue
                            elif self.condenseList[i+1][x] == "B" and ((row[x+1] == "B") or (row[x-1] == "B")):
                                b_cell_counter += 1
                                continue
                elif i == 7:
                    if x == 1:
                        if col == "R":
                            #if the cell to the right and the cell above are the same as the original cell
                            #add one to the counter
                            if row[x+1] == "R" and self.condenseList[i-1][x] == "R":
                                r_cell_counter += 1
                                continue
                        if col == "B":
                            #if the cell to the right and the cell above are the same as the original cell
                            #add one to the counter
                            if row[x+1] == "B" and self.condenseList[i-1][x] == "B":
                                b_cell_counter += 1
                                continue
                    elif x == 8:
                        if col == "R":
                            #if the cell to the left and the cell above are the same as the original cell
                            #add one to the counter
                            if row[x-1] == "R" and self.condenseList[i-1][x] == "R":
                                r_cell_counter += 1
                                continue
                        if col == "B":
                            #if the cell to the left and the cell above are the same as the original cell
                            #add one to the counter
                            if row[x-1] == "B" and self.condenseList[i-1][x] == "B":
                                b_cell_counter += 1
                                continue
                    elif 1 < x < 8:
                        if col == "R":
                            if row[x+1] == "R" and row[x-1] == "R":
                                r_cell_counter += 1
                                continue
                            elif self.condenseList[i-1][x] == "R" and ((row[x+1] == "R") or (row[x-1] == "R")):
                                r_cell_counter += 1
                                continue
                        if col == "B":
                            if row[x+1] == "B" and row[x-1] == "B":
                                b_cell_counter += 1
                                continue
                            elif self.condenseList[i-1][x] == "B" and ((row[x+1] == "B") or (row[x-1] == "B")):
                                b_cell_counter += 1
                                continue

        return(r_cell_counter, b_cell_counter)

    def rowCounter(self):
        b_row = 0
        r_row = 0 

        #loop through each list
        for lst in self.condenseList:
            #initialize a counter for comparison
            b_row_count = 0
            r_row_count = 0

            #check each element in the list and see if it holds an R or a B
            #if it does, add one to the respective comparison variable
            for element in lst:
                if element == "B":
                    b_row_count += 1
                elif element == "R":
                    r_row_count += 1

            #at then end of one list, check which count from the comparison variables is larger
            #whoever has the more items in a row wins and gets a point added
            if b_row_count > r_row_count:
                b_row += 1
            elif r_row_count > b_row_count:
                r_row += 1


            #print(r_row, 0, 0, 0, b_row)
        
        return r_row, b_row
    
    def colCounter(self):
        r_col_counter = 0
        b_col_counter = 0

        #for i in the range 1 - 8, we don't want to include the first index item
        for i in range(1, 9):
            #initialize counters to compare which player has more items in a column
            r_counter = 0
            b_counter = 0
            #loop through each of the lists
            for lst in self.condenseList:
                #if lst[i] is R, add to the comparison counter
                if lst[i] == "R":
                    r_counter += 1
                #if lst[i] is B, add to the comparison counter
                elif lst[i] == "B":
                    b_counter += 1
            
            #check which way the comparison counter leans
            if r_counter > b_counter:
                r_col_counter += 1
            elif b_counter > r_counter:
                b_col_counter += 1
            #in case comparisons are equal
            #elif r_counter == b_counter:


            #continue to loop through the indexes
            #i += 1 in python iterators that are declared following for... are au
        #return the column points
        return r_col_counter, b_col_counter
      
    def getScore(self):
        # Calculate the sum of rows, columns, and cells controlled by
        # Red and Blue.  Return this as a pair (red, blue).  This is
        # the most complicated method, so it's probably a good idea 
        # to write subsidiary functions for this

        r_cell_counter, b_cell_counter = self.cellCounter()
        
        r_row_counter, b_row_counter = self.rowCounter()

        r_col_counter, b_col_counter = self.colCounter()

        r_final_points = r_cell_counter + r_row_counter + r_col_counter
        b_final_points = b_cell_counter + b_row_counter + b_col_counter

        return r_final_points, b_final_points
