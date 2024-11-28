import psycopg2
from psycopg2.errors import UniqueViolation

username = input("Enter username: ")
try:
    with psycopg2.connect(
            dbname="module_2",
            user="player",
            password="mypass"
    ) as conn:
        with conn.cursor() as cur:
            cur.execute("insert into player (name) values (%s);", (username,))
            print("Данные успешно добавлены.")
except UniqueViolation:
    print("User already exist")
