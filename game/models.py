from game import settings
from game import exceptions
import random


class Player:
    lives: int
    def __init__(self, lives: int = 2, score: int = 0) -> None:
        """для инициализации игрока, принимает только имя, назначает имя, кол-во жизней и очков."""
        #Имя игрока, задается пользователем через консоль
        self.name = input("Введите имя игрока: ")
        #Количество жизней, берется из константы из settings.py
        self.lives = lives
        #Очки игрока, изначально 0
        self.score = score
        print(f"Приветствую, {self.name}!")

    def select_attack(self):
        """метод для ввода атаки игроком. Вводим до тех пор, пока пользователь не введет валидное значение (1, 2, 3),
        использует константы из файла settings.py"""
        while True:
            attack = input("Введите 1:камень, 2:ножницы или 3:бумага для атаки: ")
            try:
                attack = int(attack)
                if attack not in (1, 2, 3):
                    raise exceptions.IncorrectInputError
            except ValueError:
                print("Не правильный ввод! Введите 1, 2 или 3")
                continue
            except exceptions.IncorrectInputError:
                print("Не правильный ввод! Введите 1, 2 или 3")
                continue
            else:
                print(f"Ваш ход: {settings.ALLOWED_ATTACKS[str(attack)]}")
                return settings.ALLOWED_ATTACKS[str(attack)]

    def decrease_lives(self):
        """метод, который будет вызываться если игрок проиграл "бой", уменьшает жизни на 1.
        Если жизни закончились, вызывает исключение GameOver из файла exceptions.py"""
        self.lives -= 1
        try:
            exceptions.check_lives(self.lives)
        except exceptions.GameOver as e:
            print(e)
            raise


    def add_score(self, points):
        """метод для начисления очков игроку"""
        self.score += points



# john = Player("John")
# print(john.select_attack())


class Enemy:
    #Кол-во жизней, изначально зависит от уровня соперника и уровня сложности,
    #уменьшается на 1 когда соперник проигрывает бой
    lives: int
    #уровень соперника, будет увеличиваться с каждым новым соперником. Изначально 1
    level: int
    def __init__(self, level: int, mode: int) -> None:
        """для инициализации соперника, принимает только уровень и сложность, чтобы вычислить кол-во жизней,
        назначает кол-во жизней и уровень"""
        self.level = level
        self.lives = level * mode
        print(f"Создание соперника: уровень {self.level}, жизни {self.lives}, режим {settings.MODES[str(mode)]}")

    def select_attack(self):
        """метод для случайного выбора атаки (1, 2, 3), использует константы из файла settings.py"""
        random_attack = settings.ALLOWED_ATTACKS[str(random.randint(1, 3))]
        print(f"Ход соперника: {random_attack}")
        return random_attack

    def decrease_lives(self):
        """уменьшает жизни при проигрыше "боя", вызывает исключение EnemyDown из файла exceptions.py,
         если у соперника закончились жизни"""
        self.lives -= 1
        try:
            exceptions.enemy_lives(self.lives)
            return settings.POINTS_FOR_FIGHT
        except exceptions.EnemyDown as e:
            print(e)
            # game.create_enemy(self.level, self.lives)
            return settings.POINTS_FOR_KILLING

# en = Enemy(1, 1)

# print(f"Ход соперника: {en.select_attack()}")
# print(en.lives)