import turtle
import math

# Constants for the angles used to draw rhombuses
ANGLE_THIN = 36  # Angle for thin rhombus
ANGLE_THICK = 72  # Angle for thick rhombus
GOLDEN_RATIO = (1 + math.sqrt(5)) / 2

def draw_rhombus(t, size, angle):
    """Draws a rhombus with two angles of 'angle' degrees and side length 'size'."""
    for _ in range(2):
        t.forward(size)
        t.left(180 - angle)
        t.forward(size)
        t.left(angle)

def subdivide_thin(t, size, depth):
    if depth == 0:
        t.color('green')
        draw_rhombus(t, size, ANGLE_THIN)
    else:
        newSize = size / GOLDEN_RATIO
        t.forward(size)
        t.left(ANGLE_THICK)
        subdivide_thick(t, newSize, depth - 1)
        t.right(ANGLE_THIN)
        t.forward(newSize)
        t.right(ANGLE_THICK)
        subdivide_thin(t, newSize, depth - 1)
        t.left(ANGLE_THIN)
        t.forward(newSize)
        t.left(ANGLE_THIN)
        t.forward(size)
        t.right(180 - ANGLE_THICK)
        subdivide_thin(t, newSize, depth - 1)
        t.right(ANGLE_THICK)
        t.forward(newSize)
        t.right(ANGLE_THIN)
        subdivide_thick(t, newSize, depth - 1)
        t.left(ANGLE_THICK)
        t.forward(size)
        t.left(180 - ANGLE_THIN)

def subdivide_thick(t, size, depth):
    if depth == 0:
        t.color('blue')
        draw_rhombus(t, size, ANGLE_THICK)
    else:
        newSize = size / GOLDEN_RATIO
        subdivide_thin(t, newSize, depth - 1)
        t.forward(newSize)
        t.right(ANGLE_THIN)
        subdivide_thick(t, newSize, depth - 1)
        t.left(ANGLE_THIN)
        t.forward(size)
        t.left(ANGLE_THICK)
        subdivide_thick(t, newSize, depth - 1)
        t.right(ANGLE_THICK)
        t.forward(newSize)
        t.right(ANGLE_THIN)
        subdivide_thin(t, newSize, depth - 1)
        t.left(ANGLE_THIN)

def main():
    turtle.speed(0)
    turtle.hideturtle()
    turtle.tracer(False)
    size = 200  # Size of the initial rhombus
    depth = 4  # Recursion depth

    # Initial position
    turtle.penup()
    turtle.goto(-size / 2, -size / (2 * math.sin(math.radians(ANGLE_THICK))))
    turtle.pendown()

    # Start the recursive drawing
    subdivide_thick(turtle, size, depth)

    turtle.update()
    turtle.done()

if __name__ == "__main__":
    main()
