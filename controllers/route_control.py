from views import add_workout, workout_sugestion, homeview, login_view

# Função de navegação entre rotas/janelas
def go_to(page,route,permission=None):
        print(route)
        if route == "/add_workout":
            add_workout.AddWorkoutView(page)
        elif route == "/workout_sugestion":
            workout_sugestion.WorkoutSugestionView(page)
        elif route == "/home":
              page.views.pop()
              homeview.HomeView(page,permission)
        elif route == "/login_page":
              page.views.pop()
              login_view.LoginPage(page)


# Função que volta até a home
def go_home(page):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)