import flet as ft
from models import database_control

class WorkoutForm():
    def __init__(self):
        self.grupos_musculares = database_control.get_muscles()

        self.nome_exercicio = ft.TextField(label='Nome do Exercicio',max_length=30)

        self.grupo_muscular_drop = ft.Dropdown(
                label="Grupos musculares",
            )
        
        self.series = ft.TextField(label='Séries',keyboard_type="NUMBER")

        self.repeticoes = ft.TextField(label='Repetições',keyboard_type="NUMBER")

        self.botao_salvar = ft.ElevatedButton(
            text="Salvar",
            on_click=self.save_values
        )

        for grupos in self.grupos_musculares:
            self.grupo_muscular_drop.options.append(ft.dropdown.Option(grupos))
        
        self.form = ft.Column(
            [
                self.nome_exercicio,
                self.grupo_muscular_drop,
                self.series,
                self.repeticoes,
                self.botao_salvar,
            ],
            spacing=10
        )

    def save_values(self,event):
        dados = self.get_values()
        print(dados)

    def get_values(self):
        return {
            "nome_exercicio": self.nome_exercicio.value,
            "grupo_muscular": self.grupo_muscular.value,
            "series": self.series.value,
            "repeticoes": self.repeticoes.value,
        }

    def get_form(self):
        """Retorna o layout completo do formulário"""
        return self.form