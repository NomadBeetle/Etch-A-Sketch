import turtle
from turtle import Turtle, Screen

# Initialize turtle
color = "black"
squirtle = Turtle()
squirtle.speed(5)

# Movement functions
def move_forward():
    squirtle.forward(5)

def move_back():
    squirtle.back(5)

def move_right():
    squirtle.right(5)

def move_left():
    squirtle.left(5)

# Clear screen
def clear_screen():
    squirtle.clear()
    squirtle.penup()
    squirtle.home()
    squirtle.pendown()

# Exit program
def end():
    myScreen.bye()

# Change pen color
def change_color():
    global color
    colors = ["red", "blue", "green", "yellow", "purple", "black", "orange"]
    color = myScreen.textinput("Change Color", f"Choose a color: {', '.join(colors)}")

    if color and color.lower() in colors:
        squirtle.pencolor(color.lower())  # Change color
    else:
        myScreen.textinput("Invalid Color", f"Choose from: {', '.join(colors)}")  # Reprompt
    myScreen.listen()

# Change pen width
def change_width():
    width = myScreen.numinput("Width Changer", "Enter pen width (1-10):", minval=1, maxval=10)
    if width:  # Ensures width is not None
        squirtle.pensize(int(width))  # Convert to int to avoid float sizes
    myScreen.listen()

def eraser():
    squirtle.pencolor("white")

def draw():
    squirtle.pencolor(color)

# Screen setup
myScreen = Screen()
myScreen.title("Etch-A-Sketch")
myScreen.listen()

# Key bindings
myScreen.onkey(change_color, "f")
myScreen.onkey(clear_screen, "c")
myScreen.onkeypress(move_forward, "w")
myScreen.onkeypress(move_back, "s")
myScreen.onkeypress(move_right, "d")
myScreen.onkeypress(move_left, "a")
myScreen.onkey(end, "space")
myScreen.onkey(change_width, "g")
myScreen.onkey(eraser, "e")
myScreen.onkey(draw, "r")

myScreen.exitonclick()
