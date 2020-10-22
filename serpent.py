class Serpent:
    def __init__(self, cases):
        self.tete = cases[0]
        self.queue = cases[1:]

    def longueur(self):
        return len(self.queue) + 1

    def avance(self, direction):
        # Chaque écaille prend la place de l'écaille qui la précède
        cases = [self.tete] + self.queue
        for index in reversed(range(self.longueur())):
            cases[index].x = cases[index - 1].x
            cases[index].y = cases[index - 1].y
        self.tete.x += direction[0]
        self.tete.y += direction[1]
