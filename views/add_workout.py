import flet as ft
from forms import add_workout

class AddWorkoutView():
    def __init__(self,page:ft.Page):
        self.page = page

        self.workout_form = add_workout.WorkoutForm()
        

     # Inicializando a janela
        self.page.views.append(self.create_add_workout_view())
        self.page.update()

    def go_home(self,e):
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)
            
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
                leading=ft.IconButton(ft.icons.ARROW_BACK,on_click=self.go_home)
            )
        )