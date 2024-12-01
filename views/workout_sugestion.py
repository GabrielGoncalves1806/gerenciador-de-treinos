import flet as ft
from controllers import route_control


class WorkoutSugestionView():
    def __init__(self,page:ft.Page):
        self.page = page

        self.page.views.append(self.create_workout_sugestion_view())
        self.page.update()

    def create_workout_sugestion_view(self):
        return ft.View(
            route="/workout_sugestion",
            controls=[
                ft.Column(
                    [
                        ft.Text('opa')
                    ]
                )
            ],
            appbar=ft.AppBar(
                    title=ft.Text("Sugestão de treinos"),
                    center_title=True,
                    leading=ft.IconButton(icon=ft.icons.ARROW_BACK,on_click=lambda _: route_control.go_home(self.page))
                )
        )