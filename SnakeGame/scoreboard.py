from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.goto(0, 250)
        self.write(f"Score: {self.score}   High Score: {self.high_score}", True, align="center",
                   font=("Arial", 24, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    # def game_over(self):
    #   self.goto(0,0)
    #   self.write("GAME OVER", True, align="center", font=("Arial", 24 , 'normal'))

    def increase_score(self):
        self.score += 1
        self.update_score()
        self.goto(0, 250)
