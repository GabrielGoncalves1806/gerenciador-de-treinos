# import sqlite3

# data_base = sqlite3.connect("empresa.db")
# cursor = data_base.cursor()

# # cursor.execute("""
# #     CREATE TABLE IF NOT EXISTS funcionarios (
# #         id INTEGER PRIMARY KEY,
# #         nome TEXT,
# #         cargo TEXT,
# #         salario REAL
# #     )
# # """)

# #cursor.execute("ALTER TABLE funcionarios ADD COLUMN departamento_id INTEGER")

# # cursor.execute("""
# #         CREATE TABLE IF NOT EXISTS departamentos (
# #         id INTEGER PRIMARY KEY,
# #         nome TEXT,
# #         local TEXT          
# #     )
# # """)

# def add_departamento(nome,local):
#     cursor.execute("INSERT INTO departamentos (nome, local) VALUES (?,?)",(nome,local))
#     data_base.commit()

# def add_funcionario(nome,cargo, salario):
#     cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES (?,?,?)",(nome,cargo,salario))
#     data_base.commit()

# def listar_funcionarios():
#     cursor.execute("""
#         SELECT funcionarios.nome, funcionarios.cargo, funcionarios.salario, departamentos.nome AS departamento
#         FROM funcionarios
#         LEFT JOIN departamentos ON funcionarios.departamento_id = departamentos.id
#     """)
#     rows = cursor.fetchall()
#     for row in rows:
#         print(row)
    

# def atualizar_salario(nome,salario):
#     cursor.execute("UPDATE funcionarios SET salario = ? WHERE nome = ?",(salario,nome))
#     data_base.commit()

# def deletar_funcionario(name):
#     cursor.execute("DELETE FROM funcionarios WHERE nome = ?",(name,))
#     data_base.commit()

# def pesquisar_por_cargo(cargo):
#     cursor.execute("SELECT * FROM funcionarios WHERE cargo = ?",(cargo,))
#     rows = cursor.fetchall()
#     for row in rows:
#         print(row)

# def media_salario():
#     media = []
#     cursor.execute("SELECT salario FROM funcionarios")
#     salarios = cursor.fetchall()
#     if salarios:
#         total_salario = sum(salario[0] for salario in salarios)
#         media = total_salario / len(salarios)
#         print(f"Média salarial: {media:.2f}")
#     else:
#         print("Nenhum funcionário cadastrado.")

# def alterar_departamento(funcionario, departamento):
#     cursor.execute("SELECT id FROM departamentos WHERE nome = ?",(departamento,))
#     departamento_data = cursor.fetchone()
#     print(departamento_data)
#     if departamento_data:
#         departamento_id = departamento_data[0]
#         cursor.execute("UPDATE funcionarios SET departamento_id = ? WHERE nome = ?",(departamento_id,funcionario))
#         data_base.commit()
#     else:
#         print(f"Departamento {departamento} não encontrado.")


# # add_funcionario("João", "Gerente", 5000.00)

# alterar_departamento("Carlos","administrativo")
# # alterar_departamento("Maria","recursos humanos")
# listar_funcionarios() 

# # add_departamento("administrativo","local")
# # add_departamento("recursos humanos","filial")

# data_base.close()

import sqlite3
import hashlib

def criptografia(senha):
    senha_bytes = senha.encode("utf-8")
    senha_hash = hashlib.sha256(senha_bytes)
    return senha_hash.hexdigest()


def database_connection():
    database = sqlite3.connect("data/database.db")
    cursor = database.cursor()
    return database, cursor
        
def get_professor(email):
        database, cursor = database_connection()
        cursor.execute("SELECT id, nome FROM professores WHERE email = ?",(email,))
        professor = cursor.fetchone()
        return professor
    
def add_professor():
    database, cursor = database_connection()
    cursor.execute("INSERT INTO professores (username, email, senha, nome) VALUES (?,?,?,?)",("admin","admin@","123456","Gabriel admin"))
    database.commit()
    

def add_aluno(username,nome,email,senha,id_professor):
    senha_cripto = criptografia(senha)

    database, cursor = database_connection()
    cursor.execute("INSERT INTO alunos (username, nome, email, senha, id_professor) VALUES (?,?,?,?,?)",(username,nome,email,senha_cripto,id_professor))
    database.commit()
    
#add_aluno("jorge","jorge jorginho","jorge@gmail.com","8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92",2)