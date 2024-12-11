import flet as ft

class DialogAddAluno():
    def __init__(self,nome,email):
        self.nome = nome
        self.email = email
        pass
        
    def salvar(self):
        pass

    def get_controls(self):
        return ft.AlertDialog(
            title=ft.Text("Editar"),
            content=ft.Column(
                [
                    # ft.TextField(value=sellabel="Usuário",tooltip="Nome que o alunos vai usar para logar"),
                    ft.TextField(value=self.nome,label="Nome do Aluno",tooltip="Nome completo do aluno"),
                    ft.TextField(value=self.email,label="E-mail"),
                ]
            ),
            actions=[
                ft.TextButton("Cancelar"),
                ft.TextButton("Salvar")
            ],
        )