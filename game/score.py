from . import settings
from . import models
import psycopg2
from psycopg2.errors import UniqueViolation


class ScoreHandler:
    """класс для обработки очков"""
    # def __init__(self) -> None:
    #     """принимает только имя файла и сохраняет его. Вызывает метод для чтения файла"""
        #объект класса GameRecord, туда мы будем считывать сохраненные очки и записывать таблицу с новыми
        # self.game_record = GameRecord()
        # self.file_name = file_name


    # def read(self, file_name = settings.SCORE_FILE, player: models.Player = None, player_mode: int = None):
    #     """метод, который будет читать файл и каждую его строку сохранять в PlayerRecord, которые будут сохранятся
    #      в GameRecord"""
    #     with open(file_name, "r") as file:
    #         for line in file:
    #             """вернуться и доделать чтение и сохранение из файла в PlayerRecord"""
    #             # name, mode, score = line.strip().split(" ")
    #             name, mode_str, score = line.strip().split(" ")

#                 # Преобразуем строку 'Normal' или 'Hard' в числовой ключ
#                 mode_key = [key for key, value in settings.MODES.items() if value == mode_str]

#                 if mode_key:
#                     mode = int(mode_key[0])
#                 self.game_record.add_record(name, mode, int(score))
#                 self.game_record.prepare_records()
#             if player and player_mode is not None:
#                 self.game_record.add_record(player.name, player_mode, int(player.score))
#                 self.game_record.prepare_records()

    def save(self, player: models.Player, player_mode: int):
        """метод, который нужен, что бы записать новые результаты в файл (предварительно отсортировать и обрезать, если нужно)"""
        try:
            with psycopg2.connect(
                dbname="module_2",
                user="player",
                password="mypass"
            ) as conn:
                with conn.cursor() as cur:
                    cur.execute("insert into score (player, mode, score) values (%s, %s, %s);", (player.name, settings.MODES[str(player_mode)], player.score))
                    print("Новый игрок сохранён")
        except UniqueViolation:
            print("Игрок с таким именем и режимом уже существует. Проверяем, нужно ли обновить результат...")
            with psycopg2.connect(
                dbname="module_2",
                user="player",
                password="mypass"
            ) as conn:
                with conn.cursor() as cur:
                    cur.execute(
                    "SELECT score FROM score WHERE player = %s AND mode = %s;",
                    (player.name, settings.MODES[str(player_mode)])
                )
                    existing_score = cur.fetchone()[0]
                    if player.score > existing_score:
                        cur.execute(
                        "UPDATE score SET score = %s WHERE player = %s AND mode = %s;",
                        (player.score, player.name, settings.MODES[str(player_mode)])
                    )
                        print("Результат обновлён")
                    else:
                        print("Новый результат не выше текущего. Обновление не требуется.")



    def display(self):
        """метод для отображения очков"""
        with psycopg2.connect(
            dbname="module_2",
            user="player",
            password="mypass"
        ) as conn:
            with conn.cursor() as cur:
                cur.execute("select player, mode, score from score order by score desc limit 5;")
                res = cur.fetchall()
                print(f"{'Name':<15} {'Mode':<15} {'Score':<5}")
                print("=" * 40)
                for i in res:
                    name, mode, score = i
                    print(f"{name:<15} {mode:<15} {score:<5}")
        # print(f"{'Name':<10} {'Mode':<10} {'Score':<5}")
        # print("=" * 25)
        # for record in self.game_record.records:
        #     print(f"{record.name:<10} {record.mode:<10} {record.score:<5}")



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







