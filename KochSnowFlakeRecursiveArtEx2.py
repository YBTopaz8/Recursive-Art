import turtle
import colorsys

# Function to create Koch snowflake or Koch curve
def koch_curve(t, iterations, length, i=0):
    # Calculate a rainbow color by mapping i to the hue
    # hue = i / 50
    # r, g, b = colorsys.hsv_to_rgb(hue % 1, 1.0, 1.0)
    # t.pencolor(r, g, b)
    
    if iterations == 0:
        t.forward(length)
    else:
        length /= 4.0
        koch_curve(t, iterations - 1, length)
        t.left(60)
        koch_curve(t, iterations - 1, length)
        t.right(120)
        koch_curve(t, iterations - 1, length)
        t.left(60)
        koch_curve(t, iterations - 1, length)

# Function to create the full Koch Snowflake
def koch_snowflake(t, iterations, length):
    for i in range(3):
        koch_curve(t, iterations, length)
        t.right(120)

# Setting up the drawing
window = turtle.Screen()
window.bgcolor("gray")

# Creating a turtle for drawing
my_turtle = turtle.Turtle()
my_turtle.speed(0)

# Positioning the turtle
my_turtle.penup()
my_turtle.goto(-150, 90)
my_turtle.pendown()

# Drawing the Koch Snowflake with desired iterations and length
iterations = 4 # Number of iterations
length = 550 # Length of the side of the initial triangle
koch_snowflake(my_turtle, iterations, length)

# Finishing up
my_turtle.hideturtle()
window.mainloop()
