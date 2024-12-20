import flet as ft
from controllers import route_control
from models import database_control

class PersonalizarTreino():
    def __init__(self,page:ft.Page,data):
        self.page = page
        self.data = data
        self.aluno_data = database_control.get_aluno(self.data["id"])
        self.page.views.append(self.get_controls())
        self.page.update()
        
    
    def get_controls(self):
        return ft.View(
            route="/personalizar_treino",
            controls=[
                ft.Column(
                    [
                        ft.Text(f"personalizar treino {self.aluno_data}")
                    ]
                )
            ],
            appbar=ft.AppBar(
                title=ft.Text("Personalizar treino"),
                center_title=True,
                leading=ft.IconButton(icon=ft.Icons.ARROW_BACK,on_click= lambda e: route_control.go_to(self.page,route="/central_alunos"))
            )
        )