"""
This program is a basic game of pong.
Has ability to play with two players or against AI.
Uses turtle to use as graphics.

GitHub: @ILYLegend
"""

import turtle
import time
import random

# Game screen
turtle.setup(800, 600)
turtle.bgcolor("black")
turtle.tracer(0)

# Create AI status
ai_status = turtle.Turtle()
ai_status.color("white")
ai_status.penup()
ai_status.hideturtle()
ai_status.goto(0, 200)

# Create AI instruction
ai_instruction = turtle.Turtle()
ai_instruction.color("white")
ai_instruction.penup()
ai_instruction.hideturtle()
ai_instruction.goto(0, 230)
ai_instruction.write("Press 'a' for AI mode", align="center", font=("Arial", 16, "normal"))

# Create left paddle instruction
left_instruction = turtle.Turtle()
left_instruction.color("white")
left_instruction.penup()
left_instruction.hideturtle()
left_instruction.goto(-275, 260)
left_instruction.write("Press 'w' or 's' to move paddle", align="center", font=("Arial", 8, "normal"))

# Create right paddle instruction
right_instruction = turtle.Turtle()
right_instruction.color("white")
right_instruction.penup()
right_instruction.hideturtle()
right_instruction.goto(275, 260)
right_instruction.write("Press 'up' or 'down' keys to move paddle", align="center", font=("Arial", 8, "normal"))

# Create the ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = random.choice([-2.3, 2.3])
ball.dy = random.choice([-2.3, 2.3])

# Create left paddle
left_paddle = turtle.Turtle()
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350, 0)
left_paddle.dy = 0

# Create right paddle
right_paddle = turtle.Turtle()
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)
right_paddle.dy = 0

# Game points system
game_over = False
winner = None
points = {
    "player1": 0,
    "player2": 0
}
game_limit = {
    "max_points": 3,
    "ball_speed": 3
}

# Display scores
score = turtle.Turtle()
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player 1: 0  Player 2: 0", align="center", font=("Arial", 24, "normal"))

# Move left paddle
def left_paddle_up():
    if left_paddle.ycor() < 250:
        left_paddle.sety(left_paddle.ycor() + 10)
def left_paddle_down():
    if left_paddle.ycor() > -240:
        left_paddle.sety(left_paddle.ycor() - 10)

# Move right paddle
def right_paddle_up():
    if right_paddle.ycor() < 250:
        right_paddle.sety(right_paddle.ycor() + 10)
def right_paddle_down():
    if right_paddle.ycor() > -240:
        right_paddle.sety(right_paddle.ycor() - 10)

# AI controlled left paddle
ai_mode = False
def move_left_paddle_ai():
    if ball.ycor() > left_paddle.ycor():
        left_paddle.sety(left_paddle.ycor() + 1.8)
    elif ball.ycor() < left_paddle.ycor():
        left_paddle.sety(left_paddle.ycor() - 1.8) 

# AI mode toggle
def toggle_ai():
    global ai_mode
    ai_mode = not ai_mode
    update_ai_status()

# Show AI mode status
def update_ai_status():
    ai_status.clear()
    ai_status.write("AI mode: On" if ai_mode else "AI mode: Off", align="center", font=("Arial", 16, "normal"))

# Keyboard bindings
turtle.listen()
turtle.onkeypress(left_paddle_up, "w")
turtle.onkeypress(left_paddle_down, "s")
turtle.onkeypress(right_paddle_up, "Up")
turtle.onkeypress(right_paddle_down, "Down")
turtle.onkeypress(toggle_ai, "a")

# Set objects in place
left_paddle.sety(left_paddle.ycor() + left_paddle.dy)
right_paddle.sety(right_paddle.ycor() + right_paddle.dy)
ball.setx(ball.xcor() + ball.dx)
ball.sety(ball.ycor() + ball.dy)

# Loop to run game
while not game_over:
    # Update screen
    turtle.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Move paddles
    left_paddle.sety(left_paddle.ycor() + left_paddle.dy)
    right_paddle.sety(right_paddle.ycor() + right_paddle.dy)

    # AI left paddle
    if ai_mode:
        move_left_paddle_ai()

    # Check if ball is hitting top or bottom
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1

    # Check if ball and paddle hit
    if (340 > ball.xcor() > 330) and (right_paddle.ycor() + 50 > ball.ycor() > right_paddle.ycor() - 50):
        ball.color("blue")
        ball.setx(330)
        ball.dx *= -1

    elif (-340 < ball.xcor() < -330) and (left_paddle.ycor() + 50 > ball.ycor() > left_paddle.ycor() - 50):
        ball.color("red")
        ball.setx(-330)
        ball.dx *= -1

    # Score points
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        points["player1"] += 1

    elif ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        points["player2"] += 1

    # Check for game over
    if points["player1"] == game_limit["max_points"] or points["player2"] == game_limit["max_points"]:
        winner = "Player 1" if points["player1"] > points["player2"] else "Player 2"
        print(f"{winner} wins!")
        turtle.bye()
        break

    # Update score display
    score.clear()
    score.write("Player 1: {}  Player 2: {}".format(points["player1"], points["player2"]), align="center", font=("Arial", 24, "normal"))

    # Update screen and delay
    turtle.update()
    time.sleep(0.01)
