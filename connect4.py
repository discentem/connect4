import tkinter as tk


class Space(tk.Canvas):
    def __init__(self, board, width, row, column, height=0):
        self.board = board
        self.width = width
        self.height = height
        self.row = row
        self.column = column
        if self.height == 0:
            self.height = self.width

        # instantiate Canvas
        super().__init__(width=self.width, height=self.height)
        # set board colors
        self.config(background="yellow", highlightbackground="black",
                    highlightthickness=.5)
        # create button
        self.bind("<Button-1>", self.clicked)
        # add to parent grid
        self.grid(row=self.row, column=self.column)

        inset = 6
        self.circle = self.create_oval(self.width/inset, self.height/inset,
                                       self.width - self.width/inset,
                                       self.height - self.height/inset)

    def clicked(self, event):
        self.board.drop_piece(self.row, self.column)


class Board(tk.Tk):

    def __init__(self, rows=6, cols=7,
                 square_width=80, square_height=0,
                 player_colors=['red', 'green']):

        self.rows = rows
        self.cols = cols
        self.square_width = square_width
        self.square_height = square_height
        self.p_colors = player_colors

        self.player = 1

        super().__init__()
        self.resizable(width=False, height=False)
        self.grid = []
        for x in range(0, rows):
            row = []
            for y in range(0, cols):
                s = Space(self, square_width, x, y, height=self.square_height)
                row.append(s)
            self.grid.append(row)

    def drop_piece(self, row, col):
        for i in range(self.rows-1, -1, -1):
            space = self.grid[i][col]
            c1 = space.itemcget(1, 'fill') == self.p_colors[0]
            c2 = space.itemcget(1, 'fill') == self.p_colors[1]
            if not(c1) and not(c2):
                if self.player == 1:
                    space.itemconfig(1, fill=self.p_colors[0])
                    self.player = -1
                elif self.player == -1:
                    space.itemconfig(1, fill=self.p_colors[1])
                    self.player = 1
                break

board = Board()
board.mainloop()
