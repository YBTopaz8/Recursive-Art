import turtle
import random
import math
import colorsys
from random import choice

# Define the function for drawing a Koch snowflake
def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order-1, size/3)
            t.left(angle)


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

def draw_wave_pattern(t, num_snowflakes):
    # Your existing implementation for wave-like pattern
    pass

def draw_big_star_pattern(t, num_snowflakes, size):
    # Calculate the positions of the snowflakes to form a big star
    angles = [18, -54, -54, -54, -54]
    t.penup()
    start_x, start_y = t.pos()
    for _ in range(5):  # A star has 5 vertices
        draw_random_snowflake(t, start_x, start_y, random_color())
        t.forward(size)
        t.right(angles[_ % 5])
    t.goto(start_x, start_y)  # Return to the starting point

def draw_arrow_pattern(t, num_snowflakes, size):
    # Calculate the positions of the snowflakes to form an arrow
    pass

def draw_cameroon_structure(t, num_snowflakes, size):
    # Simplify Cameroon's map structure to a basic shape and draw
    pass

def random_color():
    # Function to generate a random color
    hue = random.random()
    return colorsys.hsv_to_rgb(hue, 1.0, 1.0)

# Main function to call the drawing functions randomly
def main():
    t = turtle.Turtle()
    t.speed(0)
    screen = turtle.Screen()
    screen.bgcolor("#666666")
    num_snowflakes = 150

    # List of pattern functions
    pattern_functions = [draw_wave_pattern] #[draw_wave_pattern, draw_big_star_pattern, draw_arrow_pattern, draw_cameroon_structure]
    # Randomly select a pattern to draw
    pattern = choice(pattern_functions)
    
    # Call the selected pattern function
    pattern(t, num_snowflakes, 50)  # You can adjust the size parameter as needed

    turtle.done()

if __name__ == "__main__":
    main()
