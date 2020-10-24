from case import Case


class Serpent:
    def __init__(self, cases):
        self.tete = cases[0]
        self.queue = cases[1:]

    def __str__(self):
        snake_str = "tete(%d, %d)" % self.tete.to_vect()
        for case in self.queue:
            snake_str += "_(%d, %d)" % case.to_vect()
        return snake_str

    def longueur(self):
        return len(self.queue) + 1

    def avance(self, direction, mange_pomme=False):
        if mange_pomme:
            self.queue.append(Case(0, 0))
        # Chaque écaille prend la place de l'écaille qui la précède
        for index in reversed(range(self.longueur() - 1)):
            if index == 0:
                self.queue[index].x = self.tete.x
                self.queue[index].y = self.tete.y
            else:
                self.queue[index].x = self.queue[index - 1].x
                self.queue[index].y = self.queue[index - 1].y
        self.tete.x += direction[0]
        self.tete.y += direction[1]

    def show(self, canvas):
        self.tete.show(canvas, True)
        for case in self.queue:
            case.show(canvas)
