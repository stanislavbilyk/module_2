from . import settings
from game import exceptions
from .models import Player, Enemy
# import score
# from module_2 import main


class Game:
    #объект соперника, при убийстве будет создан новый, с более высоким уровнем
    # player: Player
    # enemy: Enemy
    #уровень сложности, normal или hard, содержит либо 1, либо 2, которые определены константами
    mode: int
    #player - объект игрока
    def __init__(self, player: Player, mode: int) -> None:
        """принимает объект игрока и уровень сложности, создает первого соперника"""
        self.__player = player
        self.enemy = Enemy(level=1, mode=mode)
        self.mode = mode

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
                points = self.enemy.decrease_lives()
                self.__player.add_score(points)
            except exceptions.EnemyDown:
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
        from .score import ScoreHandler
        score_handler = ScoreHandler("result.txt")
        score_handler.read("result.txt")
        score_handler.save(self.__player, self.mode)
        # print(f"игрок {self.player.name} с уровнем {self.mode}")







