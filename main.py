from game import settings
from game import exceptions
from game import models
from game import game_logic

menu = [
    "1 - Запуск игры",
    "2 - Посмотреть очки",
    "3 - Выйти из игры"
]


def play_game():
    """вызывается если игрок выбрал начать игру, в этой функции будет запущен процесс создания игрока,
    создание объекта игры и запуск самой игры"""


    def create_player():
        """спросить игрока имя и сложность, создать объект игрока с указанным именем,
        и передать объект игрока и сложность в класс игры"""
        name = input("Введите имя игрока: ")
        mode = int(input("Выберите уровень сложности игры(1 или 2): "))
        # player = models.Player(name)
        game = game_logic.Game(name=name, mode=mode)
        game.play()
    create_player()

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





