# import colorgram
#
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

from turtle import Turtle, Screen
import random

color_list = [(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162),
              (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157),
              (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221),
              (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210),
              (65, 66, 56), (240, 246, 243)]


screen = Screen()
screen.colormode(255)

# Turtle initializations
turtle = Turtle()
turtle.hideturtle()
turtle.penup()
turtle_x_pos = -225
turtle_y_pos = -200
turtle.setposition(turtle_x_pos, turtle_y_pos)
turtle.pendown()
turtle.speed("fastest")


def dot_maker():
    turtle.dot(15, random.choice(color_list))
    turtle.penup()
    turtle.forward(45)
    turtle.pendown()


for dot_count in range(1, 101):
    dot_maker()
    if dot_count % 10 == 0:
        turtle_y_pos += 45
        turtle.penup()
        turtle.setposition(turtle_x_pos, turtle_y_pos)


screen.exitonclick()
