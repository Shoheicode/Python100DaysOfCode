from turtle import Screen, Turtle

turtle_t = Turtle()

# Draw square
turtle_t.forward(120)
turtle_t.left(90)
turtle_t.forward(120)
turtle_t.left(90)
turtle_t.forward(120)
turtle_t.left(90)
turtle_t.forward(120)

# Draw dotted line
turtle_t.penup()
turtle_t.forward(10)
turtle_t.left(90)
for i in range(10):
    turtle_t.pendown()
    turtle_t.forward(10)
    turtle_t.penup()
    turtle_t.forward(10)

screen = Screen()
screen.exitonclick()
