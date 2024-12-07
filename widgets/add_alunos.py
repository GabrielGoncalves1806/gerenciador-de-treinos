import flet as ft

class DialogAddAluno():
    def __init__(self):
        pass
        
    def salvar(self):
        pass

    def get_controls(self):
        return ft.AlertDialog(
            title=ft.Text("Editar"),
            content=ft.Column(
                [
                    ft.TextField(label="Nome do Aluno"),
                    ft.TextField(label="Email"),
                ]
            ),
            actions=[
                ft.TextButton("Cancelar"),
                ft.TextButton("Salvar")
            ],
        )