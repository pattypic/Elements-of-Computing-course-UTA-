# File: Handicap.py s
# Student: Patrick Pichardo
# UT EID: pjp953
# Course: CS303E
#
# Date: 01/25/2023
# Description of Program: okay, so basicly you put in your name and it gets saved in 'name' variable that which will later be printed at the end. you then input your 3 scores saved in there respective variables. After that it gives you the average that is then ran through the code that prevents numbers less than 0 to then spit out the last 2 statements. (:

name = input("Enter bowler's name: ")
G1 = int(input("Enter Game 1: "))
G2 = int(input("Enter Game 2: "))
G3 = int(input("Enter Game 3: "))

T = G1 + G2 + G3
Avg = int(T / 3)
hacp1 = (200 - Avg) * .8
hacp2 = int(max(0 , hacp1))

print("----------------------------------")
print("Handicap report for {}:".format(name))
print("     {}'s average is:".format(name), Avg)
print("     {}'s handicap is:".format(name), hacp2)
print()
print("It's time to Bowl!")



