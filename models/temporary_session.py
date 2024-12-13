import json
from models import database_control

class LocalSession():
    def __init__(self,email=None,database=None):
        self.email = email
        self.local = database
        
        if self.local == "alunos":
            self.dados = database_control.get_aluno(self.email)
        elif self.local == "professores":
            self.dados = database_control.get_professor(self.email)
            
    def save_local_session(self,status):
        print(self.dados)
        with open("data/local_session.json","w") as data:
            data_session = {
                "id":self.dados[0],
                "nome":self.dados[1],
                "email":self.email,
                "status":status,
                "database":self.local
            }
            json.dump(data_session,data)
            
    def get_session(self):
        with open("data/local_session.json","r") as data: 
            return json.load(data)
            
        