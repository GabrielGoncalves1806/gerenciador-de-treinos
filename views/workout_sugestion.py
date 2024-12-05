import flet as ft
from controllers import route_control
from models import database_control
from widgets import workout_card


class WorkoutSugestionView():
    def __init__(self,page:ft.Page):
        self.page = page

        self.grupos_musculares = database_control.get_muscles()
        self.cards = ft.Row(expand=1, wrap=False, scroll="always")

        self.page.views.append(self.create_workout_sugestion_view())
        self.get_cards()
        self.page.update()
        
    def get_cards(self):
        for grupo in self.grupos_musculares:
            self.cards.controls.append(workout_card.WorkoutCard(grupo).get_control())

    def create_workout_sugestion_view(self):
        return ft.View(
            route="/workout_sugestion",
            controls=[
                ft.Column(
                    [
                        self.cards
                    ]
                )
            ],
            appbar=ft.AppBar(
                    title=ft.Text("Sugestão de treinos"),
                    center_title=True,
                    leading=ft.IconButton(icon=ft.Icons.ARROW_BACK,on_click=lambda _: route_control.go_home(self.page))
                )
        )