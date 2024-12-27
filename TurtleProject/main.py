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

# Draw other shapes

screen = Screen()
screen.exitonclick()
