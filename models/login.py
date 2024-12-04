from models.database_control import database_connection

# Função que valida o login com os dados fornecidos no formulario
# e verifica se correspondem com o banco de dados

def validar_login(tabela,username,senha):
    database, cursor = database_connection()

    if tabela == "professor":
        cursor.execute("SELECT senha FROM professores WHERE username = ?",(username,))
    elif tabela == "aluno":
        cursor.execute("SELECT senha FROM alunos WHERE username = ?",(username,))
    senha_db = cursor.fetchone()
    try:
        if senha_db[0] == senha:
            return True
        else:
            return False
    except Exception as e:
        return False