# File: FunctionExamples.py
# Student: Patrick Pichardo
# UT EID: pjp953
# Course: CS303E
#
# Date: 02/15/23
# Description of Program: his code defines several functions in Python to perform mathematical operations on numbers: 
# { sum3Numbers , multiply3Numbers , sumUpTo3Numbers , multiplyUpTo3Numbers , printInOrder , areaOfSquare , perimeterOfSquare , areaOfCircle , circumferenceOfCircle , bothFactors , squareAndCircle , factorial }
# Descriptions for each definition is below. 

import math
# Write a function to return the sum of three numbers. 
def sum3Numbers (x, y, z):
    n = x + y + z
    return n

# Write a function to return the product of three numbers.
def multiply3Numbers( x, y, z ):
    return x * y * z

# Write a function to return the sum of up to 3 numbers.  It should
# accept 1, 2, or 3 parameters.  Hint: any parameter not given
# should default to 0
def sumUpTo3Numbers (x, y = 0, z = 0):
    return x + y + z

# Write a function to return the product of up to 3 numbers.  It
# should accept 1, 2, or 3 parameters.  Hint: what should the
# default be in this case?
def multiplyUpTo3Numbers (x , y = 1, z = 1):
    return x * y * z

# Write a function that takes 2 numbers as input and prints them
# out in ascending order.  Make sure it works if they are equal
def printInOrder( x, y ):
    if x <= y:
        return x , y
    else:
        return y , x

# Write a function that returns the area of a square, given the length of a side.
# Print an error message if side is negative
def areaOfSquare( side ):
    if side < 0:
        print('Negative value entered')
    else:
        area = side ** 2
        return area
    


# Write a function that returns the perimeter of a square, given
# the length of a side.  Print an error message if side is negative.
def perimeterOfSquare( side ):
    if side < 0:
        print('Negative value entered')
    else:
        perm = 4 * side
        return perm

# Write a function that returns the area of a circle, given the
# radius.  Use math.pi. Print an error message if radius is negative
def areaOfCircle( radius ):
    if radius < 0:
        print('Negative value entered')
    else:
        area = math.pi * radius ** 2
        return area

# Write a function that returns the circumference of a circle given
# the radius.  Use math.pi. Print an error if radius is negative.
def circumferenceOfCircle( radius ):
    if radius < 0:
        print('Negative value entered')
    else:
        ccum = 2 * math.pi * radius
        return ccum
# Write a function: given parameters d1, d2, x, returns whether
# both d1 and d2 are both factors (evenly divide) x.  You can
# assume all values are integers.
def bothFactors( d1, d2, x ):
    if x % d1 == 0 and x % d2 == 0:
        return True
    else:
        return False
# Given a value x, compute and print out the area and circumference of a circle with
# radius x and the area and perimeter of a square with side x.  Use your previous 
# functions for these computations.  Leave a blank line above and below the printing.
def squareAndCircle( x ):
    area_sq = areaOfSquare(x)
    perm_sq = perimeterOfSquare(x)
    area_cir = areaOfCircle(x)
    ccum = circumferenceOfCircle(x)
    if area_sq is not None and perm_sq is not None and area_cir is not None and ccum is not None:
        print('Circle with radius', x ,'has:')
        print(f"    Area: {area_cir}")
        print(f"    Circumference: {ccum}")
        print("Square with side", x ,"has:")
        print(f"    Area: {area_sq}")
        print(f"    Perimeter = {perm_sq}")
# Write a function that returns the factorial of a positive
# integer n.  Use a for loop to compute the factorial.  You can
# assume the input is an integer, but print an error message if
# it's not positive and return None.
def factorial( n ):
    if n <= 0:
        print('Negative value entered')
        return
    end = 1
    for i in range(1, n+1):
        end *= i
    return end

r1 = sum3Numbers(5, 6, 7)
print(r1)
r2 = multiply3Numbers(3.2, 6, -19.123)
print(r2)
r3_1 = sumUpTo3Numbers( 12.9 )
print(r3_1)
r3_2 = sumUpTo3Numbers( 12.9, 3 )
print(r3_2)
r3_3 = sumUpTo3Numbers( 12.9, 3, 14.7 )
print(r3_3)
r4_1 = multiplyUpTo3Numbers( 12.9 )
print(r4_1)
r4_2 = multiplyUpTo3Numbers( 12.9, 3 )
print(r4_2)
r4_3 = multiplyUpTo3Numbers( 12.9, 3, -2.7 )
print(r4_3)
r5_1 = printInOrder( 2.1, -10 )
print(r5_1)
r5_2 = printInOrder( 2.1, 10 )
print(r5_2)
r6_1 = areaOfSquare( -10 )
print(r6_1)
r6_2 = areaOfSquare( 10 )
print(r6_2)
r7_1 = perimeterOfSquare( -10.2 )
print(r7_1)
r7_2 = perimeterOfSquare( 10.2 )
print(r7_2)
r8_1 = areaOfCircle( -10 )
print(r8_1)
r8_2 = areaOfCircle( 10 )
print(r8_2)
r9_1 = circumferenceOfCircle( -10 )
print(r9_1)
r9_2 = circumferenceOfCircle( 10 )
print(r9_2)
r10_1 = bothFactors(-2, 3, 20)
print(r10_1)
r10_2 = bothFactors(-2, 3, 30)
print(r10_2)
r11 = squareAndCircle( 10 )
print(r11)
r12_1 = factorial( -10 )
print(r12_1)
r12_2 = factorial( 10 )
print(r12_2)
