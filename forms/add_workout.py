import flet as ft

class WorkoutForm():
    def __init__(self):
        self.grupos_musculares = [ 
        ft.dropdown.Option("Peito"),
        ft.dropdown.Option("Costas"),
        ft.dropdown.Option("Ombros"),
        ft.dropdown.Option("Trapézio"),
        ft.dropdown.Option("Tríceps"),
        ft.dropdown.Option("Bíceps"),
        ft.dropdown.Option("Antebraços"),
        ft.dropdown.Option("Quadríceps"),
        ft.dropdown.Option("Posteriores da Coxa"),
        ft.dropdown.Option("Glúteos"),
        ft.dropdown.Option("Panturrilhas"),
        ft.dropdown.Option("Abdominais"),
        ]
    
        self.nome_exercicio = ft.TextField(label='Nome do Exercicio',max_length=30)

        self.grupo_muscular = ft.Dropdown(
                label="Grupos musculares",
                options=self.grupos_musculares
            )
        self.series = ft.TextField(label='Séries',keyboard_type="NUMBER")
        self.repeticoes = ft.TextField(label='Repetições',keyboard_type="NUMBER")

        self.botao_salvar = ft.ElevatedButton(
            text="Salvar",
            on_click=self.save_values
        )

        self.form = ft.Column(
            [
                self.nome_exercicio,
                self.grupo_muscular,
                self.series,
                self.repeticoes,
                self.botao_salvar,
                ft.ElevatedButton(
                                text="Sugestão de Treinos",
                                icon=ft.icons.FITNESS_CENTER,
                                
                                width=300
                            ),
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