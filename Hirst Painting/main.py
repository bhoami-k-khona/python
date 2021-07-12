import colorgram
import turtle
import random

# Extract 30 colors from an image.
colors = colorgram.extract('image.jpg', 30)

# Add the extracted colors to "colours" list
colours = []

# create tuple rgb values and append to colours
for color in colors:
    red = color.rgb.r
    green = color.rgb.g
    blue = color.rgb.b
    new_color = (red, green, blue)
    colours.append(new_color)

# create turtle and screen
tim = turtle.Turtle()
screen = turtle.Screen()

# set color mode
turtle.colormode(255)

# Initial setup
tim.penup()
tim.shape("turtle")
tim.speed("fastest")
tim.setheading(225)
tim.forward(200)
tim.setheading(0)

# Damien Hirst Spot Painting
for col in range(10):
    for row in range(10):
        tim.color(random.choice(colours))
        tim.dot(20)
        tim.forward(50)

    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)

# exit screen on click
screen.exitonclick()
