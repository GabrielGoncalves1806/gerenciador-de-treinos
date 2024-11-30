import flet as ft
from controllers import route_control

class HomeView():
    def __init__(self,page:ft.Page):
        # Definição das informções da janela
        self.page = page
        self.page.window.height = 667
        self.page.window.width = 375
        self.page.vertical_alignment = "center"

        # Inicializando a janela
        self.page.views.append(self.create_homeview())
        self.page.update()

    # Função que cria a janela atual
    def create_homeview(self):
        return ft.View(
            route="/home",
            controls=[
                ft.Column(
                    [
                        # Cabeçalho com foto
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Image(src='assets/logo.jpeg',border_radius=200,height=100,width=100),
                                    ft.Text(
                                        "Seu guia de treinos diário",
                                        size=16,
                                        color=ft.colors.GREY_600,
                                        text_align="center",
                                    ),
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                        ),
                        
                        ft.Divider(),

                        # Opções
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.ElevatedButton(
                                        text="Adicionar Exercício",
                                        icon=ft.icons.ADD,
                                        on_click=lambda _: route_control.go_to(self.page,'/add_workout'),
                                        width=300
                                    ),

                                    ft.ElevatedButton(
                                        text="Sugestão de Treinos",
                                        icon=ft.icons.FITNESS_CENTER,
                                        
                                        width=300
                                    ),
                                ]
                            )                            
                        ),  
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            ],
            bottom_appbar=ft.BottomAppBar(
                content=ft.Row(
                    [
                        ft.IconButton(ft.icons.MENU),
                        ft.IconButton(ft.icons.SETTINGS)
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY
                ),
                
            ),
            appbar=ft.AppBar(
                title=ft.Text('Treinos FIT'),
                automatically_imply_leading=False,
                center_title=True
            )
        )