import flet as ft
from controllers import route_control
from widgets import workout_list

class HomeView():
    def __init__(self,page:ft.Page,permission:bool):
        # Definição das informções da janela
        self.page = page
        self.page.window.height = 667
        self.page.window.width = 375
        self.page.scroll = True
        self.page.vertical_alignment = "center"

        self.workout_list_widget = ft.Column()
        
        # Inicializando a janela
        
        self.page.views.append(self.create_homeview())
        self.get_workout_list()
        self.page.update()
    
    def get_workout_list(self):
        self.workout_list_widget.controls.append(workout_list.WorkoutList("peito").get_control())

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
                                    ft.Image(src="assets/logo.jpeg",border_radius=200,height=100,width=100),
                                    ft.Text(
                                        "Seu guia de treinos diário",
                                        size=16,
                                        color=ft.Colors.GREY_600,
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
                                        icon=ft.Icons.ADD,
                                        width=300,
                                        on_click=lambda e: route_control.go_to(self.page,"/add_workout"),
                                    ),

                                    ft.ElevatedButton(
                                        text="Sugestão de Treinos",
                                        icon=ft.Icons.FITNESS_CENTER,
                                        on_click=lambda e: route_control.go_to(self.page,"/workout_sugestion"),
                                        width=300
                                    ),
                                ]
                            ),                           
                        ),  
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            ],
            bottom_appbar=ft.BottomAppBar(
                content=ft.Row(
                    [
                        ft.IconButton(ft.Icons.SETTINGS)
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY
                ),
            ),
            appbar=ft.AppBar(
                title=ft.Text("Treinos FIT"),
                leading=ft.IconButton(ft.Icons.ARROW_BACK,on_click=lambda e: route_control.go_to(self.page,"/login_page")),
                center_title=True,
                actions=[
                    ft.PopupMenuButton(
                        icon=ft.Icons.MENU,
                        items=[
                            ft.PopupMenuItem(text="Central de alunos",on_click=lambda e: route_control.go_to(self.page,"/central_alunos")),
                            ft.PopupMenuItem(text="opção 2"),
                        ]
                    ),
                ] 
            )
        )