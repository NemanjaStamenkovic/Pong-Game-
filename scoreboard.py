from turtle import Turtle


class scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.color("white")
        self.penup()
        self.goto(position)
        self.hideturtle()
        self.update_left()
        self.update_right()


    def increase_left(self):
        self.score_left += 1
        self.clear()
        self.update_left()


    def increase_right(self):
        self.score_right += 1
        self.clear()
        self.update_right()        


    def update_left(self):
        self.write(f"Score: {self.score_left}", font=("Arial", 16, "normal"))


    def update_right(self):  
        self.write(f"Score: {self.score_right}", font=("Arial", 16, "normal"))
