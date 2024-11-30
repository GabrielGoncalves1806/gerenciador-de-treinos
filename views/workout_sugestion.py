import flet as ft


class WorkoutSugestionView():
    def __init__(self,page:ft.Page):
        self.page = page

        self.page.views.append(self.create_workout_sugestion_view())

    def create_workout_sugestion_view(self):
        return