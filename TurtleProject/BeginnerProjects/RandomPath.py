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
