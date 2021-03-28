from turtle import Turtle

SCORE_POSITION = (0, 240)


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.color('white')
        self.penup()
        self.setpos(SCORE_POSITION)
        self.write('Score:', True, align='center', font=('Arial', 9, 'bold'))
        self.left_score = 0
        self.right_score = 0

    def update(self, winner):
        if winner == 'left':
            self.left_score += 1
            self.print_score()
        elif winner == 'right':
            self.right_score += 1
            self.print_score()

    def print_score(self):
        self.clear()
        self.setpos(SCORE_POSITION)
        self.write(f'{self.left_score}     {self.right_score}', True, align='center',
                   font=('Arial', 30, 'bold'))

    def end_game(self):
        self.clear()
        self.home()
        self.write('Game Over!', True, align='center', font=('Arial', 18, 'bold'))
