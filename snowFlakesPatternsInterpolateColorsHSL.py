import turtle
import random
import math
import colorsys  # Import the colorsys module for color space conversions

# Define the function for drawing a Koch snowflake
def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order-1, size/3)
            t.left(angle)

# Define the function for drawing a random snowflake
def draw_random_snowflake(t, x, y, color):
    t.penup()
    t.goto(x, y)
    t.pendown()

    t.pencolor(color)  # Set the color passed to the function
    size=50
    order= 1

    for _ in range(3):
        koch_snowflake(t, order, size)
        t.right(120)

# Test the functions
if __name__ == "__main__":
    t = turtle.Turtle()
    t.speed(0)
    screen = turtle.Screen()
    screen.bgcolor("#666666")
    #screen.bgcolor("#919191")
    num_snowflakes = 50#random.randint(3, 500)

    for i in range(num_snowflakes):
        x = i * 10 - 250
        y = 100 * math.sin(i / 5.0)

        hue = i / num_snowflakes  # Calculate the hue based on the current snowflake number
        color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)  # Convert the hue to RGB

        draw_random_snowflake(t, x, y, color)

    turtle.done()
