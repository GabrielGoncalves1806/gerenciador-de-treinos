import flet as ft
from widgets import lista_alunos, add_alunos
from controllers import route_control

class CentralAlunos():
    def __init__(self,page:ft.Page):
        self.page = page
        #self.page.dialog = add_alunos.DialogAddAluno().get_controls()
        
        
        self.lista_alunos_widget = lista_alunos.ListaAlunos(self.page).get_controls()
        self.page.views.append(self.create_central_view())
        self.page.update()

    

    def create_central_view(self):
        return ft.View(
            route="/central_alunos",
            controls=[
                ft.Column(
                    [   
                        ft.Text("Lista de alunos"),
                        self.lista_alunos_widget   
                    ]
                )
            ],
            appbar=ft.AppBar(
                title=ft.Text("Central de aluno"),
                leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: route_control.go_to(self.page,"/home")),
                center_title=True
            )
        )