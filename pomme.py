class Pomme:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return "Pomme(x=%r, y=%r)" % (self.x, self.y)

    def show(self, canvas):
        canvas.create_oval(self.x * 20, self.y * 20,
                           self.x * 20 + 20, self.y * 20 + 20,
                           outline="blue", fill="blue")
