# File: Project1.py
# Student: Eloragh Espie
# UT EID: eae2273
# Course Name: CS303E
# 
# Date: 03/05/2022
# Description of Program: This program is a converter that can convert English to metric units and vice versa

LINE = "------------------------------------------------------------"
ONE = "1"
TWO = "2"
THREE = "3"
ERROR = "ERROR: Answer must be 1, 2 or 3. Try again."

def welcome():
    print("")
    print("Welcome to the English/Metric conversion utility.")
    print("")
    print("This utility allows you to convert between English units")
    print("(miles, feet, inches) and metric units (kilometers, meters,")
    print("centimeters).")
    print("")
    print(LINE)

def unitFrom(english_or_metric):
    unit_from = 0
#English to metric units
    if english_or_metric == ONE:
        print("Select English units to convert to metric equivalent:")
        print("   For miles type:  1")
        print("   For feet type:   2")
        print("   For inches type: 3")
        print("")

        unit_from = input("   Choose English units to convert (1, 2 or 3): ")

        valid = False
        if unit_from == ONE:
            valid = True
        elif unit_from == TWO:
            valid = True
        elif unit_from == THREE:
            valid = True

        while valid == False:
            print("")
            print(ERROR)

            print("")
            print("Select English units to convert to metric equivalent:")
            print("   For miles type:  1")
            print("   For feet type:   2")
            print("   For inches type: 3")
            print("")

            unit_from = input("   Choose English units to convert (1, 2 or 3): ")
        
            if unit_from == ONE:
                valid = True
            elif unit_from == TWO:
                valid = True
            elif unit_from == THREE:
                valid = True
        return unit_from
#metric to English units
    elif english_or_metric == TWO:
        print("Select metric units to convert to English equivalent:")
        print("   For kilometers type:  1")
        print("   For meters type:      2")
        print("   For centimeters type: 3")
        print("")

        unit_from = input("   Choose metric units to convert (1, 2 or 3): ")

        valid = False
        if unit_from == ONE:
            valid = True
        elif unit_from == TWO:
            valid = True
        elif unit_from == THREE:
            valid = True

        while valid == False:
            print("")
            print(ERROR)

            print("")
            print("Select metric units to convert to English equivalent:")
            print("   For kilometers type:  1")
            print("   For meters type:      2")
            print("   For centimeters type: 3")
            print("")

            unit_from = input("   Choose metric units to convert (1, 2 or 3): ")
        
            if unit_from == ONE:
                valid = True
            elif unit_from == TWO:
                valid = True
            elif unit_from == THREE:
                valid = True
        return unit_from

def unitTo(english_or_metric):

    if english_or_metric == ONE:
        print("")
        print("Convert to which metric units:")
        print("   For kilometers type:  1")
        print("   For meters type:      2")
        print("   For centimeters type: 3")
        print("")

        unit_to = input("   Choose target metric units (1, 2 or 3): ")

        valid = False
        if unit_to == ONE:
            valid = True
        elif unit_to == TWO:
            valid = True
        elif unit_to == THREE:
            valid = True

        while valid == False:
            print("")
            print(ERROR)

            print("")
            print("Convert to which metric units:")
            print("   For kilometers type:  1")
            print("   For meters type:      2")
            print("   For centimeters type: 3")
            print("")

            unit_to = input("   Choose target metric units (1, 2 or 3): ")
        
            if unit_to == ONE:
                valid = True
            elif unit_to == TWO:
                valid = True
            elif unit_to == THREE:
                valid = True
        return unit_to
    
    elif english_or_metric == TWO:
        print("")
        print("Convert to which English units: ")
        print("   For miles type:  1")
        print("   For feet type:   2")
        print("   For inches type: 3")
        print("")

        unit_to = input("   Choose target English units (1, 2 or 3): ")

        valid = False
        if unit_to == ONE:
            valid = True
        elif unit_to == TWO:
            valid = True
        elif unit_to == THREE:
            valid = True

        while valid == False:
            print("")
            print(ERROR)

            print("")
            print("Convert to which English units: ")
            print("   For miles type:  1")
            print("   For feet type:   2")
            print("   For inches type: 3")
            print("")

            unit_to = input("   Choose target English units (1, 2 or 3): ")
        
            if unit_to == ONE:
                valid = True
            elif unit_to == TWO:
                valid = True
            elif unit_to == THREE:
                valid = True
        
        #return unit_to
    return unit_to

