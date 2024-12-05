import flet as ft
from models import database_control

class WorkoutList():
    def __init__(self,grupo_mucular):
        self.exercicios = database_control.get_exercicios(grupo_mucular)
        
        self.lista_exercicios = ft.DataTable(
            columns=[
                #ft.DataColumn(label=ft.Text("ID")),
                ft.DataColumn(label=ft.Text('Exercicio')),
            ],
        )

        for exercicio in self.exercicios:
            self.lista_exercicios.rows.append(
                ft.DataRow(cells=[
                    #ft.DataCell(ft.Text(exercicio[0])),
                    ft.DataCell(ft.Text(exercicio[0].capitalize())),
                    # ft.DataCell(ft.Text(database_control.get_grupo_muscular(exercicio[2]).capitalize()))
                ])
            )

    def get_control(self):
        return ft.Column(
            [
                self.lista_exercicios
            ],
            scroll=True,
            height=200
        )
