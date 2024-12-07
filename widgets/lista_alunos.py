import flet as ft
from models import database_control
from widgets import add_alunos

class ListaAlunos():
    def __init__(self,page:ft.Page):
        self.page = page
        self.lista_alunos = database_control.get_alunos()

        #self.lista = ft.Column(scroll=True,horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        self.lista = ft.ListView(spacing=0)
        
        for alunos in self.lista_alunos:
            self.lista.controls.append(
                ft.Row(
                    [
                        ft.Container(
                            content=ft.Row(
                                [
                                    ft.Text(alunos[5])
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                
                            ),
                            bgcolor=ft.Colors.CYAN,
                            border_radius=25,
                            padding=8,
                            expand=True
                        ),
                        ft.Container(
                            content=ft.Row(
                                [
                                    # ft.IconButton(icon=ft.Icons.EDIT, on_click=lambda e, nome=alunos[5], email=alunos[2]: self.show_dialog(nome,email))
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                
                            ),
                            border_radius=25,
                            padding=8,
                            alignment=ft.alignment.center_right
                        )
                    ],
                    spacing=5
                )
            )

    def show_dialog(self,nome,email):
        print(self.lista_alunos)
        self.add_dialog = add_alunos.DialogAddAluno(nome,email).get_controls()
        self.page.dialog = self.add_dialog
        self.add_dialog.open = True
        self.page.update()

    def get_controls(self):
        return ft.Column(
            [
                self.lista
            ]
        )