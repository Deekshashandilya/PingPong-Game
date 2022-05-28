from turtle import Turtle


class CreatePaddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)
        self.move_up()
        self.move_down()

    def move_down(self):
        new_y = self.ycor() - 30
        self.goto(x=self.xcor(), y=new_y)

    def move_up(self):
        new_y = self.ycor() + 30
        self.goto(x=self.xcor(), y=new_y)
