import flet as ft
from random import choice

def main(page:ft.Page):
    cores = [
        ft.colors.AMBER,
        ft.colors.GREEN,
        ft.colors.RED,
        ft.colors.PURPLE,
        ft.colors.PINK,
    ]
    cards = ft.Row(expand=1, wrap=False, scroll="always")
    for x in range(1,5):
        cards.controls.append(
            ft.Container(
            content=ft.Column(
                [
                    ft.Text(f'Treino de Peito {x}'),
                    
                ]
            ),
            bgcolor=choice(cores),
            border_radius=10,
            width=200,
            height=200,
            padding=10
        )
        )
    page.add(
        cards
    )

ft.app(main)