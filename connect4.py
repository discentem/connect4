from graphics import *
import math


class Board:
    def __init__(self, win, x, y, rows=6, columns=7, squareSize=1):
        self.win = win
        self.w = squareSize*columns
        self.h = squareSize*rows
        self.x = x
        self.y = y

        self.rows = 6
        self.columns = 7

        self.squareSize = squareSize

        spaces = []
        x_move = 0
        for i in range(self.columns):
            s = Space(win, self.x+x_move, self.y, squareSize)
            spaces.append(s)
            x_move += squareSize
        for space in spaces:
            space.draw()


class Space:
    def mid(self, p1, p2):
        x = (p1.getX() + p2.getX()) / 2
        y = (p1.getY() + p2.getY()) / 2
        return Point(x, y)

    def fill_circle(self, win):
        if self.player == 1:
            self.circle.setFill('Red')
        elif self.player == 2:
            self.circle.setFill('black')

    def __init__(self, win, x, y, w, r=.3, player=0):
        self.win = win
        self.x = x
        self.y = y
        self.w = w
        self.r = r
        self.player = player

        top_left = Point(self.x, self.y)
        bottom_right = Point(self.x+self.w, self.y+self.w)
        self.sq = Rectangle(top_left, bottom_right)
        self.circle = Circle(self.mid(top_left, bottom_right), r)

    def draw(self):
        self.sq.draw(self.win)
        self.fill_circle(win)
        self.circle.draw(self.win)

win = GraphWin('Connect 4 World Tour', 500, 500)
win.setCoords(-1, -1, 20, 20)
b = Board(win, 2, 12, 0, 0)
while(True):
    pass
