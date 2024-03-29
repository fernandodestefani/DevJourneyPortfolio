from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.draw_line()
        self.update_scoreboard()

    def draw_line(self):
        self.home()
        self.penup()
        self.pensize(8)
        self.goto(0, 300)
        self.right(90)
        for c in range(30):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)

    def update_scoreboard(self):
        self.clear()
        self.draw_line()
        self.goto(-100, 190)
        self.write(self.l_score, align='center', font=('Courier', 80, 'normal'))
        self.goto(100, 190)
        self.write(self.r_score, align='center', font=('Courier', 80, 'normal'))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()