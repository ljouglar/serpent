import random


class Pomme:
    def __init__(self):
        self.x = random.randint(1, 24)
        self.y = random.randint(1, 24)

    def __repr__(self):
        return "Pomme(x=%r, y=%r)" % (self.x, self.y)

    def change(self):
        self.x = random.randint(1, 24)
        self.y = random.randint(1, 24)

    def show(self, canvas):
        canvas.create_oval(self.x * 20, self.y * 20,
                           self.x * 20 + 20, self.y * 20 + 20,
                           outline="blue", fill="blue")
