# Turtle Graphics Game
import turtle

# Set up screen
wn = turtle.Screen()
wn.bgcolor("lightgreen")

# Draw border
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300,-300)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()

# Draw border
mypen = turtle.Turtle

# Create player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)

# Set speed
speed = 1

# Define functions

def turnleft():
    player.left(30)

def turnright():
    player.right(30)

def increasespeed():
    global speed
    speed += 1

# Set Keyboard bindings
turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(increasespeed, "Up")

while True:
    player.forward(speed)

    #Boundary Checking
    if player.xcor()  > 300 or player.xcor() < -300:
        player.right(100)
    if player.ycor()  > 300 or player.ycor() < -300:
        player.right(100)




delay = raw_input("Press Enter to finish")