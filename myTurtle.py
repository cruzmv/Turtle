import turtle
import time

class myTurtle:
    pixMov = 20
    win = turtle.Screen()
    title = turtle.Turtle()
    mypixTurtle = turtle.Turtle()

    ball = []

    sholder = [ [-260,turtle.Turtle()],
                [-160,turtle.Turtle()],
                [-60,turtle.Turtle()],
                [40,turtle.Turtle()],
                [140,turtle.Turtle()],
                [240,turtle.Turtle()]
              ]
    score = 0
    points = 0

    def turtle_up(self):
        y = self.mypixTurtle.ycor()
        y += self.pixMov
        self.mypixTurtle.sety(y)

    def turtle_down(self):
        y = self.mypixTurtle.ycor()
        y -= self.pixMov
        self.mypixTurtle.sety(y)

    def turtle_right(self):
        x = self.mypixTurtle.xcor()
        x += self.pixMov
        self.mypixTurtle.setx(x)

    def turtle_left(self):
        x = self.mypixTurtle.xcor()
        x -= self.pixMov
        self.mypixTurtle.setx(x)

    def reTitle(self):
        self.title.clear()
        #self.title.write("X: {}  X: {}  -  Score: {} - Points: {}".format(self.mypixTurtle.xcor(),self.mypixTurtle.ycor(),self.score,self.points),align="center", font=("Courier", 24, "normal"))
        self.title.write("Score: {} - Points: {}".format(self.score,self.points),align="center", font=("Courier", 24, "normal"))

    def myTitle(self):
        self.title.speed(0)
        self.title.color("white")
        self.title.penup()
        self.title.hideturtle()
        self.title.goto(2,260)

    def myBall(self,cl,x,y):
        bl1 = turtle.Turtle()
        bl1.speed(0)
        bl1.shape("circle")
        bl1.color(cl)
        bl1.penup()
        bl1.goto(x,y)
        bl1.dx = 1
        bl1.dy = -1
        return(bl1)

    def pixTurtle(self):
        self.mypixTurtle.speed(0)
        self.mypixTurtle.shape("turtle")
        self.mypixTurtle.color("green")
        self.mypixTurtle.penup()
        self.mypixTurtle.goto(-300,-260)

    def line(self,x,y,myLine):
        myLine.speed(0)
        myLine.shape("square")
        myLine.color("white")
        myLine.shapesize(stretch_wid=1, stretch_len=300)
        myLine.penup()
        myLine.goto(x,y)
        return(self)

    def level(self,x,y):
        self.ball.append(self.myBall("red",x,y))
        self.ball.append(self.myBall("blue",x,y-20))
        self.ball.append(self.myBall("yellow",x,y-40))
        self.ball.append(self.myBall("gray",x,y-60))

    def init(self):
        self.win.title("Lab1 by MCruz")
        self.win.bgcolor("black")
        self.win.setup(width=800, height=600)
        self.win.tracer(0)

        for n in self.sholder:
            self.line(-350,n[0],n[1])
            if n[0]>-260:
                self.level(380,n[0]-20)

        self.pixTurtle()
        self.myTitle()

    def myScore(self):
        if self.mypixTurtle.ycor() == self.sholder[0][0]:
            self.score = 1
            self.sholder[0][1].color("gray")
        if self.mypixTurtle.ycor() == self.sholder[1][0]:
            self.score = 5
            self.sholder[1][1].color("gray")
        if self.mypixTurtle.ycor() == self.sholder[2][0]:
            self.score = 10
            self.sholder[2][1].color("gray")
        if self.mypixTurtle.ycor() == self.sholder[3][0]:
            self.score = 20
            self.sholder[3][1].color("gray")
        if self.mypixTurtle.ycor() == self.sholder[4][0]:
            self.score = 50
            self.sholder[4][1].color("gray")
        if self.mypixTurtle.ycor() == self.sholder[5][0]:
            self.sholder[5][1].color("gray")
            self.score = 100
            self.points += 1
            self.mypixTurtle.goto(-300,-260)
            for n in self.sholder:
                n[1].color("white")


    def action(self):
        # Ball moviment
        speed = 0.0000
        index = 0
        for bl in self.ball:
            bl.setx( bl.xcor() - bl.dx - speed)
            speed += 0.8

            #First Level
            if bl.xcor()<= -400:
                bl.setx(380)
                bl.sety(bl.ycor()-self.pixMov)

            #Second Level
            if index<=3:
                if bl.ycor()<=-260:
                    bl.setx(380)
                    bl.sety(-180)

            #Third Level
            if index>=4 and index<=7:
                if bl.ycor()<=-160:
                    bl.setx(380)
                    bl.sety(-80)

            #fourth Level
            if index>=8 and index<=11:
                if bl.ycor()<=-60:
                    bl.setx(380)
                    bl.sety(20)

            #Fifth Level
            if index>=12 and index<=15:
                if bl.ycor()<=60:
                    bl.setx(380)
                    bl.sety(120)

            #Sixth Level
            if index>=16:
                if bl.ycor()<=160:
                    bl.setx(380)
                    bl.sety(220)

            # tutle hit
            if self.mypixTurtle.ycor() == bl.ycor() and self.mypixTurtle.xcor()+10 >= bl.xcor() and  self.mypixTurtle.xcor()<=bl.xcor():
                self.mypixTurtle.goto(-300,-260)

            index +=1

        self.myScore()

    def __init__(self):
        #self.init()

        # Keyboard binding
        self.win.listen()
        self.win.onkeypress(self.turtle_up,"Up")
        self.win.onkeypress(self.turtle_down,"Down")
        self.win.onkeypress(self.turtle_right,"Right")
        self.win.onkeypress(self.turtle_left,"Left")

mt = myTurtle()
mt.init()

while True:
    mt.win.update()
    time.sleep(0.002)
    mt.reTitle()
    mt.action()
    
