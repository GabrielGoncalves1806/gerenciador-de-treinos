import json
import sqlite3

def database_connection():
    database = sqlite3.connect('data/database.db')
    cursor = database.cursor()
    return database, cursor

def get_muscles():
    database, cursor = database_connection()
    cursor.execute("SELECT * FROM muscle_group")
    rows = cursor.fetchall()
    muscles = []
    for row in rows:
        muscles.append(row[1].capitalize())
    database.close()
    return muscles


def get_sprite_path(grupo_muscular):
    database, cursor = database_connection()
    cursor.execute("SELECT sprite_path FROM muscle_group WHERE nome = ?",(grupo_muscular.lower(),))
    sprite = cursor.fetchone()
    sprite_path = sprite[0]
    return sprite_path

################################ funções de teste ################################

def create_table():
    database, cursor = database_connection()
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS fichas_de_treino (
                id INTEGER PRIMARY KEY,
                id_aluno INTEGER,
                id_exercicio INTEGER,
                series INTEGER,
                repeticoes INTEGER,
                carga INTEGER
                )
            """)
    database.commit()

create_table()

def add_professor():
    database, cursor = database_connection()
    cursor.execute("INSERT INTO professores (username,email,senha) VALUES (?,?,?)",("gab","teste@gmail.com","123456"))
    database.commit()

def alterar_tabela():
    database, cursor = database_connection()
    cursor.execute("ALTER TABLE alunos ADD COLUMN nome TEXT")
    database.commit()


# def add_sprite():
#     database = database_connection()
#     cursor = database.cursor()
#     with open("data/sprites.json") as file:
#         sprites = json.load(file)
#         for sprite in sprites:
#             print(sprites[sprite])
#     # cursor.execute("ALTER TABLE muscle_group ADD COLUMN sprite_path TEXT")
#             cursor.execute("UPDATE muscle_group SET sprite_path = ? WHERE nome = ?",(sprites[sprite],sprite,))
#     database.commit()

# add_sprite()


# with open("data/grupos_musculares.json") as file:
#     musculos = json.load(file)
#     for muscle in musculos['grupos_musculares']:
#         cursor.execute("INSERT INTO muscle_group (nome) VALUES (?)",(muscle.lower(),))
#         data_base.commit()

# cursor.execute("""
#                CREATE TABLE IF NOT EXISTS muscle_group (
#                id INTEGER PRIMARY KEY,
#                nome TEXT
#                )"""
#         )