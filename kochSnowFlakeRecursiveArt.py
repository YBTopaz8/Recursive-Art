# import turtle

# def koch(size, n):
#     if n == 0:
#         turtle.fd(size)
#     else:
#         for angle in [0, 60, -120, 60]:
#             turtle.left(angle)
#             koch(size/3, n-1)

# def main():
#     turtle.setup(1200, 1000)
#     turtle.speed(11)
#     turtle.penup()
#     turtle.goto(-300, 200)
#     turtle.pendown()
#     turtle.pensize(2)
#     level = 4
#     koch(600, level)  # Third-iteration Koch curve
#     turtle.right(120)
#     koch(600, level)
#     turtle.right(120)
#     koch(600, level)
#     turtle.hideturtle()
#     turtle.done()

# main()

import turtle

def koch(size, n):
    """Draws a Koch curve with a given size and recursion depth."""
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            koch(size / 3, n - 1)

def setup_environment():
    """Sets up the turtle environment before drawing."""
    turtle.setup(1200, 1000)
    turtle.speed(11)
    turtle.penup()
    turtle.goto(-300, 200)
    turtle.pendown()
    turtle.pensize(2)

def draw_snowflake(level, size):
    """Draws a complete Koch snowflake with a given recursion level and size."""
    for _ in range(3):
        koch(size, level)
        turtle.right(120)

def main(level=4, size=600):
    """Main function to set up the environment and draw the Koch snowflake."""
    setup_environment()
    draw_snowflake(level, size)
    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main(level=4, size=600)
