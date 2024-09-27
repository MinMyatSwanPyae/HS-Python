import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("House Drawing")
screen.bgcolor("skyblue")

# Function to draw a rectangle
def draw_rectangle(color, x, y, width, height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

# Function to draw a triangle (roof)
def draw_triangle(color, x, y, base):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.goto(x + base / 2, y + (base * 0.866))  # Height of the triangle
    turtle.goto(x + base, y)
    turtle.goto(x, y)
    turtle.end_fill()

# Function to draw the house
def draw_house():
    # Draw the base of the house
    draw_rectangle("lightgray", -50, -50, 100, 100)  # House body

    # Draw the roof
    draw_triangle("brown", -60, 50, 120)  # Roof

    # Draw the door
    draw_rectangle("saddlebrown", -20, -50, 40, 60)  # Door

    # Draw windows
    draw_rectangle("white", -40, 0, 30, 30)  # Left window
    draw_rectangle("white", 10, 0, 30, 30)   # Right window

# Draw the house
draw_house()

# Hide the turtle and display the scene
turtle.hideturtle()
turtle.done()
