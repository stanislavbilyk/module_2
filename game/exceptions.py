class GameOver(Exception):
    """Исключение вызывается когда у игрока заканчиваются жизни"""

class EnemyDown(Exception):
    """Исключение вызывается когда у соперника заканчиваются жизни"""

class IncorrectAttackError(Exception):
    """Исключение при вводе некорректного значения(кроме 1, 2, 3)"""

class ValidationMode(Exception):
    """Исключение при вводе некорректного значения уровня сложности(кроме 1 или 2)"""

class ValidationName(Exception):
    """Исключение при вводе некорректного значения имени пользователя"""

class ValidationLives(Exception):
    """Исключение при вводе некорректного значения количества жизней"""

class ValidationFight(Exception):
    """Исключение при выводе некорректного значения метода fight"""

class IncorrectMenuInput(Exception):
    """Исключение при выборе некорректного значения меню(кроме 1, 2, 3)"""

