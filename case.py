class Case:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return "Case(x=%r, y=%r)" % (self.x, self.y)

    def to_vect(self):
        return self.x, self.y

    def __add__(self, vecteur):
        return Case(self.x + vecteur[0], self.y + vecteur[1])

    def show(self, canvas, tete=False):
        outline = "red" if tete else "blue"
        canvas.create_rectangle(self.x * 20, self.y * 20,
                                self.x * 20 + 20, self.y * 20 + 20,
                                outline=outline, fill="black")
