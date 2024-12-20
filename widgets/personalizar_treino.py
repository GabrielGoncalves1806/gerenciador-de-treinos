import flet as ft
from models import database_control
from controllers import route_control

class PersonalizarTreinoAluno():
    def __init__(self,data):
        self.data = data
        
        #self.aluno = database_control.get_aluno(data["id"])
        pass
        
    def salvar(self):
        pass

    def get_controls(self):
        return ft.AlertDialog(
            title=ft.Text("Editar"),
            content=ft.Column(
                [
                    # ft.TextField(value=sellabel="Usuário",tooltip="Nome que o alunos vai usar para logar"),
                    ft.TextField(value=self.data["id"],label="Nome do Aluno",tooltip="Nome completo do aluno"),
                    ft.TextField(label="E-mail"),
                ]
            ),
            actions=[
                ft.TextButton("Cancelar"),
                ft.TextButton("Salvar")
            ],
        )