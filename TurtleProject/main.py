from turtle import Screen, Turtle

turtle_t = Turtle()


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


screen = Screen()
screen.exitonclick()
