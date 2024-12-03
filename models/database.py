import sqlite3

def database_connection():
    return sqlite3.connect('data/database.db')

def get_muscles():
    database = database_connection()
    cursor = database.cursor()
    cursor.execute("SELECT * FROM muscle_group")
    rows = cursor.fetchall()
    muscles = []
    for row in rows:
        muscles.append(row[1].capitalize())
    database.close()
    return muscles




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