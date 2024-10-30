MODE_NORMAL = 'Normal'
MODE_HARD = 'Hard'
MODES = {'1': MODE_NORMAL,
         '2': MODE_HARD}

PLAYER_LIVES = 2
POINTS_FOR_FIGHT = 1
POINTS_FOR_KILLING = 5
MAX_RECORDS_NUMBER = 5
HARD_MODE_MULTIPLIER = 2

SCORE_FILE = 'scores.txt'

PAPER = 'Paper'
STONE = 'Stone'
SCISSORS = 'Scissors'

WIN = 1
DRAW = 0
LOSE = -1

ALLOWED_ATTACKS = {
    '1': PAPER,
    '2': STONE,
    '3': SCISSORS
}

ATTACK_PAIRS_OUTCOME = {
    (PAPER, PAPER): DRAW,
    (PAPER, STONE): WIN,
    (PAPER, SCISSORS): LOSE,
    (STONE, PAPER): LOSE,
    (STONE, STONE): DRAW,
    (STONE, SCISSORS): WIN,
    (SCISSORS, PAPER): WIN,
    (SCISSORS, STONE): LOSE,
    (SCISSORS, SCISSORS): DRAW
}

menu = [
    "1 - Запуск игры",
    "2 - Посмотреть очки",
    "3 - Выйти из игры"
]