from graphics import *
import tkinter

'''
class Button(tkinter.Button):

    def __init__(self):
        self.win = win
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.coords = coords

        self.top_left = Point(self.x, self.y)
        self.bottom_right = Point(self.x+self.w, self.y+self.h)

        self.frame = Rectangle(self.top_left, self.bottom_right)

    def draw(self):
        self.frame.draw(self.win)

    def clicked(self):
            return self.coords
'''

class Space:
    def mid(self, p1, p2):
        x = (p1.getX() + p2.getX()) / 2
        y = (p1.getY() + p2.getY()) / 2
        return Point(x, y)

    def fill_circle(self, player):
        if self.circle:
            if player == 1:
                self.circle.setFill('Red')
            elif player == -1:
                self.circle.setFill('Black')

    def __init__(self, win, x, y, w, h=0, circle=True):
        self.win = win
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.circle = circle
        if h == 0:
            self.h = self.w
        self.r = self.w/3

        self.top_left = Point(self.x, self.y)
        self.bottom_right = Point(self.x+self.w, self.y+self.h)

        self.sq = Rectangle(self.top_left, self.bottom_right)
        if self.circle:
            self.circle = Circle(self.mid(self.top_left, self.bottom_right),
                                 self.r)

    def draw(self):
        self.sq.draw(self.win)
        self.fill_circle(self.win)
        if type(self.circle) != bool:
            self.circle.draw(self.win)


class Board:
    def coords(self, i, j):
        return(i, j)
    def __init__(self, win, x, y, num_of_rows=6, num_of_cols=7, squareSize=3):  # noqa
        self.win = win
        self.x = x
        self.y = y
        self.num_of_rows = num_of_rows
        self.num_of_cols = num_of_cols
        self.rows = []

        self.squareSize = squareSize

    def setup(self):
        board = []
        x_move = 0
        y_move = 0
        for i in range(self.num_of_rows+1):
            print(i)
            row = []
            for j in range(self.num_of_cols):
                # s = None
                if i == self.num_of_rows:
                    '''
                    s = Space(win, self.x+x_move, self.y+y_move,
                              self.squareSize, h=self.squareSize/2,
                              circle=False)
                    '''
                    b = tkinter.Button(self.win, text="Hello", command=self.coords(i, j))

                else:
                    s = Space(win, self.x+x_move, self.y+y_move,
                              self.squareSize)  # noqa

                row.append(s)
                x_move += self.squareSize
            board.append(row)
            y_move += self.squareSize
            x_move = 0

        self.board = board

    def chk_button_processes(self):
        pool = ThreadPool(5)
        results = []
        for b in self.board[-1]:
            results = pool(b)
            pool.close()
            pool.join()
        print(results)

    def display(self):
        for row in self.board:
            for space in row:
                space.draw()


class Game:
    def __init__(self, board):
        self.board = board

        self.board.setup()
        self.board.display()

    def play(self, turn):
        for row in self.board.rows:
            for space in row:
                if space.clicked():
                    print(space)


win = GraphWin('Connect 4', 540, 500)
win_w = win.getWidth()
win_h = win.getHeight()


board = Board(win, 0, 0, squareSize=70)
board.setup()
board.display()

board.chk_button_processes()
