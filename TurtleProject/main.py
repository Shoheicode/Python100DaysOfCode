from turtle import Screen, Turtle

turtle_t = Turtle()

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
    for j in range(i):
        turtle_t.forward(10)
        turtle_t.right(360 / i)

screen = Screen()
screen.exitonclick()