def find_amount(english_or_metric, unit_from, unit_to):

    #if we are converting from English to metric
    if english_or_metric == ONE:  
        #if the starting unit is miles
        if unit_from == ONE:
            if unit_to == ONE:
                amount = float(input("Enter the number of miles to convert to kilometers: "))
            elif unit_to == TWO:
                amount = float(input("Enter the number of miles to convert to meters: "))
            elif unit_to == THREE:
                amount = float(input("Enter the number of miles to convert to centimeters: "))
        #if the starting unit is feet        
        elif unit_from == TWO:
            if unit_to == ONE:
                amount = float(input("Enter the number of feet to convert to kilometers: "))
            elif unit_to == TWO:
                amount = float(input("Enter the number of feet to convert to meters: "))
            elif unit_to == THREE:
                amount = float(input("Enter the number of feet to convert to centimeters: "))
        
        #if the starting unit is inches
        elif unit_from == THREE:
            if unit_to == ONE:
                amount = float(input("Enter the number of inches to convert to kilometers: "))
            elif unit_to == TWO:
                amount = float(input("Enter the number of inches to convert to meters: "))
            elif unit_to == THREE:
                amount = float(input("Enter the number of inches to convert to centimeters: "))

    #if we are converting from metric to English            
    elif english_or_metric == TWO:
        #if we are converting from kilometers
        if unit_from == ONE:
            if unit_to == ONE:
                amount = float(input("Enter the number of kilometers to convert to miles: " ))
            elif unit_to == TWO:
                amount = float(input("Enter the number of kilometers to convert to feet: "))
            elif unit_to == THREE: 
                amount = float(input("Enter the number of kilometers to convert to inches: "))
        #if we are converting from meters
        elif unit_from == TWO:
            if unit_to == ONE:
                amount = float(input("Enter the number of meters to convert to miles: " ))
            elif unit_to == TWO:
                amount = float(input("Enter the number of meters to convert to feet: "))
            elif unit_to == THREE: 
                amount = float(input("Enter the number of meters to convert to inches: "))
        #if we are converting from centimeters
        elif unit_from == THREE:
            if unit_to == ONE:
                amount = float(input("Enter the number of centimeters to convert to miles: " ))
            elif unit_to == TWO:
                amount = float(input("Enter the number of centimeters to convert to feet: "))
            elif unit_to == THREE: 
                amount = float(input("Enter the number of centimeters to convert to inches: "))

    return amount
        
def common_term_conversion(english_or_metric, unit_from, amount):

    #converted_unit = 0
    #converted_amount = 0

    #getting english units to common unit
    if english_or_metric == ONE:
        #ONE refers to miles
        if unit_from == ONE:
            converted_unit = amount * 63360
        #TWO refers to feet
        elif unit_from == TWO:
            converted_unit = amount * 12
        #any other case, unit_from is inches
        else:
            converted_unit = amount
        #converts to centimeters
        converted_amount = converted_unit * 2.54

    elif english_or_metric == TWO:
        #ONE refers to kilometers
        if unit_from == ONE:
            converted_unit = amount * 100000
        #TWO refers to meters
        elif unit_from == TWO:
            converted_unit = amount * 100
        #any other case, unit_from is centimeters
        else:
            converted_unit = amount
        #converts to inches
        converted_amount = converted_unit / 2.54
    
    return converted_amount

