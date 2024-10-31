from . import settings
from game import exceptions
from .models import Player, Enemy
from .score import ScoreHandler


class Game:
    #объект соперника, при убийстве будет создан новый, с более высоким уровнем
    # player: Player
    # enemy: Enemy
    #уровень сложности, normal или hard, содержит либо 1, либо 2, которые определены константами
    mode: int
    #player - объект игрока
    def __init__(self) -> None:
        """принимает объект игрока и уровень сложности, создает первого соперника"""
        self.__player = Player()
        self.mode = int(input("Выберите уровень сложности игры(1 или 2): "))
        self.enemy = Enemy(level=1, mode=self.mode)

    def create_enemy(self) -> None:
        """метод для создания нового соперника"""
        self.enemy = Enemy(level=self.enemy.level + 1, mode=self.mode)
        print(f"У Вашего нового соперника {self.enemy.level} уровень и {self.enemy.lives} жизни")

    def fight(self) -> None:
        """метод запрашивает у пользователя и соперника атаки, из констант получает результат боя (-1, 0, 1)"""
        my_attack = self.__player.select_attack()
        enemy_attack = self.enemy.select_attack()
        result = settings.ATTACK_PAIRS_OUTCOME[(my_attack, enemy_attack)]
        return result

    def handle_fight_result(self, result: str) -> None:
        """принимает результат боя, и в зависимости от результата отнимает жизни либо у игрока, либо у соперника"""
        if result == 1:
            try:
                self.enemy.decrease_lives()
                self.__player.add_score(settings.POINTS_FOR_FIGHT)
            except exceptions.EnemyDown:
                self.__player.add_score(settings.POINTS_FOR_KILLING)
                print("Жизни соперника закончились")
                raise
        elif result == -1:
            self.__player.decrease_lives()
        else:
            print("Ничья, повторите бой")


    def play(self):
        """метод запуска игры. Запускает бесконечный цикл в одной итерации которого происходит "бой".
        Для этого вызывает два метода, fight и handle_fight_result. Отслеживает не произошло ли одно из исключений
        при вызове второго метода GameOver или EnemyDown, при первом завершает игру и вызывает метод для записи очков,
        при втором создает нового, более сильного соперника"""
        while True:
            try:
                result = self.fight()
                self.handle_fight_result(result=result)
            except exceptions.EnemyDown:
                self.__player.add_score(settings.POINTS_FOR_KILLING)
                self.create_enemy()
            except exceptions.GameOver:
                print("You lost the game")
                self.save_score()
                break





    def save_score(self):
        """ вызывает сохранение очков при помощи вызова класса из файла score.py"""
        score_handler = ScoreHandler("result.txt")
        score_handler.read("result.txt")
        try:
            score_handler.save(self.__player, self.mode)
        except ValueError as e:
            print(f"ValueError при сохранении очков: {e}")

        # print(f"игрок {self.player.name} с уровнем {self.mode}")

def play_game():
    """вызывается если игрок выбрал начать игру, в этой функции будет запущен процесс создания игрока,
    создание объекта игры и запуск самой игры"""
    # player, mode = create_player()
    game = Game()
    game.play()

def main():
    while True:
        for item in settings.menu:
            print(f"• {item}")
        user_input = input("Пожалуйста, выберите один из трёх пунктов: ")
        try:
            match user_input:
                case "1":
                    play_game()


                case "2":
                    show_scores()
                    """показать очки, используя класс ScoreHandler"""



                case "3":
                    break
                case _:
                    print("Выбор неверный! Попробуйте снова")
        except ValueError:
            print("Ошибка! Вы должны выбрать только 1,2 или 3")
            continue



def show_scores():
    score_handler = ScoreHandler("result.txt")
    score_handler.read("result.txt")
    score_handler.display()

