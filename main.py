import random
from turtle import Turtle, Screen
# import colorgram
# def color_extractor(image_loc):
#     """Takes an image as input, extracts relevant colors from it, and stores it in tuples and finally in a list"""
#     x = colorgram.extract(image_loc, 40)
#     colors = []
#     for i in range(len(x)):
#         r = x[i].rgb[0]
#         g = x[i].rgb[1]
#         b = x[i].rgb[2]
#         color_combination = (r, g, b)
#         colors.append(color_combination)
#     return colors
#     # print(colors)
#
#
# x = color_extractor('image1.jpeg')
# print(x)
#
# x = colorgram.extract('image1.jpeg', 20)
# colors = []
# for i in range(len(x)):
#     r = x[i].rgb[0]
#     g = x[i].rgb[1]
#     b = x[i].rgb[2]
#     contrasted = (r, g, b)
#     colors.append(contrasted)
# print(colors)


colors = [(202, 164, 189), (219, 149, 103), (34, 101, 169), (158, 56, 86), (142, 82, 56), (241, 225, 96),
          (113, 173, 212),
          (218, 128, 156), (166, 23, 41), (217, 66, 101), (224, 83, 57), (121, 183, 138), (22, 169, 200),
          (158, 151, 34), (42, 124, 79), (19, 57, 138), (79, 37, 25)]

dotter = Turtle()
screen = Screen()
screen.colormode(255)
dotter.hideturtle()
print(dotter.pos())


def spot_painting(spot, initial_pos):
    """Makes the famous Hirst Spot Painting by taking turtle object and initial y coordinate as input"""
    #     spot.position
    #     spot.setpos()
    spot.speed('fastest')
    color_chooser = random.choice(colors)
    spot.dot(20, color_chooser)
    spot.penup()
    spot.forward(50)
    spot.pendown()
    if initial % 100 == 0:
        spot.penup()
        spot.setpos(-220, initial / 2)


initial = -500
dotter.penup()
dotter.setpos(-220, initial / 2)

for i in range(101):
    spot_painting(dotter, initial)
    initial += 10

# for i in range(40):
#     dotter.pendown()
#     dotter.dot(5)
#     dotter.forward(20)
#     if i % 2 == 0 or i == 0:
#         dotter.penup()
#         dotter.setpos(0, initial)
#         initial += 10

screen.exitonclick()
