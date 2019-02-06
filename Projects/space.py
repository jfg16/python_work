import turtle
wn = turtle.Screen()             # Set up the window and its attributes
wn.bgcolor("indigo")

from turtle import *
warp = turtle.Turtle()
warp.ht()
warp.color("darkslateblue")
def draw_warp(size,color):   
    for i in range(700):  
        warp.forward(i)
        warp.left(91) 
    return
draw_warp(30, "white")

starz = turtle.Turtle()             #Star 2 in bottom left
starz.pensize(0)
starz.ht()
starz.color("indigo")
starz.right(160)
starz.forward(280) 
def draw_starz(size, color):
    angle = 120
    starz.fillcolor(color)
    starz.begin_fill()

    for side in range(5):
        starz.forward(size)
        starz.right(angle)
        starz.forward(size)
        starz.right(72 - angle)
    starz.end_fill()
    return

draw_starz(14, "gold")

#MERCURY-------------------------------------
mring = turtle.Turtle()
mring.ht()
mring.color("indigo")
mring.right(145)
mring.forward(300)
mring.color("lightgray")
mring.pensize(2)
mring.circle(500)

mshadow = turtle.Turtle()           # create planet shadow (Mercury)
mshadow.ht()
mshadow.color("indigo")
mshadow.right(153)
mshadow.forward(265) 
mshadow.color("black")
mshadow.begin_fill()
mshadow.circle(50)
mshadow.end_fill()

mercury = turtle.Turtle()           # create planet (Mercury)
mercury.ht()
mercury.color("indigo")
mercury.right(155)
mercury.forward(265) 
mercury.color("bisque")
mercury.begin_fill()
mercury.circle(50)
mercury.end_fill()

mspot = turtle.Turtle()
mspot.ht()
mspot.color("indigo")
mspot.right(148)
mspot.forward(225)
mspot.color("burlywood")
mspot.begin_fill()
mspot.circle(5)
mspot.end_fill()
#END MERCURY-------------------------------------

#VENUS-------------------------------------
vring = turtle.Turtle()
vring.ht()
vring.color("indigo")
vring.left(180)
vring.forward(40)
vring.color("lightgray")
vring.pensize(2)
vring.circle(1000)

vshadow = turtle.Turtle()           # create planet shadow (Venus)
vshadow.ht()
vshadow.color("indigo")
vshadow.right(48)
vshadow.forward(140) 
vshadow.color("black")
vshadow.begin_fill()
vshadow.circle(70)
vshadow.end_fill()

venus = turtle.Turtle()           # create planet (Venus)
venus.ht()
venus.color("indigo")
venus.right(50)
venus.forward(140) 
venus.color("sienna")
venus.begin_fill()
venus.circle(70)
venus.end_fill()

#END VENUS-------------------------------------

#EARTH-------------------------------------
ering = turtle.Turtle()
ering.ht()
ering.color("indigo")
ering.right(270)
ering.forward(100)
ering.left(90)
ering.color("lightgray")
ering.pensize(2)
ering.circle(1500)

eshadow = turtle.Turtle()           # create planet shadow (Earth)
eshadow.ht()
eshadow.color("indigo")
eshadow.left(3)
eshadow.backward(50) 
eshadow.color("black")
eshadow.begin_fill()
eshadow.circle(60)
eshadow.end_fill()

earth = turtle.Turtle()           # create planet (Earth)
earth.ht()
earth.color("indigo")
earth.left(6)
earth.backward(50) 
earth.color("cornflowerblue")
earth.begin_fill()
earth.circle(60)
earth.end_fill()

#END EARTH-------------------------------------


star = turtle.Turtle()          #Star 1 in center
star.ht()
star.pensize(0)
def draw_star(size, color):
    angle = 120
    star.fillcolor(color)
    star.begin_fill()

    for side in range(5):
        star.forward(size)
        star.right(angle)
        star.forward(size)
        star.right(72 - angle)
    star.end_fill()
    return

draw_star(10, "gold")

stars = turtle.Turtle()             #Star 3 in right
stars.pensize(0)
stars.ht()
stars.color("indigo")
stars.right(230)
stars.forward(140) 
def draw_stars(size, color):
    angle = 120
    stars.fillcolor(color)
    stars.begin_fill()

    for side in range(5):
        stars.forward(size)
        stars.right(angle)
        stars.forward(size)
        stars.right(72 - angle)
    stars.end_fill()
    return

draw_stars(14, "gold")

starr = turtle.Turtle()             #Star 4 in 
starr.pensize(0)
starr.ht()
starr.color("indigo")
starr.right(5)
starr.forward(428) 
def draw_starr(size, color):
    angle = 120
    starr.fillcolor(color)
    starr.begin_fill()

    for side in range(5):
        starr.forward(size)
        starr.right(angle)
        starr.forward(size)
        starr.right(72 - angle)
    starr.end_fill()
    return

draw_starr(14, "gold")



scratch = turtle.Turtle()
star.pensize(5)



wn.exitonclick()