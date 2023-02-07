from turtle import Screen, Turtle
from paddles import padle
from ball import ball
import time
from scoreboard import scoreboard


#screen
screen = Screen()
screen.setup(width = 800, height= 600)
screen.bgcolor("Black")
screen.title("Pong")
screen.tracer(0)


#paddles 
leftPadle = padle((-350, 0))
rightPadle = padle((350, 0))
pongBall = ball()
score_left_player = scoreboard((-210, 260))
score_right_player = scoreboard((210, 260))


#screen settings
screen.listen()
screen.onkey(rightPadle.go_up, "Up")
screen.onkey(rightPadle.go_down, "Down")
screen.onkey(leftPadle.go_up, "w")
screen.onkey(leftPadle.go_down, "s")


#scores 
leftPlayerScore = 0
rightPlayerScore = 0


#game brain
game_is_on = True

while game_is_on:
    time.sleep(pongBall.timer_sleep)
    screen.update()
    pongBall.move()


    if pongBall.ycor() > 280 or pongBall.ycor() < -280:
        pongBall.bounce()


    if pongBall.distance(rightPadle) < 50 and pongBall.xcor() > 330 or pongBall.distance(leftPadle) < 50 and pongBall.xcor() < -330:
        pongBall.revert()
        

    if pongBall.xcor() > 380:
        score_left_player.increase_left()
        pongBall.resetball()
    elif pongBall.xcor() < -380:
        score_right_player.increase_right()
        pongBall.resetball()


screen.exitonclick()