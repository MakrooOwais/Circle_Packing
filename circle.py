from turtle import width
from p5 import *
from random import randint


class Circle:
    def __init__(self, i, j) -> None:
        self.x = i
        self.y = j
        self.r = 3
        self.growing = True

    def show(self):
        stroke(255)
        stroke_weight(1)
        no_fill()
        ellipse(self.x, self.y, self.r * 2, self.r * 2)

    def set_w_h(self, w_, h_):
        global width, height
        width = w_
        height = h_

    def grow(self):
        if self.growing:
            if self.r <= 15:
                self.r = self.r + 0.5

    def edges(self) -> bool:
        return (
            self.x + self.r > width
            or self.x - self.r < 0
            or self.y + self.r > height
            or self.y - self.r < 0
        )
