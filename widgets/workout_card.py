import flet as ft
from models import muscle_sprite

class WorkoutCard():
    def __init__(self,grupo_muscular,cor):
        self.grupo_muscular = grupo_muscular
        self.cor = cor
        self.sprite = muscle_sprite.get_muscle_sprite(grupo_muscular)

    def card(self):
        return ft.Container(
                content=ft.Column(
                    [
                        ft.Text(value=self.grupo_muscular.upper(),size=20),
                        ft.Image(src=f"../assets/body_parts/{self.sprite}",width=100,height=100),
                        ft.ElevatedButton(text='Detalhes',color=self.cor)
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                bgcolor=self.cor,
                border_radius=10,
                width=200,
                height=200,
                padding=10,
                
            )