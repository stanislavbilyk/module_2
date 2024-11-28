from game import settings
from game import exceptions
import random
import psycopg2
from psycopg2.errors import UniqueViolation


class Player:
    lives: int
    def __init__(self) -> None:
        """для инициализации игрока, принимает только имя, назначает имя, кол-во жизней и очков."""
        #Имя игрока, задается пользователем через консоль
        self.name = input("Введите имя игрока: ")
        try:
            with psycopg2.connect(
                dbname="module_2",
                user="player",
                password="mypass"
            ) as conn:
                with conn.cursor() as cur:
                    cur.execute("insert into player (name) values (%s);", (self.name,))
                    print("Данные успешно добавлены.")
        except UniqueViolation:
            print("User already exist")
        if not self.name.strip():  # Проверка на пустую строку или строку, состоящую из пробелов
            raise exceptions.ValidationName("Имя пользователя не может быть пустым или состоять только из пробелов.")
        #Количество жизней, берется из константы из settings.py
        self.lives = settings.PLAYER_LIVES
        if self.lives < 0:
            raise exceptions.ValidationLives
        #Очки игрока, изначально 0
        self.score = 0
        print(f"Приветствую, {self.name}!")

    def select_attack(self):
        """метод для ввода атаки игроком. Вводим до тех пор, пока пользователь не введет валидное значение (1, 2, 3),
        использует константы из файла settings.py"""
        while True:
            attack = input("Введите 1:камень, 2:ножницы или 3:бумага для атаки: ")
            try:
                attack = int(attack)
                if attack not in (1, 2, 3):
                    raise exceptions.IncorrectAttackError
            except ValueError:
                print("Не правильный ввод! Введите 1, 2 или 3")
                continue
            except exceptions.IncorrectAttackError:
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
            check_lives(self.lives)
        except exceptions.GameOver as e:
            print(e)
            raise


    def add_score(self, points: int, mode: int):
        """метод для начисления очков игроку"""
        if mode == 1:
            self.score += points
        elif mode == 2:
            self.score += points * settings.HARD_MODE_MULTIPLIER
        print(f"Points added: {points}, Mode: {mode}, Current Score: {self.score}")


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
            enemy_lives(self.lives)
            # return settings.POINTS_FOR_FIGHT
        except exceptions.EnemyDown as e:
            print(e)
            # game.create_enemy(self.level, self.lives)
            # return settings.POINTS_FOR_KILLING
            raise

def check_lives(lives):
    if lives > 0:
        print("Вы потеряли одну жизнь")
    else:
        raise exceptions.GameOver("Жизни игрока закончились")

def enemy_lives(lives):
    if lives > 0:
        print("Ваш соперник потерял одну жизнь")
    else:
        raise exceptions.EnemyDown("Жизни соперника закончились")