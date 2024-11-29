import flet as ft
from views import add_workout
class HomeView():
    def __init__(self,page:ft.Page):
        # Definição das informções da janela
        self.page = page

        # Inicializando a janela
        self.page.views.append(self.create_homeview())
        self.page.update()

    def go_to(self,route):
        if route == '/add_workout':
            add_workout.AddWorkoutView(self.page)
            
    def create_homeview(self):
        return ft.View(
            route="/home",
            controls=[
                ft.Column(
                    [
                        ft.ElevatedButton(text='Add',on_click=lambda _: self.go_to('/add_workout'))
                    ]
                )
            ]
        )