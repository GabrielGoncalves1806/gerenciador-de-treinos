import flet as ft
from random import choice


def main(page:ft.Page):
    cores = [
        ft.Colors.AMBER,
        ft.Colors.RED,
        ft.Colors.GREEN,
        ft.Colors.PURPLE,
        ft.Colors.PINK,
    ]

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
                ft.Text('Sugestão de treino'),
                cards
            ]
        )
        
    )

ft.app(main)