import turtle
import random
import math

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order-1, size/3)
            t.left(angle)

def draw_random_snowflake(t, x, y):
    t.penup()
    t.goto(x, y)  # Position based on the wave pattern
    t.pendown()

    t.pencolor(random.random(), random.random(), random.random())  # Random color
    size=50
    order= 1
    #size = random.randint(30, 30)  # Random size
    #order = random.randint(1, 3)  # Random order; 1 = straight line, 1 = V, 2 = jagged lines

    for _ in range(3):
        koch_snowflake(t, order, size)
        t.right(120)

# Test
if __name__ == "__main__":
    t = turtle.Turtle()
    t.speed(0)
    num_snowflakes = random.randint(100, 500)  # Random number of snowflakes

    for i in range(num_snowflakes):
        x = i * 10 - 250  # x position
        y = 100 * math.sin(i / 5.0)  # y position based on the wave pattern
        draw_random_snowflake(t, x, y)

    turtle.done()
