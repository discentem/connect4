from tkinter import *


class GameWindow(Tk):
    def __init__(self, win_title, square_width=100, square_height=100,
                 num_of_rows=6, num_of_cols=7):
        Tk.__init__(self)

        self.win_title = win_title
        self.title(self.win_title)
        self.resizable(0, 0)

        self.num_of_rows = num_of_rows
        self.num_of_cols = num_of_cols

        self.square_width = square_width
        self.square_height = square_height

        self.win_width = self.num_of_cols*self.square_width+10
        self.win_height = self.num_of_rows*self.square_height+40
        self.geometry(str(self.win_width) + 'x' + str(self.win_height))

        canvas = Canvas(self, width=self.win_width, height=self.win_height)
        canvas.pack()

        board = Board(self, canvas, 5, 5, num_of_rows=self.num_of_rows,
                      num_of_cols=self.num_of_cols,
                      square_width=self.square_width,
                      square_height=self.square_height)
        board.setup()


class Space:
    def mid(self, c='x'):
        if c == 'x':
            return (self.x + self.x+self.w)/2
        else:
            (self.y + self.y+self.h)/2

    def __init__(self, canvas, x, y, w, coords, h=0):
        self.filled = None
        self.canvas = canvas
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.mid_x = self.mid('x')
        self.mid_y = self.mid('y')
        if self.h == 0:
            self.h = self.w

        self.canvas.create_rectangle(self.x, self.y,
                                     self.x+self.w, self.y+self.h)

        c_x1 = self.x+self.w/6
        c_y1 = self.y+self.h/6
        c_x2 = self.x+(self.w)-(self.w/6)
        c_y2 = self.y+(self.h)-(self.h/6)
        self.tag = 's' + coords
        self.circle = self.canvas.create_oval(c_x1, c_y1, c_x2, c_y2,
                                              tags=self.tag)


class Board:
    def __init__(self, win, canvas, x, y, num_of_rows=6, num_of_cols=7,
                 square_width=50, square_height=0):

        self.win = win
        self.canvas = canvas
        self.x = x
        self.y = y
        self.num_of_rows = num_of_rows
        self.num_of_cols = num_of_cols
        self.board = []
        self.space_count = 1

        self.square_width = square_width
        self.square_height = square_height
        if self.square_height == 0:
            self.square_height = self.square_width

    def drop_piece(self, row, player=1):
        print("coord", 's'+str(0)+row)
        if player == 1:
            self.canvas.itemconfig('s'+str(0)+row, fill="blue")
        if player == 2:
            self.canvas.itemconfig(1, fill="red")

    def setup(self):
        board = []
        x_move = 0
        y_move = 0
        buttons = []
        for i in range(self.num_of_rows+1):
            row = []
            for j in range(self.num_of_cols):
                if i == self.num_of_rows:
                    s = Button(self.win, text="OK",
                               width=int(self.square_width/12),
                               command=lambda i=j: self.drop_piece(str(i)))

                    buttons.append(s)
                    s.pack()
                    s.place(x=self.x+x_move,
                            y=self.y+y_move+10)
                else:
                    s = Space(self.canvas, self.x+x_move, self.y+y_move,
                              self.square_width, str(i)+str(j),
                              self.square_height)
                    self.space_count += 1

                row.append(s)
                x_move += self.square_width
            board.append(row)
            y_move += self.square_height
            x_move = 0
        self.board = board


win = GameWindow("Connect4")
win.mainloop()
