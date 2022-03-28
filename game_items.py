from turtle import Screen, Turtle


def setup_screen():
    sc = Screen()
    sc.title("@@ Unicorn Pong @@")
    sc.bgcolor("#f5cac3")
    sc.bgpic("unicorn.gif")
    sc.setup(width=800, height=600)
    return sc

# class PongScreen(Screen):
#     def __init__(self):
#         super().__init__()
#         self.title("@@ Unicorn Pong @@")
#         self.bgcolor("#f5cac3")
#         self.bgpic("unicorn.gif")
#         self.setup(width=800, height=600)
#         self.tracer(0)
        # while True:
        #     self.update()


# not working :(
class Racquet(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.speed(0)
        self.shape(name="square")
        self.shapesize(stretch_wid=5, stretch_len=0.5, outline=None)
        self.color("#f28482")
        self.penup()
        self.goto(x, y)

    def move_up(self):
        y = self.ycor()
        y += 20
        return self.sety(y)

    def move_down(self):
        y = self.ycor()
        y -= 20
        return self.sety(y)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape("circle")
        self.color("#f6bd60")
        self.penup()
        self.goto(0, 0)
        self.dx = 10
        self.dy = 10

    def check_boundarise(self):
        if self.ycor() > 290:
            self.sety(290)
            self.dy *= -1

        if self.xcor() > 390:
            self.goto(0, 0)
            self.dx *= -1

        if self.ycor() < -290:
            self.sety(-290)
            self.dy *= -1

        if self.xcor() < -390:
            self.goto(0, 0)
            self.dx *= -1


# class ScoreTab():
#     def __init__(self, score_a, score_b):
#         self = turtle.Turtle()
#         self.speed(0)
#         self.color("#227c9d")
#         self.penup()
#         self.hideturtle()
#         self.goto(0, 260)
#         self.showturtle()
#         self.score_a = score_a
#         self.score_b = score_b
#         self.write(f"PLAYER 1: {score_a}        PLAYER 2: {score_b} ", align="center", font=("Curer", 24, "normal"))
