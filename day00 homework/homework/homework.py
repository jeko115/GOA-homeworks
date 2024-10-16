from turtle import *


#we want to paint house

#step 1: draw a square
speed(30)
width (7)
color ("purple")
forward ( 200 )
left (90)

forward (200)
left (90)

forward(200)
left (90)

forward (200)
left (90)
#end of square

#drawing a door

forward(70)
color("yellow")
left (90)
forward(120)    #height of the door
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(160, 160)
left(30)
pendown()
color("green")
begin_fill()
forward(30)
right(90)
forward(30)
left(90)
left(180)
forward(30)
right(90)
forward(30)

penup()
goto(60, 160)
pendown()
left(180)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
end_fill()

exitonclick ()