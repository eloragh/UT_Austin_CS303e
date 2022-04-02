# File: Payroll.py
# Student: Eloragh Espie    
# UT EID: eae2273
# Course Name: CS303E
# 
# Date: 02/11/2022
# Description of Program: This program takes input about an employee and outputs a pay statement.

from os import stat


def main ():
    print("")
    #this first section collects information about a given employee from the user
    employee_name = str(input("Enter employee's name: "))
    weekly_hours = float(input("Number of hours worked in a week: "))
    hourly_pay_rate = float(input("Hourly pay rate: "))
    #these last two lines collect tax information
    federal_tax = float(input("Federal tax witholding rate: "))
    state_tax = float(input("State tax witholding rate: "))

    #this section calculates gross pay, federal witholdings, state witholdings, total deducations, and the final net pay for the pay statement
    gross_pay = weekly_hours * hourly_pay_rate
    federal_witholding = gross_pay * federal_tax
    state_witholding = gross_pay * state_tax
    deductions = federal_witholding + state_witholding
    net_pay = gross_pay - deductions

    #this section prints and organizes the information using floats and the format function
    print("")
    print("Employee Name: " + employee_name)
    print("Hours worked: " + (format(weekly_hours, ".1f")))
    print("Pay Rate: $" + (format(hourly_pay_rate, ".2f")))
    print("Gross Pay: $" +(format(+ gross_pay, ".2f")))
    print("Deductions: ")
    print("  Federal Witholding (" + (format(federal_tax, ".1%") + "): $" + (format (federal_witholding, ".2f"))))
    print("  State Witholding (" + (format(state_tax, ".1%") + "): $" + (format (state_witholding, ".2f"))))
    print("  Total Deductions: $" +(format(deductions, ".2f")))
    print("Net Pay: $" + (format(net_pay, ".2f")))

main()
