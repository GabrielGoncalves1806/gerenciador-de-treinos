import flet as ft
from controllers import route_control
from models import database_control, temporary_session
from widgets import personalizar_treino

class ListaAlunos():
    def __init__(self,page:ft.Page):
        self.page = page
        self.session = temporary_session.LocalSession().get_session()
        self.lista_alunos = database_control.get_alunos_by_professor_id(self.session["id"])

        #self.lista = ft.Column(scroll=True,horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        self.lista = ft.ListView(spacing=10)
        
        for alunos in self.lista_alunos:
            self.lista.controls.append(
                ft.Row(
                    [
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Text(alunos[5].capitalize(),weight="bold",size=18),
                                    ft.Text("23 anos | 75kg"),
                                    ft.ElevatedButton(text="Personalizar treino",on_click=lambda e, id=alunos[0]: route_control.go_to(self.page,route="/personalizar_treino",data={"id":id}))
                                ],
                                
                                alignment=ft.MainAxisAlignment.CENTER,
                                
                            ),
                            bgcolor=ft.Colors.CYAN,
                            border_radius=10,
                            padding=8,
                            expand=True,
                        ),
                        # ft.Container(
                        #     content=ft.Row(
                        #         [
                        #             ft.IconButton(icon=ft.Icons.EDIT, on_click=lambda e, nome=alunos[5], email=alunos[2]: self.show_dialog(nome,email))
                        #         ],
                        #         alignment=ft.MainAxisAlignment.CENTER,
                                
                        #     ),
                        #     border_radius=25,
                        #     padding=8,
                        #     alignment=ft.alignment.center_right
                        # )
                    ],
                    spacing=5
                )
            )

    def show_dialog(self,e):
        self.add_dialog = personalizar_treino.PersonalizarTreinoAluno(e.control.data).get_controls()
        self.page.overlay.append(self.add_dialog)
        self.add_dialog.open = True
        self.page.update()

    def get_controls(self):
        return ft.Column(
            [
                self.lista
            ]
        )