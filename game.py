from case import Case
from pomme import Pomme
from serpent import Serpent
from tkinter import Tk, Canvas


class Game:
    INITIAL_DIRECTION = (0, -1)
    INITIAL_SNAKE_LENGTH = 3
    INITIAL_INTERVAL = 1000

    def __init__(self):
        self.score = 0
        self.interval = self.INITIAL_INTERVAL
        self.direction = self.INITIAL_DIRECTION
        self.snake = Serpent(self.INITIAL_DIRECTION, self.INITIAL_SNAKE_LENGTH)
        self.pomme = Pomme()
        self.tk = Tk()
        self.can = Canvas(self.tk, width=500, height=500, bg="black")
        self.can.pack()

    def compute_next_frame(self):
        self.can.delete("all")
        mange_pomme = self.snake.avance(self.direction, self.pomme)
        self.snake.show(self.can)
        print(self.snake)
        if mange_pomme:
            self.score += 1
            if self.interval > 100:
                self.interval -= 10
            self.pomme.change()
        self.pomme.show(self.can)
        self.tk.after(self.interval, self.compute_next_frame)

    def right(self, event):
        if self.direction[0] != -1:
            self.direction = [1, 0]

    def left(self, event):
        if self.direction[0] != 1:
            self.direction = [-1, 0]

    def up(self, event):
        if self.direction[1] != 1:
            self.direction = [0, -1]

    def down(self, event):
        if self.direction[1] != -1:
            self.direction = [0, 1]

    def run(self):
        self.tk.bind("<d>", self.right)
        self.tk.bind("<q>", self.left)
        self.tk.bind("<z>", self.up)
        self.tk.bind("<s>", self.down)

        self.compute_next_frame()
        self.tk.mainloop()
