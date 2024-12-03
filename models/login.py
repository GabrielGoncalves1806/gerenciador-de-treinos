from models.database_control import database_connection

def validar_login(tabela,username,senha):
    print("iniciando validação")
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