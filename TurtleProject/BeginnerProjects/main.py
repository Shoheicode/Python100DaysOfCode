import random
from turtle import Screen, Turtle

turtle_t = Turtle()
turtle_t.speed(9)


def draw_shape(num_side):
    angle = 360 / num_side
    for j in range(num_side):
        turtle_t.forward(50)
        turtle_t.right(angle)


# Draw square
turtle_t.forward(50)
turtle_t.right(90)
turtle_t.forward(50)
turtle_t.right(90)
turtle_t.forward(50)
turtle_t.right(90)
turtle_t.forward(50)

# Draw dotted line
turtle_t.penup()
turtle_t.forward(10)
turtle_t.right(90)
for i in range(10):
    turtle_t.pendown()
    turtle_t.forward(10)
    turtle_t.penup()
    turtle_t.forward(10)

turtle_t.setpos(0, 0)

turtle_t.pendown()
# Draw other shapes
for i in range(3, 12):
    draw_shape(i)

# Drawing the color lines

colours = [
    "CornflowerBlue",
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    "wheat",
    "SlateGray",
    "SeaGreen",
]

directions = [0, 90, 180, 270]

turtle_t.setpos(0, 0)
turtle_t.speed(9)
turtle_t.pensize(10)

for _ in range(200):
    turtle_t.forward(30)
    turtle_t.setheading(random.choice(directions))
    turtle_t.color(random.choice(colours))

screen = Screen()
screen.exitonclick()