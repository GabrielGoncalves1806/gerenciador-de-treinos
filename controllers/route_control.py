from views import add_workout, workout_sugestion, homeview

# Função de navegação entre rotas/janelas
def go_to(page,route,permission=None):
        print(route)
        if route == '/add_workout':
            add_workout.AddWorkoutView(page)
        elif route == '/workout_sugestion':
            workout_sugestion.WorkoutSugestionView(page)
        elif route == "/home":
              homeview.HomeView(page,permission)


# Função que volta até a home
def go_home(page):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)