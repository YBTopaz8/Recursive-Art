# import turtle
# import random

# def koch_snowflake(t, order, size):
#     if order == 0:
#         t.forward(size)
#     else:
#         for angle in [60, -120, 60, 0]:
#             koch_snowflake(t, order-1, size/3)
#             t.left(angle)

# # Test
# if __name__ == "__main__":
#     t = turtle.Turtle()
#     t.speed(0)

#     # Move the turtle to start position
#     t.penup()
#     t.goto(-150, 90)
#     t.pendown()

#     # Draw a Koch Snowflake of order 4
#     for _ in range(3):
#         t.pencolor(random.random(), random.random(), random.random())  # Random color
#         koch_snowflake(t, 4, 300)
#         t.right(120)

#     turtle.done()
import turtle
import random

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order-1, size/3)
            t.left(angle)

def draw_random_snowflake(t):
    t.penup()
    t.goto(random.randint(-200, 200), random.randint(-200, 200))  # Random position
    t.pendown()

    t.pencolor(random.random(), random.random(), random.random())  # Random color

    size = random.randint(10, 50)  # Random size
    order = random.randint(1, 3)  # Random order

    for _ in range(3):
        koch_snowflake(t, order, size)
        t.right(120)

# Test
if __name__ == "__main__":
    t = turtle.Turtle()
    t.speed(0)

    for _ in range(50):
        draw_random_snowflake(t)

    turtle.done()
