from case import Case
from pomme import Pomme
from serpent import Serpent
from tkinter import Tk, Canvas


class Game:
    def __init__(self):
        self.direction = [0, -1]
        self.snake = Serpent([Case(7, 20), Case(7, 21), Case(7, 22)])
        self.pomme = Pomme(9, 15)
        self.tk = Tk()
        self.can = Canvas(self.tk, width=500, height=500, bg="black")
        self.can.pack()

    def compute_next_frame(self):
        self.can.delete("all")
        mange_pomme = self.snake.avance(self.direction, self.pomme)
        self.snake.show(self.can)
        if mange_pomme:
            self.pomme.change()
        self.pomme.show(self.can)
        self.tk.after(1000, self.compute_next_frame)

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
