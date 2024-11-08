import unittest
from game.models import Enemy
from game import settings
from unittest.mock import patch


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



if __name__ == '__main__':
    unittest.main()
