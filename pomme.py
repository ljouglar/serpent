import random

class Pomme:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return "Pomme(x=%r, y=%r)" % (self.x, self.y)

    def to_vect(self):
        return self.x, self.y

    def change(self):
        self.x = random.randint(0, 30)
        self.y = random.randint(0, 30)

    def show(self, canvas):
        canvas.create_oval(self.x * 20, self.y * 20,
                           self.x * 20 + 20, self.y * 20 + 20,
                           outline="blue", fill="blue")
