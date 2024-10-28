from . import settings
from . import models


# class ScoreHandler:
#     game_record = GameRecord
#     file_name: str
#     def __init__(self, file_name: str) -> None:
#         with open(file_name, "r") as file:
#             content = file.read()
#             print(content)
#
#доделать


class ScoreHandler:
    """класс для обработки очков"""
    def __init__(self, file_name) -> None:
        """принимает только имя файла и сохраняет его. Вызывает метод для чтения файла"""
        #объект класса GameRecord, туда мы будем считывать сохраненные очки и записывать таблицу с новыми
        self.game_record = GameRecord()
        self.file_name = file_name
        # with open(file_name, "r") as file:
        #     content = file.read()
        #     print(content)

    def read(self, file_name):
        """метод, который будет читать файл и каждую его строку сохранять в PlayerRecord, которые будут сохранятся в GameRecord"""
        with open(file_name, "r") as file:
            for line in file:
                """вернуться и доделать чтение и сохранение из файла в PlayerRecord"""
                name, mode, score = line.strip().split(" ")
                # score = line.strip().split(" ")[-1]
                # print(f"имя {name}, уровень {mode}, очки {score}")
                play_record = PlayerRecord(name, mode, int(score))
                # print(f"{play_record}")
                self.game_record.add_record(play_record.name, play_record.mode, play_record.score)
                print(self.game_record)

    def save(self, player: models.Player, mode: int, file_name = "result.txt"):
        """метод, который нужен, что бы записать новые результаты в файл (предварительно отсортировать и обрезать, если нужно)"""
        with open(file_name, "a") as file:
            content = f"\n{player.name} {settings.MODES[str(mode)]} {player.score}"
            file.write(content)
            print(content)

    def display(self, file_name: str):
        """метод для отображения очков"""
        pass


class PlayerRecord:
    """класс для хранения записи об одном игроке"""
    name: str
    mode: int
    score: int
    def __init__(self, name: str, mode: int, score: int) -> None:
        """для создания объекта принимает все три параметра"""
        self.name = name
        self.mode = mode
        self.score = score
        # GameRecord.game_record.add_record(self.name, self.mode, self.score)
        # print(f"Checking PlayRecord{name}{mode}{score}")
    def __gt__(self, other) -> bool:
        """для того что бы можно было отсортировать записи по очкам"""
        return self.score > other.score
        # позже вернуться и пересмотреть цель сортировки

    def __str__(self):
        """для удобного вывода данных"""
        return f"Игрок {self.name} с уровнем сложности {self.mode} набрал {self.score} очков"



class GameRecord:
    """класс содержащий записи об игроках"""
    def __init__(self) -> None:
        """создает объект с пустым списком объектов типа PlayerRecord"""
        self.records: list[PlayerRecord] = []

    def __eq__(self, other) -> bool:
        """меджик метод для поиска через in ????????"""
        return self.name, self.mode == other.name, other.mode

    def add_record(self, name, mode, score) -> None:
        """метод для добавления записи об одном игроке, перезаписывает результат, если находит того же самого игрока по имени и уровню сложности"""
        # self.records.append({(name, mode): score})
        play_record = PlayerRecord(name, mode, score)
        for record in self.records:
            if play_record == record:
                if play_record > record:
                    del self.records[record]
                    self.records.append(play_record)
            else:
                self.records.append(play_record)
        # print(f"Добавление записи: {play_record}")  # Проверка добавления записи
        for record in self.records:
            print(record)



    def __str__(self) -> str:
        return "\n".join(str(record) for record in self.records)







# Alex = PlayerRecord("Alex", 1, 30)
# David = PlayerRecord("David", 2, 12)
# Alex = PlayerRecord("Alex", 2, 45)

# game_record = GameRecord()
# game_record.add_record(Alex)
# game_record.add_record(David)

# score_handler = ScoreHandler("result.txt")
# print(game_record)
