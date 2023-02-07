from turtle import Turtle


class ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.timer_sleep = 0.1


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)


    def bounce(self):
        self.y_move *= -1


    def revert(self):
        self.x_move *= -1
        self.timer_sleep *= 0.9


    def resetball(self):
        self.goto(0,0)
        self.revert()
        self.timer_sleep = 0.5

        


    
