from tkinter import W
from turtle import *

from pkg_resources import working_set


#we want to paint house
speed(3)
shape("turtle")
#1: draw a square

width(6)
color("blue")

forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)

#end of square

#drawing a door

forward(70)
color("yellow")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)

#end of door

#start a roof
color("green")
penup()
goto(200, 200)
pendown()
right(150)
forward(200)
left(120)
forward(200)


#end roof



#start drawinng windows
color("pink")
penup()
goto(60, 90)
pendown()
left(210)
forward(60)
left(90)
forward(50)
left(90)
forward(60)
left(90)
forward(50)

#left window end

#start right window

penup()
goto(140, 90)
pendown()
forward(50)
left(90)
forward(60)
left(90)
forward(50)
left(90)
forward(60)


#right window end

#start roof's window

penup()
goto(70, 280)
pendown()
forward(50)
left(90)
forward(60)
left(90)
forward(50)
left(90)
forward(60)








exitonclick()