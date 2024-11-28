import unittest
from game import settings
from game.score import GameRecord, ScoreHandler, PlayerRecord
from game.models import Player
from game.game_logic import Game



class ScoreHandlerInit(unittest.TestCase):
    def test_score_handler_init(self):
        score_handler = ScoreHandler("result.txt")
        self.assertEqual(score_handler.file_name, "result.txt")

class GameRecordInitTest(unittest.TestCase):
    def test_game_record_init(self):
        game_record = GameRecord()
        self.assertEqual(game_record.records, [])


class ScoreHandlerReadTest(unittest.TestCase):
    def test_score_handler_read(self):
        score_handler = ScoreHandler(settings.SCORE_FILE)
        self.assertEqual(score_handler.file_name, settings.SCORE_FILE)


    def test_score_handler_read_values(self):
        with open('test_file.txt', "w") as file:
            content = 'test_user Normal 100\n'
            file.write(content)
        score_handler = ScoreHandler('test_file.txt')
        score_handler.read('test_file.txt')
        self.assertEqual(len(score_handler.game_record.records), 1)
        record = score_handler.game_record.records[0]


        self.assertEqual(record.name, "test_user")
        self.assertEqual(record.mode, 1)
        self.assertEqual(record.score, 100)

    def test_score_handler_read_added_values(self):
        with open('test_file.txt', "w") as file:
            content = 'test_user Normal 100\n'
            file.write(content)

        score_handler = ScoreHandler('test_file.txt')
        score_handler.read('test_file.txt')

        class MockPlayer:
            name = 'some_test_name'
            score = 50
        mockplayer = MockPlayer()
        score_handler.read('test_file.txt', player=mockplayer, player_mode = 2)
        self.assertEqual(len(score_handler.game_record.records), 2)
        record1 = score_handler.game_record.records[0]
        record2 = score_handler.game_record.records[1]

        self.assertEqual(record1.name, "test_user")
        self.assertEqual(record1.mode, 1)
        self.assertEqual(record1.score, 100)

        self.assertEqual(record2.name, "some_test_name")
        self.assertEqual(record2.mode, 2)
        self.assertEqual(record2.score, 50)

class ScoreHandlerSaveTest(unittest.TestCase):
    def test_score_handler_save(self):
        with open('test_file.txt', "w") as file:
            file.truncate(0)
        score_handler = ScoreHandler('test_file.txt')
        class MockPlayer:
            name = 'some_test_name'
            score = 50
        mockplayer = MockPlayer()
        score_handler.read('test_file.txt', player=mockplayer, player_mode = 2)
        score_handler.save('test_file.txt')
        with open('test_file.txt', "r") as file:
            lines = file.readlines()

        self.assertEqual(len(lines), 1)
        name, mode_str, score = lines[0].strip().split(" ")
        self.assertEqual(name, mockplayer.name)
        self.assertEqual(mode_str, 'Hard')
        self.assertEqual(int(score), 50)









if __name__ == '__main__':
    unittest.main()
