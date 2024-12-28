import turtle as t
import random
from turtle import Screen

turt = t.Turtle()
t.colormode(255)


def rand_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


turt.speed("fastest")
num_of_circles = 100

for cir in range(num_of_circles):
    turt.color(rand_color())
    turt.setheading((360 / num_of_circles) * cir)
    turt.circle(100)

screen = Screen()
screen.exitonclick()
