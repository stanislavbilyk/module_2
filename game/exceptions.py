class GameOver(Exception):
    """Исключение вызывается когда у игрока заканчиваются жизни"""

def check_lives(lives):
    if lives > 0:
        print("Вы потеряли одну жизнь")
    else:
        raise GameOver("Жизни игрока закончились")

class EnemyDown(Exception):
    """Исключение вызывается когда у соперника заканчиваются жизни"""

def enemy_lives(lives):
    if lives > 0:
        print("Ваш соперник потерял одну жизнь")
    else:
        raise EnemyDown("Жизни соперника закончились")


class IncorrectInputError(Exception):
    """Исключение при вводе некорректного значения(кроме 1, 2, 3)"""