def final_conversion(amount, english_or_metric, conversion, unit_from, unit_to):
    result = 0
    #if we are converting English units to Metric units
    if english_or_metric == ONE:
        #if we are converting from miles
        if unit_from == ONE:
            #if we are converting to kilometers
            if unit_to == ONE:
                finalConversion = conversion / 100000
                result = ("RESULT: " + str(amount) + " miles = " + str(format(finalConversion, ".3f")) + " kilometers")
            #if we are converting to meters
            elif unit_to == TWO:
                finalConversion = conversion / 100
                result = ("RESULT: " + str(amount) + " miles = " + str(format(finalConversion, ".3f")) + " meters")
            #if we are converting to centimeters
            elif unit_to == THREE:
                finalConversion = conversion
                result = ("RESULT: " + str(amount) + " miles = " + str(format(finalConversion, ".3f")) + " centimeters")
        #if we are converting from feet
        elif unit_from == TWO:
            #if we are converting to kilometers
            if unit_to == ONE:
                finalConversion = conversion / 100000
                result = ("RESULT: " + str(amount) + " feet = " + str(format(finalConversion, ".3f")) + " kilometers")
            #if we are converting to meters
            elif unit_to == TWO:
                finalConversion = conversion / 100
                result = ("RESULT: " + str(amount) + " feet = " + str(format(finalConversion, ".3f")) + " meters")
            #if we are converting to centimeters
            elif unit_to == THREE:
                finalConversion = conversion
                result = ("RESULT: " + str(amount) + " feet = " + str(format(finalConversion, ".3f")) + " centimeters")
        #if we are converting from feet
        elif unit_from == THREE:
            #if we are converting to kilometers
            if unit_to == ONE:
                finalConversion = conversion / 100000
                result = ("RESULT: " + str(amount) + " inches = " + str(format(finalConversion, ".3f")) + " kilometers")
            #if we are converting to meters
            elif unit_to == TWO:
                finalConversion = conversion / 100
                result = ("RESULT: " + str(amount) + " inches = " + str(format(finalConversion, ".3f")) + " meters")
            #if we are converting to centimeters
            elif unit_to == THREE:
                finalConversion = conversion
                result = ("RESULT: " + str(amount) + " inches = " + str(format(finalConversion, ".3f")) + " centimeters")
    #if we are converting metric units to English
    elif english_or_metric == TWO:
        #if we are converting from kilometers
        if unit_from == ONE:    
            #if we are converting to miles
            if unit_to == ONE:
                finalConversion = conversion / 63360
                result = ("RESULT: " + str(amount) + " kilometers = " + str(format(finalConversion, ".3f")) + " miles")
            #if we are converting to feet
            elif unit_to == TWO:
                finalConversion = conversion / 12
                result = ("RESULT: " + str(amount) + " kilometers = " + str(format(finalConversion, ".3f")) + " feet")
            #if we are converting to inches
            elif unit_to == THREE:
                finalConversion = conversion
                result = ("RESULT: " + str(amount) + " kilometers = " + str(format(finalConversion, ".3f")) + " inches")
        #if we are converting from meters
        elif unit_from == TWO:    
            #if we are converting to miles
            if unit_to == ONE:
                finalConversion = conversion / 63360
                result = ("RESULT: " + str(amount) + " meters = " + str(format(finalConversion, ".3f")) + " miles")
            #if we are converting to feet
            if unit_to == TWO:
                finalConversion = conversion / 12
                result = ("RESULT: " + str(amount) + " meters = " + str(format(finalConversion, ".3f")) + " feet")
            #if we are converting to inches
            if unit_to == THREE:
                finalConversion = conversion
                result = ("RESULT: " + str(amount) + " meters = " + str(format(finalConversion, ".3f")) + " inches")
        #if we are converting from centimeters
        elif unit_from == THREE:    
            #if we are converting to miles
            if unit_to == ONE:
                finalConversion = conversion / 63360
                result = ("RESULT: " + str(amount) + " centimeters = " + str(format(finalConversion, ".3f")) + " miles")
            #if we are converting to feet
            elif unit_to == TWO:
                finalConversion = conversion / 12
                result = ("RESULT: " + str(amount) + " centimeters = " + str(format(finalConversion, ".3f")) + " feet")
            #if we are converting to inches
            elif unit_to == THREE:
                finalConversion = conversion
                result = ("RESULT: " + str(amount) + " centimeters = " + str(format(finalConversion, ".3f")) + " inches")
    
    return result

def main():

    print("")
    print("Which direction would you like to convert:")
    print("   For English to Metric type: 1")
    print("   For Metric to English type: 2")
    print("   To Quit type:               3")
    print("")

    english_or_metric = input("   Input your answer (1, 2 or 3): ")
    print("")

    if english_or_metric == THREE:
        print("Thanks for using our converter. Goodbye!")
        print("")
        return
    
    if int(english_or_metric) > 3:
        print(ERROR)
        main()

    elif int(english_or_metric) < 1:
        print(ERROR)
        main()

    while english_or_metric == ONE or TWO:

        unit_from = unitFrom(english_or_metric)
        unit_to = unitTo(english_or_metric)

        print("")

        amount = find_amount(english_or_metric, unit_from, unit_to)
        conversion = common_term_conversion(english_or_metric, unit_from, amount)
        final_con = final_conversion(amount, english_or_metric, conversion, unit_from, unit_to)

        print("")
        print(final_con)
        print("")

        print(LINE)
        print("")


        print("Which direction would you like to convert:")
        print("   For English to Metric type: 1")
        print("   For Metric to English type: 2")
        print("   To Quit type:               3")
        print("")
        
        english_or_metric = input("   Input your answer (1, 2 or 3): ")
        print("")

        if english_or_metric == THREE:
            print("Thanks for using our converter. Goodbye!")
            print("")
            return

        while int(english_or_metric) > 3:
            print(ERROR)
            main()
            
        while int(english_or_metric) <= 0:
            print(ERROR)
            main

welcome()
main()