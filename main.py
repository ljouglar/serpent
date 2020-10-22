from case import Case
from serpent import Serpent
from tkinter import Tk, Canvas


def compute_next_frame():
    global snake
    global direction
    can.delete("all")
    snake.avance(direction)
    snake.show(can)
    tk.after(100, lambda: compute_next_frame())


def right(event):
    global direction
    direction = [1, 0]


def left(event):
    global direction
    direction = [-1, 0]


def up(event):
    global direction
    direction = [0, -1]


def down(event):
    global direction
    direction = [0, 1]


if __name__ == '__main__':
    snake = Serpent([Case(7, 10), Case(7, 11), Case(7, 12)])
    direction = [0, -1]
    tk = Tk()
    can = Canvas(tk, width=500, height=500, bg="black")
    can.pack()

    tk.bind("<d>", right)
    tk.bind("<q>", left)
    tk.bind("<z>", up)
    tk.bind("<s>", down)

    compute_next_frame()
    tk.mainloop()
