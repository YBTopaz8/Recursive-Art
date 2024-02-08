import turtle
import random
import math

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

# Function to interpolate between two colors
def interpolate_color(color1, color2, factor):
    return ((1-factor)*color1[0] + factor*color2[0],
            (1-factor)*color1[1] + factor*color2[1],
            (1-factor)*color1[2] + factor*color2[2])

# Test the functions
if __name__ == "__main__":
    t = turtle.Turtle()
    t.speed(0)

    num_snowflakes = random.randint(100, 500)

    colors = [(1.0, 0.0, 0.0),  # Red
              (0.0, 1.0, 0.0),  # Green
              (0.0, 0.0, 1.0),  # Blue
              (1.0, 1.0, 0.0),  # Yellow
              (1.0, 0.0, 1.0),  # Magenta
              (0.0, 1.0, 1.0)]  # Cyan

    for i in range(num_snowflakes):
        x = i * 10 - 250
        y = 100 * math.sin(i / 5.0)

        color_index = (i // 5) % len(colors)  # Change color every 5 snowflakes
        start_color = colors[color_index]
        end_color = colors[(color_index + 1) % len(colors)]
        color = interpolate_color(start_color, end_color, (i % 5) / 5)  # Interpolate the color

        draw_random_snowflake(t, x, y, color)

    turtle.done()
