import unittest
from game.models import Enemy
from game import settings
from unittest.mock import patch
from game.exceptions import EnemyDown
from game.game_logic import Game


class EnemyTestCreation(unittest.TestCase):
    def test_enemy_normal(self):
        enemy = Enemy(level = 1, mode = 1)
        self.assertEqual(enemy.lives, 1 * 1)
        self.assertEqual(enemy.level, 1)
        self.assertEqual(settings.MODES['1'], 'Normal')

    def test_enemy_hard(self):
        enemy = Enemy(level = 2, mode = 2)
        self.assertEqual(enemy.lives, 2 * 2)
        self.assertEqual(enemy.level, 2)
        self.assertEqual(settings.MODES['2'], 'Hard')


    def test_mode_string(self):
        with self.assertRaises(ValueError):
            enemy = Enemy(level=2, mode='abc')

class NewEnemyCreation(unittest.TestCase):
    def test_new_enemy_level(self):
        game = Game()
        initial_level = game.enemy.level
        game.create_enemy()
        self.assertEqual(game.enemy.level, initial_level + 1)

    def test_new_enemy_lives(self):
        game = Game()
        initial_lives = game.enemy.lives
        game.create_enemy()
        self.assertEqual(game.enemy.lives, initial_lives + 1)

class EnemyTestSelectAttack(unittest.TestCase):
    @patch("random.randint", return_value = "1")
    def test_enemy_select_attack_1(self, mock_randint):
        enemy = Enemy()
        random_attack = enemy.select_attack()
        self.assertEqual(random_attack, settings.ALLOWED_ATTACKS["1"])

    @patch("random.randint", return_value="2")
    def test_enemy_select_attack_2(self, mock_randint):
        enemy = Enemy()
        random_attack = enemy.select_attack()
        self.assertEqual(random_attack, settings.ALLOWED_ATTACKS["2"])

    @patch("random.randint", return_value="3")
    def test_enemy_select_attack_3(self, mock_randint):
        enemy = Enemy()
        random_attack = enemy.select_attack()
        self.assertEqual(random_attack, settings.ALLOWED_ATTACKS["3"])

class EnemyDecreaseLives(unittest.TestCase):
    def test_decrease_lives(self):
        enemy = Enemy(level = 2, mode = 1)
        initial_lives = enemy.lives
        self.assertEqual(initial_lives, 2)
        enemy.decrease_lives()
        self.assertEqual(enemy.lives, initial_lives - 1)

    def test_enemy_lives(self):
        enemy = Enemy(level=1, mode=1)
        enemy.lives = 1
        with self.assertRaises(EnemyDown):
            enemy.decrease_lives()




if __name__ == '__main__':
    unittest.main()
