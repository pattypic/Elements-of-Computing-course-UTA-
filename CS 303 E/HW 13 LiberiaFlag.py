# File: LiberiaFlag.py
# Student: Patrick Pichardo
# UT EID: pjp953
# Course: CS303E
#
# Date: 04/12/2023
# Description: 
# Draws the LiberiaFlag using turtle graphics
# the rest is elaborated through out the assignment. 

# import turtle
import turtle

# creating the turtle object and the speed of the drawing. 
t = turtle.Turtle()
t.speed(0)

# defines colors using tuples
myBlue = (0, 32, 91)
myRed = (191, 13, 62)
white = (255, 255, 255)

screen = turtle.Screen()

# draws rectangle
def draw_rectangle(x, y, width, height, color):
    t.penup()
    t.pencolor(color)
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for i in range(2): # draws the rectangle
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

# draws start
def draw_star(x, y, size, color):
    t.penup()
    t.pencolor(color)
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for i in range(5):  # draws star
        t.forward(size)
        t.right(144)
    t.end_fill()

# used to draw a pentagon to fill in the center of the star
def draw_pentagon(x, y, size, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(5):  # draws pentagon
        t.forward(size / 2)
        t.right(72)
    t.end_fill()
    t.penup()

# uses the abover defenition to draw the flag
def draw_liberia_flag():
    screen.colormode(255)
    screen.bgcolor(white)
    for i in range(12):     # range for the amount of lines in the flag
        if i % 2 == 0:
            draw_rectangle(-200, 0 + i * 20, 400, 20, white) # mults the index by 20
        else:
            draw_rectangle(-200, 0 + i * 20, 400, 20, myRed)# mults the index by 20
    draw_rectangle(-200, 140, 100, 100, myBlue)
    draw_star(-185, 200, 70, white)
    draw_pentagon(-158, 200, 33, white)
    screen.exitonclick()        # click off to close screen

draw_liberia_flag()     # works (:
    