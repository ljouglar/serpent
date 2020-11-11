import random
from case import Case


class Serpent:
    def __init__(self, direction, length):
        self.tete = Case(random.randint(length, 24 - length), random.randint(length, 24 - length))
        self.queue = []
        for i in range(length - 1):
            self.queue.append(Case(self.tete.x - (i + 1) * direction[0],
                                   self.tete.y - (i + 1) * direction[1]))

    def __str__(self):
        snake_str = "tete(%d, %d)" % self.tete.to_vect()
        for case in self.queue:
            snake_str += "_(%d, %d)" % case.to_vect()
        return snake_str

    def longueur(self):
        return len(self.queue) + 1

    def avance(self, direction, pomme):
        # D'abord on calcule les nouvelles coordonnées de la tête
        new_tete_x = self.tete.x + direction[0]
        new_tete_y = self.tete.y + direction[1]
        # Puis on détermine si la tête va être sur la même case que la pomme (le serpent mange la pomme)
        mange_pomme = pomme.x == new_tete_x and pomme.y == new_tete_y
        if mange_pomme: # Si le serpent mange la pomme on ajoute une écaille au serpent
            self.queue.append(Case(0, 0)) # On la met en (0,0) car elle prendra les coords de la dernière case

        # La liste des index inversés dans la queue du serpent
        index_list = reversed(range(self.longueur() - 1))
        # C'est à dire qu'on part de la dernière écaille et on remonte jusqu'à la première
        for index in index_list:
            if index == 0:  # Première écaille (en dernier dans la liste), elle prend les coords de la tête
                self.queue[index].x = self.tete.x
                self.queue[index].y = self.tete.y
            else:  # Toutes les autres écaille prennent les coords de l'écaille qui la précède
                self.queue[index].x = self.queue[index - 1].x
                self.queue[index].y = self.queue[index - 1].y

        # Enfin, la tête prend ses nouvelles coords
        self.tete.x = new_tete_x
        self.tete.y = new_tete_y
        return mange_pomme

    def tete_in_queue(self):
        for case in self.queue:
            if self.tete.x == case.x and self.tete.y == case.y:
                return True
        return False

    def hors_zone(self):
        return self.tete.x < 0 or self.tete.y < 0 or self.tete.x > 24 or self.tete.y > 24

    def show(self, canvas):
        self.tete.show(canvas, True)
        for case in self.queue:
            case.show(canvas)
