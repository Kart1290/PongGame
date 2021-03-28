from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self, width, height):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.x_direction = random.choice([-10, -5, -2, 2, 5, 10])
        self.y_direction = random.choice([-10, -5, -2, 2, 5, 10])
        self.x_boundary = (-1*((width/2)-20), (width/2)-20)
        self.y_boundary = (-1*((height/2)-20), (height/2)-20)

    def move(self):
        if self.ycor() <= self.y_boundary[0] or self.ycor() >= self.y_boundary[1]:
            self.y_direction *= -1
            if self.x_direction > 0:
                self.x_direction = random.choice([2, 5, 10])
            elif self.x_direction < 0:
                self.x_direction = random.choice([-2, -5, -10])
            self.setpos(self.xcor()+self.x_direction, self.ycor()+self.y_direction)
        elif self.xcor() <= self.x_boundary[0] or self.xcor() >= self.x_boundary[1]:
            self.ht()  # Print something to screen
            self.home()
            self.random_direction()
            self.st()
        else:
            self.setpos(self.xcor() + self.x_direction, self.ycor() + self.y_direction)

    def hit(self):
        if self.x_direction < 0:
            self.x_direction = random.choice([2, 5, 10])
        elif self.x_direction > 0:
            self.x_direction = random.choice([-2, -5, -10])

        if self.y_direction < 0:
            self.y_direction = random.choice([2, 5, 10])
        elif self.y_direction > 0:
            self.y_direction = random.choice([-2, -5, -10])
        # self.y_direction *= -1
        # self.x_direction *= -1

    def random_direction(self):
        self.x_direction = random.choice([-10, 10])
        self.y_direction = random.choice([-10, 10])
