from game import settings
from game import exceptions
from game.models import Player
from game.game_logic import Game

menu = [
    "1 - Запуск игры",
    "2 - Посмотреть очки",
    "3 - Выйти из игры"
]


def play_game():
    """вызывается если игрок выбрал начать игру, в этой функции будет запущен процесс создания игрока,
    создание объекта игры и запуск самой игры"""
    # player, mode = create_player()
    player = Player()
    game = Game(player)
    game.play()


# def create_player():
    """спросить игрока имя и сложность, создать объект игрока с указанным именем,
    и передать объект игрока и сложность в класс игры"""
    # name = input("Введите имя игрока: ")
    # mode = int(input("Выберите уровень сложности игры(1 или 2): "))
    # player = Player(name)
    # return player, mode



def main():
    while True:
        for item in menu:
            print(f"• {item}")
        user_input = input("Пожалуйста, выберите один из трёх пунктов: ")
        try:
            match user_input:
                case "1":
                    play_game()


                case "2":
                    def show_scores():
                        """показать очки, используя класс ScoreHandler"""
                        pass


                case "3":
                    break
                case _:
                    print("Выбор неверный! Попробуйте снова")
        except ValueError:
            print("Ошибка! Вы должны выбрать только 1,2 или 3")
            continue
if __name__ == "__main__":
    main()





