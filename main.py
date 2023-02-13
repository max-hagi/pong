import turtle

window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width = 800, height = 600)
window.tracer = 0 # Stops the window from automatically updating

# Left paddle
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup() # Prevent a lines from bering drawn
paddle_a.goto(-350, 0)

# Right paddle
paddle_b = turtle.Turtle()
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup() # Prevent a lines from bering drawn
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup() # Prevent a lines from bering drawn
ball.goto(0, 0)
ball.dx = 7
ball.dy = 7


# Paddle movement functions
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 245:
        paddle_a.sety(y+20)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 245:
        paddle_b.sety(y+20)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -240:
        paddle_a.sety(y-20)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -240:
        paddle_b.sety(y-20)


#Keyboard listeners
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_down, "Down")


while True:
    window.update()
    
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


   
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1


    # Ball hits right paddle
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    # Ball hits left paddle
    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1