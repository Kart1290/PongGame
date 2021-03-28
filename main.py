from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MAX_SCORE = 5

screen = Screen()
screen.bgcolor('black')
screen.title('Kart_PonG')
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))

screen.update()
screen.tracer(1)

game_ball = Ball(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
score_board = Score()

screen.listen()
screen.onkey(left_paddle.move_up, 'w')
screen.onkey(left_paddle.move_down, 's')
screen.onkey(right_paddle.move_up, 'Up')
screen.onkey(right_paddle.move_down, 'Down')

game_on = True
game_speed = 0.01
while game_on:
    time.sleep(game_speed)

    if (left_paddle.distance(game_ball.pos()) <= 110 and (game_ball.xcor() == -340)) or \
            (right_paddle.distance(game_ball.pos()) <= 110 and (game_ball.xcor() == 340)):
        game_ball.hit()

    if game_ball.xcor() >= game_ball.x_boundary[1]:
        score_board.update(winner='left')
        game_speed /= 1.25
    elif game_ball.xcor() <= game_ball.x_boundary[0]:
        score_board.update(winner='right')
        game_speed /= 1.25

    game_ball.move()

    if score_board.left_score == MAX_SCORE or score_board.right_score == MAX_SCORE:
        game_on = False
        game_ball.ht()
        score_board.end_game()

screen.exitonclick()
