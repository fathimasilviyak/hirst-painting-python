import random
import turtle as t
from turtle import Turtle, Screen

t.colormode(255)
from random import choice

# import colorgram
# # Extract 30 colors from an image.
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

# rgb_colors:
colors = [(22, 30, 46), (140, 173, 200), (36, 105, 148), (205, 160, 112), (226, 210, 99), (140, 29, 62), (169, 51, 83),
          (208, 74, 101), (192, 139, 172), (16, 163, 191), (64, 167, 115), (136, 88, 73), (117, 181, 115),
          (190, 182, 43), (223, 81, 47), (27, 61, 117), (172, 209, 179), (72, 34, 67), (51, 141, 110), (9, 90, 108),
          (239, 204, 5), (217, 176, 195), (115, 36, 34), (232, 169, 162), (146, 208, 226), (186, 186, 212)]

tim = Turtle()
tim.speed("fastest")

# Set starting position
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)


def hist_paint(row, column):
    for i in range(column):
        for j in range(row):
            tim.dot(20, choice(colors))
            tim.penup()
            tim.forward(50)
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


hist_paint(10, 10)

screen = Screen()
screen.exitonclick()
