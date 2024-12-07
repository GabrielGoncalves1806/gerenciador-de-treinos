
from models.database_control import database_connection
from models import criptografia_senha

# Função que valida o login com os dados fornecidos no formulario
# e verifica se correspondem com o banco de dados

def validar_login(dados):
    database, cursor = database_connection()

    if dados["tipo_usuario"] == "professor":
        cursor.execute("SELECT senha FROM professores WHERE username = ?",(dados["username"],))
    elif dados["tipo_usuario"] == "aluno":
        cursor.execute("SELECT senha FROM alunos WHERE username = ?",(dados["username"],))
    senha_db = cursor.fetchone()
    try:
        if senha_db[0] == criptografia_senha.criptografia(dados["password"]):
            return True
        else:
            return False
    except Exception as e:
        return False