from . import settings
from . import models


class ScoreHandler:
    """класс для обработки очков"""
    def __init__(self, file_name) -> None:
        """принимает только имя файла и сохраняет его. Вызывает метод для чтения файла"""
        #объект класса GameRecord, туда мы будем считывать сохраненные очки и записывать таблицу с новыми
        self.game_record = GameRecord()
        self.file_name = file_name


    def read(self, file_name = settings.SCORE_FILE, player: models.Player = None, player_mode: int = None):
        """метод, который будет читать файл и каждую его строку сохранять в PlayerRecord, которые будут сохранятся в GameRecord"""
        with open(file_name, "r") as file:
            for line in file:
                """вернуться и доделать чтение и сохранение из файла в PlayerRecord"""
                # name, mode, score = line.strip().split(" ")
                name, mode_str, score = line.strip().split(" ")

                # Преобразуем строку 'Normal' или 'Hard' в числовой ключ
                mode_key = [key for key, value in settings.MODES.items() if value == mode_str]

                if mode_key:
                    mode = int(mode_key[0])
                self.game_record.add_record(name, mode, int(score))
                self.game_record.prepare_records()
            if player and player_mode is not None:
                self.game_record.add_record(player.name, player_mode, int(player.score))
                self.game_record.prepare_records()

    def save(self, file_name = "result.txt"):
        """метод, который нужен, что бы записать новые результаты в файл (предварительно отсортировать и обрезать, если нужно)"""
        with open(file_name, "w") as file:
            for record in self.game_record.records:
                content = f"{record.name} {settings.MODES[str(record.mode)]} {record.score}\n"
                file.write(content)


    def display(self):
        """метод для отображения очков"""
        print(f"{'Name':<10} {'Mode':<10} {'Score':<5}")
        print("=" * 25)
        for record in self.game_record.records:
            print(f"{record.name:<10} {record.mode:<10} {record.score:<5}")



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


    def __eq__(self, other) -> bool:
        """меджик метод для поиска через in ????????"""
        return (self.name, self.mode) == (other.name, other.mode)

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



    def add_record(self, name, mode, score) -> None:
        """метод для добавления записи об одном игроке, перезаписывает результат,
        если находит того же самого игрока по имени и уровню сложности"""
        play_record = PlayerRecord(name, mode, score)
        record_found = False
        for index, record in enumerate(self.records):
            if play_record == record:
                record_found = True
                if play_record > record:
                    self.records[index] = play_record
        if not record_found:
            self.records.append(play_record)


    def prepare_records(self):
        """метод для сортировки существующих результатов и обрезки до
        максимального кол-ва указанного в настройках"""
        self.records.sort(key=lambda record: record.score, reverse=True)
        self.records = self.records[:settings.MAX_RECORDS_NUMBER]

    def __str__(self) -> str:
        return "\n".join(str(record) for record in self.records)







