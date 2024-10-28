import settings
import models


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
                # line = PlayerRecord()
                print(line)

    def save(self, file_name, player: models.Player):
        """метод, который нужен, что бы записать новые результаты в файл (предварительно отсортировать и обрезать, если нужно)"""
        with open(file_name, "w") as file:
            content = file.write(str(player))
            print(player)
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
        return (self.name, self.mode) == (other.name, other.mode)

    def add_record(self, player: PlayerRecord) -> None:
        """метод для добавления записи об одном игроке, перезаписывает результат, если находит того же самого игрока по имени и уровню сложности"""
        if player in self.records:
            for i in self.records:
                if PlayerRecord.__gt__(player, self.records[i]):
                    self.records[i] = player.score
        else:
            self.records.append(player)



    def __str__(self) -> str:
        return "\n".join(str(record) for record in self.records)







# Alex = PlayerRecord("Alex", 1, 30)
# David = PlayerRecord("David", 2, 12)
# Alex = PlayerRecord("Alex", 2, 45)

game_record = GameRecord()
# game_record.add_record(Alex)
# game_record.add_record(David)

score_handler = ScoreHandler("result.txt")
print(game_record)
