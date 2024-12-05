import hashlib
from models.database_control import database_connection

# Função que valida o login com os dados fornecidos no formulario
# e verifica se correspondem com o banco de dados

def criptografia(senha):
    senha_bytes = senha.encode("utf-8")
    senha_hash = hashlib.sha256(senha_bytes)
    return senha_hash.hexdigest()



def validar_login(dados):
    database, cursor = database_connection()

    if dados["tipo_usuario"] == "professor":
        cursor.execute("SELECT senha FROM professores WHERE username = ?",(dados["username"],))
    elif dados["tipo_usuario"] == "aluno":
        cursor.execute("SELECT senha FROM alunos WHERE username = ?",(dados["username"],))
    senha_db = cursor.fetchone()
    try:
        if senha_db[0] == criptografia(dados["password"]):
            return True
        else:
            return False
    except Exception as e:
        return False