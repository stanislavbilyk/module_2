import unittest
from unittest.mock import patch
from game.models import Player
from game import settings
from game.exceptions import ValidationName, ValidationLives, IncorrectAttackError


class PlayerTest(unittest.TestCase):
    def test_player_initialization(self):
        player = Player(name = "TestName")
        self.assertEqual(player.lives, settings.PLAYER_LIVES)
        self.assertEqual(player.score, 0)

    def test_score_player_1(self):
        player = Player(name="TestName")
        self.assertEqual(player.lives, settings.PLAYER_LIVES - 1)
        self.assertEqual(player.score, 1)

    def test_negativ_score_player_(self):
        player = Player(name="TestName")
        with self.assertRaises(ValidationLives):
            player.lives = -1

    def test_string_score_player_(self):
        player = Player(name="TestName")
        with self.assertRaises(ValueError):
            player.score = "abc"

    def test_string_lives_player_(self):
        player = Player(name="TestName")
        with self.assertRaises(ValueError):
            player.lives = "abc"

    def test_name_player_space(self):
        with self.assertRaises(ValidationName):
            Player(name=" ")

    def test_name_player_null(self):
        with self.assertRaises(ValidationName):
            Player(name="")


class SelectAttackTest(unittest.TestCase):
    @patch('builtins.input', return_value="1")
    def test_select_attack_1(self, mock_input):
        player = Player()
        attack = player.select_attack()
        self.assertEqual(attack, settings.ALLOWED_ATTACKS["1"])

    @patch('builtins.input', return_value="2")
    def test_select_attack_2(self, mock_input):
        player = Player()
        attack = player.select_attack()
        self.assertEqual(attack, settings.ALLOWED_ATTACKS["2"])

    @patch('builtins.input', return_value="3")
    def test_select_attack_3(self, mock_input):
        player = Player()
        attack = player.select_attack()
        self.assertEqual(attack, settings.ALLOWED_ATTACKS["3"])

    @patch('builtins.input', side_effect=["4", "abc", "2"])
    def test_select_attack_wrong(self, mock_input):
        player = Player()
        attack = player.select_attack()
        self.assertEqual(attack, settings.ALLOWED_ATTACKS["2"])

    @patch('builtins.input', return_value="5")
    def test_select_attack_5(self, mock_input):
        player = Player()
        with self.assertRaises(IncorrectAttackError):
            player.select_attack()

    @patch('builtins.input', return_value="two")
    def test_select_attack_string(self, mock_input):
        player = Player()
        with self.assertRaises(ValueError):
            player.select_attack()




if __name__ == '__main__':
    unittest.main()
