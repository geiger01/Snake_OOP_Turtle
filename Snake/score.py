from turtle import Turtle, Screen

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0,260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align="center", font=("Ariel",30, "normal"))
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score=self.score
            with open("data.txt",'w') as data:
                data.write(f"{self.high_score}")

        self.score = 0
        self.update_score()



    def score_up(self):
        self.score += 1
        self.update_score()


