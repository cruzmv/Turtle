import turtle
import time

win = turtle.Screen()
win.title("Pong by MCruz")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

#Paddle A
pda = turtle.Turtle()
pda.speed(0)
pda.shape("square")
pda.color("white")
pda.shapesize(stretch_wid=5, stretch_len=1)
pda.penup()
pda.goto(-350,0)

#Paddle B
pdb = turtle.Turtle()
pdb.speed(0)
pdb.shape("square")
pdb.color("white")
pdb.shapesize(stretch_wid=5, stretch_len=1)
pdb.penup()
pdb.goto(350,0)


#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 1
ball.dy = -1




# Function
#--A
def pda_up():
    y = pda.ycor()
    y += 20
    pda.sety(y)

def pda_down():
    y = pda.ycor()
    y -= 20
    pda.sety(y)

#--B
def pdb_up():
    y = pdb.ycor()
    y += 20
    pdb.sety(y)

def pdb_down():
    y = pdb.ycor()
    y -= 20
    pdb.sety(y)





# Keyboard binding
win.listen()
win.onkeypress(pda_up,"w")
win.onkeypress(pda_down,"s")
win.onkeypress(pdb_up,"Up")
win.onkeypress(pdb_down,"Down")


# Main game loop
while True:
    win.update()

    time.sleep(0.002)

    # Ball moviment
    ball.setx( ball.xcor() + ball.dx )
    ball.sety( ball.ycor() + ball.dy )

    # borders
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *=-1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *=-1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1        
    
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < pdb.ycor() + 40 and ball.ycor() > pdb.ycor() -40 ):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() < -350) and (ball.ycor() < pda.ycor() + 40 and ball.ycor() > pda.ycor() -40 ):
        ball.setx(-340)
        ball.dx *= -1



