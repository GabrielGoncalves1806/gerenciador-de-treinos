import flet as ft
from models import database_control

class WorkoutCard():
    def __init__(self,grupo_muscular):
        self.grupo_muscular = grupo_muscular
        self.cor = ft.Colors.GREEN
        self.sprite = database_control.get_sprite_path(grupo_muscular)

    def get_control(self):
        return ft.Container(
                content=ft.Column(
                    [
                        ft.Text(value=self.grupo_muscular.upper(),size=20),
                        ft.Image(src=f"../assets/body_parts/{self.sprite}",width=100,height=100),
                        ft.ElevatedButton(text='Detalhes',color=self.cor)
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                bgcolor=self.cor,
                border_radius=10,
                width=200,
                height=225,
                padding=10,
                
            )