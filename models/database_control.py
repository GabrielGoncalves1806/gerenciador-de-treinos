import sqlite3

def database_connection():
    database = sqlite3.connect("data/database.db")
    cursor = database.cursor()
    return database, cursor

def get_muscles():
    database, cursor = database_connection()
    cursor.execute("SELECT * FROM grupos_musculares")
    rows = cursor.fetchall()
    muscles = []
    for row in rows:
        muscles.append(row[1])
    database.close()
    return muscles

def get_sprite_path(grupo_muscular):
    database, cursor = database_connection()
    cursor.execute("SELECT sprite_path FROM grupos_musculares WHERE nome = ?",(grupo_muscular.lower(),))
    sprite = cursor.fetchone()
    sprite_path = sprite[0]
    return sprite_path

def get_grupo_muscular(id_grupo_muscular):
    database, cursor = database_connection()
    cursor.execute("SELECT nome FROM grupos_musculares WHERE id = ?",(id_grupo_muscular,))
    nome = cursor.fetchone()
    return nome[0]

def add_exercicio(nome_exercicio,grupo_muscular):
    database, cursor = database_connection()
    try:
        cursor.execute("SELECT id FROM grupos_musculares WHERE nome = ?",(grupo_muscular,))
        id_grupo_muscular = cursor.fetchone()
        cursor.execute("INSERT INTO exercicios (nome, id_grupo_muscular) VALUES (?,?)",(nome_exercicio,id_grupo_muscular[0]))
        database.commit()
        print(nome_exercicio,grupo_muscular)
        return True
    except Exception as e:
        return False
    
def get_exercicios(grupo_muscular):
    database, cursor = database_connection()
    cursor.execute("SELECT id FROM grupos_musculares WHERE nome = ?",(grupo_muscular,))
    id_grupo = cursor.fetchone()
    cursor.execute("SELECT nome FROM exercicios WHERE id_grupo_muscular = ?",(id_grupo[0],))
    exercicios = cursor.fetchall()
    return exercicios

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

def add_professor():
    database, cursor = database_connection()
    cursor.execute("INSERT INTO professores (username, email, senha, nome) VALUES (?,?,?,?)",("gab","teste@gmail.com","123456"))
    database.commit()

def add_aluno():
    database, cursor = database_connection()
    cursor.execute("INSERT INTO alunos (username, nome, email, senha) VALUES (?,?,?,?)",("joao","joao eudes","teste@gmail.com","123456"))
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
#     for muscle in musculos["grupos_musculares"]:
#         cursor.execute("INSERT INTO muscle_group (nome) VALUES (?)",(muscle.lower(),))
#         data_base.commit()

# cursor.execute("""
#                CREATE TABLE IF NOT EXISTS muscle_group (
#                id INTEGER PRIMARY KEY,
#                nome TEXT
#                )"""
#         )