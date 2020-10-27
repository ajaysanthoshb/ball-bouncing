import turtle
import time
import random

wn = turtle.Screen()
wn.setup(700,700)
wn.title("ball bouncing simulator")
wn.bgcolor("black")
wn.tracer(0)

shapes = ["triangle","square","circle"]
colors = ["white","pink","lime","red","purple","orange","yellow"]
balls = []
for i in range(15):
 ball = turtle.Turtle()
 ball.color(random.choice(colors))
 ball.shape(random.choice(shapes))
 ball.penup()
 ball.speed(0)
 ball.goto(random.randint(-290,290),random.randint(200,395))
 ball.dy = 0
 ball.dx = random.randint(-4,4)
 ball.da = random.randint(-5,5)
 balls.append(ball)
gravity = 1

while True:
  wn.update()
  for ball in balls:
    ball.rt(ball.da)
    ball.dy -= gravity
    ball.sety(ball.ycor()+ball.dy)
    ball.setx(ball.xcor()+ball.dx)

    if(ball.xcor() < -290):
        ball.dx *= -1
        ball.da *= -1

    if(ball.xcor() > 290):
        ball.dx *= -1
        ball.da *= -1

    if(ball.ycor() < -290):
        ball.sety(-290)
        ball.dy *= -1
        ball.da *= -1
  time.sleep(0.02)
