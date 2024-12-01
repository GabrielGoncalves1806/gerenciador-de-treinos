import flet as ft
from random import choice


def main(page:ft.Page):
    cores = [
        ft.Colors.RED,        # Para Peito
        ft.Colors.BLUE,       # Para Costas
        ft.Colors.ORANGE,     # Para Ombros
        ft.Colors.YELLOW,      # Para Trapézio
        ft.Colors.GREEN,      # Para Tríceps
        ft.Colors.PURPLE,     # Para Bíceps
        ft.Colors.BROWN,      # Para Antebraços
        ft.Colors.LIGHT_GREEN, # Para Quadríceps
        ft.Colors.GREY_200,  # Para Posteriores da Coxa
        ft.Colors.PINK,       # Para Glúteos
        ft.Colors.LIGHT_BLUE, # Para Panturrilhas
        ft.Colors.TEAL,       # Para Abdômen
    ]

    # cores = [valor for nome, valor in vars(ft.Colors).items() if not nome.startswith("_")]
    
    cards = ft.Row(expand=1, wrap=False, scroll="always")
    for x in range(1,6):
        cor = choice(cores)
        cores.remove(cor)
        cards.controls.append(
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text(f'Treino de Peito {x}',size=20),
                        ft.Image(src='../assets/body_parts/costas.png',width=100,height=100),
                        ft.ElevatedButton(text='Detalhes',color=cor)
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                bgcolor=cor,
                border_radius=10,
                width=200,
                height=200,
                padding=10,
                
            )
        )
    page.add(
        ft.Column(
            [
                cards
            ]
        )
        
    )

ft.app(main)