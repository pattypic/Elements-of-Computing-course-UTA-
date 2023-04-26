# File: Project2.py
# Student: Patrick Pichardo
# UT EID: pjp953
# Course: CS303E
# 
# Date: 03/25/2023
# Description of Program: Format for project is below and comments to each function is below. 
# Program header and description, Imports, Constants, ToyCar class definition, Other function definitions (including randomDrive, goto, gasStation, and gasUp), Main program (including test cases and output).

# Imports
import random

# Constants
# added this list to make things easier
DIR_NAMES = {0: "East", 90: "North", 180: "South", 270: "West"}
EAST = 0
NORTH = 90
SOUTH = 180
WEST = 270

# ToyCar class definition
class ToyCar:

    def __init__(self, x = 0, y = 0, d = 0):
        # the initializer for the class (include default values; you can assume that the arguments are integers, but validate that d is a legal value)
        # x is the initial x-coordinate
        # y is the initial y-coordinate
        # d is the initial direction
        if d not in [EAST, NORTH, SOUTH, WEST]:
            print("Invalid direction")
            d = EAST
        self.__x = x
        self.__y = y
        self.__d = d

    def __str__(self):
        # string representation of the car information
        return f"Your car is at location ({str(self.__x)}, {str(self.__y)}), heading {DIR_NAMES[self.__d]}"

    def setDir(self, n):
        # validate the parameter and then set the direction accordingly
        if n not in [EAST, NORTH, SOUTH, WEST]:
            print("Invalid direction")
            n = EAST
        self.__d = n

    def getDir(self):
        # return the direction (one of 0, 90, 180, 270)
        return DIR_NAMES[self.__d]

    def getX(self):
        # return the X coordinate of the car's location
        return self.__x

    def getY(self):
        # return the Y coordinate of the car's location
        return self.__y

    def turnLeft(self):
        # change direction 90 degrees to the left
        self.__d = (self.__d + 180) % 360
        print(f'DEBUG: turning {DIR_NAMES[self.__d]}')

    def turnRight(self):
        # change direction 90 degrees to the right
        self.__d = (self.__d + 90) % 360
        print(f'DEBUG: turning {DIR_NAMES[self.__d]}')

    def forward(self, n):
        # validate that n is non-negative and then move the car in the current direction
        if n < 0:
            print("Invalid distance")
            n = 0
        else:
            if self.__d == EAST:
                self.__x += n
            elif self.__d == NORTH:
                self.__y += n
            elif self.__d == SOUTH:
                self.__y -= n
            elif self.__d == WEST:
                self.__x -= n
            print(f'DEBUG: moving forward {n} {DIR_NAMES[self.__d]}')

# Other function definitions
def randomDrive(car, n):
    # Checks if n is negative
    if n < 0:
        print("ERROR: Illegal value entered.")
        return car
    for i in range(n): 
        # Choose a random direction
        dir = random.choice(['left', 'right', 'none']) 
        # Choose a random distance
        dist = random.randint(0, 100)
        if dir == 'left':
            car.turnLeft()
        elif dir == 'right':
            car.turnRight()
        elif dir == 'none':
            car.forward(dist)

def goto(car, x, y):
    # Moves the car to the given location
    x_diff = x - car.getX()
    y_diff = y - car.getY()

    if x_diff == 0 and y_diff == 0:
        return  # the car is already at the destination

    # Determine the direction to move in the x-axis
    if x_diff > 0:
        car.setDir(EAST)
    else:
        car.setDir(WEST)

    car.forward(abs(x_diff))

    # Determine the direction to move in the y-axis
    if y_diff > 0:
        car.setDir(NORTH)
    else:
        car.setDir(SOUTH)

    car.forward(abs(y_diff))

def gasStation():
    # Creates a gas station
    x = random.randint(-100, 100) # Quards for gas station
    y = random.randint(-100, 100)
    print(f'DEBUG: gas station at {x} {y}') # Found gas station
    return (x, y)

def crashPillar():
    # Creates a random pillar
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    print(f'DEBUG: random pillar at {x} {y}')
    return (x, y)

def youCrashed(car):
    x, y = crashPillar()
    goto(car, x, y) # sets values
    print(f"Oh, oh, OH SHIT THERE'S A PILLAR AT ({x}, {y})") # finds a pillar
    print('YOU DIED') # Died prompt

def gasUp(car):
    x, y = gasStation()
    goto(car, x, y) # sets values
    print(f'Located gas station at ({x}, {y})') # finds gas station
    print("Your tank is now full!") # Notifies you that you filled your tank

def main():
    c1 = ToyCar( 100, -100, SOUTH )
    print( c1 )
    c2 = ToyCar()
    print( c2 )
    c3 = ToyCar( y = -50, d = 313 )
    c3 = ToyCar( y = -50, d = 90 )
    print( c3 )
    c = ToyCar( d = NORTH )
    print( c )
    c.forward( 100 )
    print( c )
    # This one needs a print, or you won't see it.
    print( c.getDir() )
    c.turnLeft()
    print( c )
    c.forward( -50 )
    c.forward( 50 )
    print( c )
    c.setDir( SOUTH )
    print( c )
    # This one needs a print, or you won't see it.
    print( c.getX(), c.getY() )
    randomDrive( c, 5 )
    print( c )
    gasUp( c )
    print( c )
    gasStation()
    print( c )
    c4 = ToyCar(20, 30, SOUTH)
    print(c4)
    goto( c4, -50, -25 )
    print(c4)
    youCrashed(c4)

main()
