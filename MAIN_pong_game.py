from game_items import Racquet, Ball, setup_screen

screen = setup_screen()

rac_a = Racquet(-350, 0)
rac_b = Racquet(350, 0)

ball = Ball()

# Scores
# scores = ScoreTab(0, 0)

#  Moving Racquets
screen.listen()
screen.onkeypress(rac_a.move_up, "w")
screen.onkeypress(rac_a.move_down, "s")
screen.onkeypress(rac_b.move_up, "Up")
screen.onkeypress(rac_b.move_down, "Down")

while True:


    screen.update()
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Borders
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        # score_a += 1
        # scores.clear()
        # scores.write(f"PLAYER 1: {score_a}        PLAYER 2: {score_b} ", align="center", font=("Curier", 24, "normal"))

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        # score_b += 1
        # scores.clear()
        # scores.write(f"PLAYER 1: {score_a}        PLAYER 2: {score_b} ", align="center", font=("Curier", 24, "normal"))

    # collision
    if 350 > ball.xcor() > 340 \
            and (ball.ycor() < rac_b.ycor() + 40) and (ball.ycor() > rac_b.ycor() - 40):
        ball.dx *= -1

    if -350 > ball.xcor() < -340 \
            and (ball.ycor() < rac_a.ycor() + 40) and (ball.ycor() > rac_a.ycor() - 40):
        ball.dx *= -1

