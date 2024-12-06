import flet as ft
from models import database_control

class WorkoutList():
    def __init__(self,grupo_mucular):
        self.exercicios = database_control.get_exercicios(grupo_mucular)
        
        self.lista_exercicios = ft.DataTable(
            columns=[
                ft.DataColumn(label=ft.Text("Exercicio")),
            ],
            border=ft.border.all(1),
            border_radius=15,
        )

        for exercicio in self.exercicios:
            self.lista_exercicios.rows.append(
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text(exercicio[0].capitalize())),
                ])
            )

        self.lista_exercicios2 = ft.Row()

    def get_control(self):
        return ft.Column(
            [
                self.lista_exercicios
            ],
            height=200, 
            wrap=False,
            scroll="always",
            
        )
