import turtle

#for game windows

game = turtle.Screen()
game.title("Ping Pong")
game.bgcolor("Black")
game.setup(width=720, height=360)
game.tracer(0)

score_a = 0
score_b = 0

#paddle a setup
paddle_a = turtle.Turtle()
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-300,0)

#paddle b setup
paddle_b = turtle.Turtle()
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(300,0)

#paddle a controls
def paddle_a_up():
    y = paddle_a.ycor()
    y = y + 10
    paddle_a.sety(y)
    if y > 130:
        paddle_a.sety(130)

def paddle_a_down():
    y = paddle_a.ycor()
    y = y - 10
    paddle_a.sety(y)
    if y < -130:
        paddle_a.sety(-130)

#paddle b controls
def paddle_b_up():
    y = paddle_b.ycor()
    y = y + 10
    paddle_b.sety(y)
    if y > 130:
        paddle_b.sety(130)


#scoreb
pen=turtle.Turtle()
pen.color("white")
pen.penup()
pen.speed(0)
pen.hideturtle()
pen.goto(0,150)
pen.clear()
pen.write("A : 0  B : 0", align ="center" , font=("Arial", 16, "normal"))



def paddle_b_down():
    y = paddle_b.ycor()
    y = y - 10
    paddle_b.sety(y)
    if y < -130:
        paddle_b.sety(-130)
game.listen()
game.onkeypress(paddle_a_up,"w")
game.onkeypress(paddle_a_down,"s")
game.onkeypress(paddle_b_up,"Up")
game.onkeypress(paddle_b_down,"Down")

#ball settings
ball=turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(100,0)
#change this to change speed of ball
ball.dx = 0.05
ball.dy = 0.05


while(1):
    game.update()
    ball.setx(ball.xcor() + ball.dx)
    if ball.xcor() > 330:
       ball.setx(0)
       ball.dx *= -1
       score_a = score_a + 1 
       pen.clear()
       pen.write("A : {}  B : {}".format(score_a,score_b), align ="center" , font=("Arial", 16, "normal"))
    ball.sety(ball.ycor() + ball.dy)
    if ball.ycor() > 130:
       ball.sety(130)
       ball.dy *= -1
    ball.setx(ball.xcor() + ball.dx)
    if ball.xcor() < -330:
       ball.setx(0)
       ball.dx *= -1
       score_b = score_b + 1
       pen.clear()
       pen.write("A : {}  B : {}".format(score_a,score_b), align ="center" , font=("Arial", 16, "normal"))
    ball.sety(ball.ycor() + ball.dy)
    if ball.ycor() < -130:
       ball.sety(-130)
       ball.dy *= -1   
    
    #when ball collides with paddles
    if (ball.xcor() > 290) and (ball.ycor() < paddle_b.ycor()+50 and ball.ycor() > paddle_b.ycor()-50):
        ball.setx(290)
        ball.dx *= -1
    if (ball.xcor() < -290) and (ball.ycor() < paddle_a.ycor()+50 and ball.ycor() > paddle_a.ycor()-50):
        ball.setx(-290)
        ball.dx *= -1    



  
