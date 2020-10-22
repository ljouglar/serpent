class Case:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return "Case(x=%r, y=%r)" % (self.x, self.y)

    def __add__(self, vecteur):
        return Case(self.x + vecteur[0], self.y + vecteur[1])
