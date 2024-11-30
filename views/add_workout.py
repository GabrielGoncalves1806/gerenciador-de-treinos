import flet as ft
from forms import add_workout
from controllers import route_control

class AddWorkoutView():
    def __init__(self,page:ft.Page):
        self.page = page

        self.workout_form = add_workout.WorkoutForm()
        
     # Inicializando a janela
        self.page.views.append(self.create_add_workout_view())
        self.page.update()

            
    def create_add_workout_view(self):
        return ft.View(
            route="/add_workout",
            controls=[
                ft.Column(
                    [
                        self.workout_form.get_form(),
                    ]
                )
            ],
            appbar=ft.AppBar(
                title=ft.Text('Adicionar novo Treino'),
                center_title=True,
                leading=ft.IconButton(ft.icons.ARROW_BACK,on_click=lambda _: route_control.go_home(self.page))
            )
        )