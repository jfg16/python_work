import turtle
wn = turtle.Screen()             # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()           # create tess and set his pen width
tess.pensize(5)

alex = turtle.Turtle()           # create alex
alex.color("hotpink")            # set his color
alex.pensize(5)

tess.forward(80)                 # Let tess draw an equilateral triangle
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)                   # complete the triangle

tess.right(180)                  # turn tess around
tess.forward(80)                 # move her away from the origin so we can see alex

alex.forward(60)                 # make alex draw a square
alex.left(90)
alex.forward(60)
alex.left(90)
alex.forward(60)
alex.left(90)
alex.forward(60)
alex.left(90)

wn.exitonclick()