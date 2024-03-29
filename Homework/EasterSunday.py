# File: EasterSunday.py
# Student: Eloragh Espie	
# UT EID: eae2273
# Course Name: CS303E
# 
# Date: 02/04/2022
# Description of Program: This program is an algorithm that can identify the date of Easter Sunday for any given year inputted by the user.

y = int(input("Enter year: "))

a = y % 19

b = y // 100

c = y % 100

d = b // 4

e = b % 4

g = (8 * 6 + 14) // 25

h = (19 * a + b - d - g +15) % 30

j = c // 4

k = c % 4 

m = (a + 11 * h) // 319

r = (2* e + 2 * j - k -h + m + 32) % 7

n = (h - m + r + 90) // 25

p = (h - m + r + n + 19) % 32

print("In " + str(y) + " Easter Sunday is on month " + str(n) + " and day " + str(p))
