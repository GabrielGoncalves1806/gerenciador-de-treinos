import flet as ft
from models import database_control
from widgets import workout_list

class WorkoutCard():
    def __init__(self,grupo_muscular,lista_exercicios:ft.Column,page:ft.Page):
        self.page = page
        self.lista_exercicios = lista_exercicios
        self.grupo_muscular = grupo_muscular
        self.cor = ft.Colors.GREEN
        self.sprite = database_control.get_sprite_path(grupo_muscular)

    def atualiza_lista(self):
        try:
            self.lista_exercicios.clean()
            self.lista_exercicios.controls.append(workout_list.WorkoutList(self.grupo_muscular).get_control())
            self.lista_exercicios.update()
        except Exception as e:
            print(e)
        
    def get_control(self):
        return ft.Container(
                content=ft.Column(
                    [
                        ft.Text(value=self.grupo_muscular.upper(),size=20),
                        ft.Image(src=f"../assets/body_parts/{self.sprite}",width=100,height=100),
                        ft.ElevatedButton(text='Detalhes',color=self.cor,on_click=lambda e: self.atualiza_lista())
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                bgcolor=self.cor,
                border_radius=10,
                width=200,
                height=225,
                padding=10,
            )