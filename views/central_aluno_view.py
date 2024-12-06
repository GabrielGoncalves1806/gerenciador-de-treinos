import flet as ft

class CentralAlunos():
    def __init__(self,page:ft.Page):
        self.page = page
        
        self.page.views.append(self.create_central_view())
        self.page.update()

    def create_central_view(self):
        return ft.View(
            route="/central_alunos",
            controls=[
                ft.Column(
                    [
                        ft.Text('Central')
                    ]
                )
            ],
            appbar=ft.AppBar(
                title=ft.Text("Central de aluno")
            )
        )