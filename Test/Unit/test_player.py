import unittest
from unittest.mock import patch
from game.game_logic import Game
from game.models import Player, Enemy
from game import settings
from game.exceptions import ValidationName, ValidationLives, IncorrectAttackError, GameOver


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

class PlayerAddScore(unittest.TestCase):
    def test_add_score_for_fight_normal(self):
        game = Game()
        player = game._Game__player
        game.mode = 1
        initial_score = player.score
        points = settings.POINTS_FOR_FIGHT
        player.add_score(points, game.mode)
        expected_score = initial_score + points
        self.assertEqual(player.score, expected_score)

    def test_add_score_for_fight_hard(self):
        game = Game()
        player = game._Game__player
        game.mode = 2
        initial_score = player.score
        points = settings.POINTS_FOR_FIGHT
        player.add_score(points, game.mode)
        expected_score = initial_score + points * settings.HARD_MODE_MULTIPLIER
        self.assertEqual(player.score, expected_score)

    def test_add_score_for_killing_normal(self):
        game = Game()
        player = game._Game__player
        game.mode = 1
        initial_score = player.score
        points = settings.POINTS_FOR_KILLING
        player.add_score(points, game.mode)
        expected_score = initial_score + points
        self.assertEqual(player.score, expected_score)

    def test_add_score_for_killing_hard(self):
        game = Game()
        player = game._Game__player
        game.mode = 2
        initial_score = player.score
        points = settings.POINTS_FOR_KILLING
        player.add_score(points, game.mode)
        expected_score = initial_score + points * settings.HARD_MODE_MULTIPLIER
        self.assertEqual(player.score, expected_score)


class PlayerDecreaseLives(unittest.TestCase):
    def test_decrease_lives(self):
        player = Player()
        initial_lives = player.lives
        player.decrease_lives()
        self.assertEqual(player.lives, initial_lives - 1)

    def test_player_check_lives(self):
        player = Player()
        player.lives = 1
        with self.assertRaises(GameOver):
            player.decrease_lives()

if __name__ == '__main__':
    unittest.main()
