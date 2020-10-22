from case import Case
from serpent import Serpent


if __name__ == '__main__':
    snake = Serpent([Case(7, 10), Case(7, 11), Case(7, 12)])  # definition du serpent
    print("longueur du serpent : ", snake.longueur())
    print("abscisse de la tete : ", snake.tete.x)
    print("ordonnee de la tete : ", snake.tete.y)
    print("abscisse de la premiere ecaille de la queue : ", snake.queue[0].x)
    print("ordonnee de la premiere ecaille de la queue : ", snake.queue[0].y)
    print("abscisse de la deuxieme ecaille de la queue : ", snake.queue[1].x)
    print("ordonnee de la deuxieme ecaille de la queue : ", snake.queue[1].y)
    snake.avance([1, 0])
    print("longueur du serpent : ", snake.longueur())
    print("abscisse de la tete : ", snake.tete.x)
    print("ordonnee de la tete : ", snake.tete.y)
    print("abscisse de la premiere ecaille de la queue : ", snake.queue[0].x)
    print("ordonnee de la premiere ecaille de la queue : ", snake.queue[0].y)
    print("abscisse de la deuxieme ecaille de la queue : ", snake.queue[1].x)
    print("ordonnee de la deuxieme ecaille de la queue : ", snake.queue[1].y)