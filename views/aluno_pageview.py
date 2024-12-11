import flet as ft
from controllers import route_control

class AlunoPage():
    def __init__(self, page:ft.Page):
        self.page =  page
        
        self.page.views.append(self.create_aluno_page())
        self.page.update()
        
    def create_aluno_page(self):
        return ft.View(
            route="/aluno_page",
            controls=[
                
            ],
            appbar=ft.AppBar(
                title=ft.Text("Área do Aluno"),
                center_title=True,
                leading=ft.IconButton(ft.Icons.ARROW_BACK,on_click=lambda e: route_control.go_to(self.page,route="/login_page"))
            )
        )