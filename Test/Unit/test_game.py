import unittest
from game.game_logic import Game
from game.exceptions import ValidationMode, ValidationFight
from game.models import Player, Enemy
from unittest.mock import patch
from game import settings


class GameTest(unittest.TestCase):
    def test_mode_one(self):
        game = Game(mode = 1)
        self.assertIn(game.mode, (1, 2))

    def test_mode_two(self):
        game = Game(mode=2)
        self.assertIn(game.mode, (1, 2))

    def test_mode_wrong(self):
        # Проверка для значения больше 2
        with self.assertRaises(ValidationMode):
            Game(mode=3)

        # Проверка для отрицательного значения
        with self.assertRaises(ValidationMode):
            Game(mode=-1)

        # Проверка для строки
        with self.assertRaises(ValidationMode):
            Game(mode="abc")


class FightTest(unittest.TestCase):
    @patch("random.randint", return_value=1)
    def test_fight_result_1_1(self, mock_randint):
        my_attack = "PAPER"
        enemy = Enemy(level = 1, mode = 1)
        random_attack = enemy.select_attack()
        self.assertEqual(my_attack, random_attack)

    @patch("random.randint", return_value=2)
    def test_fight_result_1_2(self, mock_randint):
        my_attack = "PAPER"
        enemy = Enemy(level=1, mode=1)
        random_attack = enemy.select_attack()
        self.assertEqual(my_attack, random_attack)

    @patch("random.randint", return_value=3)
    def test_fight_result_1_3(self, mock_randint):
        my_attack = "PAPER"
        enemy = Enemy(level=1, mode=1)
        random_attack = enemy.select_attack()
        self.assertEqual(my_attack, random_attack)

    @patch("random.randint", return_value=1)
    def test_fight_result_2_1(self, mock_randint):
        my_attack = "STONE"
        enemy = Enemy(level=1, mode=1)
        random_attack = enemy.select_attack()
        self.assertEqual(my_attack, random_attack)

    @patch("random.randint", return_value=2)
    def test_fight_result_2_2(self, mock_randint):
        my_attack = "STONE"
        enemy = Enemy(level=1, mode=1)
        random_attack = enemy.select_attack()
        self.assertEqual(my_attack, random_attack)

    @patch("random.randint", return_value=3)
    def test_fight_result_2_3(self, mock_randint):
        my_attack = "STONE"
        enemy = Enemy(level=1, mode=1)
        random_attack = enemy.select_attack()
        self.assertEqual(my_attack, random_attack)

    @patch("random.randint", return_value=1)
    def test_fight_result_3_1(self, mock_randint):
        my_attack = "SCISSORS"
        enemy = Enemy(level=1, mode=1)
        random_attack = enemy.select_attack()
        self.assertEqual(my_attack, random_attack)

    @patch("random.randint", return_value=2)
    def test_fight_result_3_2(self, mock_randint):
        my_attack = "SCISSORS"
        enemy = Enemy(level=1, mode=1)
        random_attack = enemy.select_attack()
        self.assertEqual(my_attack, random_attack)

    @patch("random.randint", return_value=3)
    def test_fight_result_3_3(self, mock_randint):
        my_attack = "SCISSORS"
        enemy = Enemy(level=1, mode=1)
        random_attack = enemy.select_attack()
        self.assertEqual(my_attack, random_attack)


class ValidationFight(unittest.TestCase):
    def test_result_1(self):
        result = 1
        self.assertEqual(result, settings.WIN)

    def test_result_minus_1(self):
        result = -1
        self.assertEqual(result, settings.LOSE)

    def test_result_0(self):
        result = 0
        self.assertEqual(result, settings.DRAW)

    def test_result_wrong(self):
        with self.assertRaises(ValidationFight):
            result = 4







if __name__ == '__main__':
    unittest.main()
