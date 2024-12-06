from views import add_workout_view, homeview, login_view, workout_sugestion_view, central_aluno_view

# Função de navegação entre rotas/janelas
def go_to(page,route,permission=None):
        print(route)
        if route == "/add_workout":
            add_workout_view.AddWorkoutView(page)
        elif route == "/workout_sugestion":
            workout_sugestion_view.WorkoutSugestionView(page)
        elif route == "/home":
              page.views.pop()
              homeview.HomeView(page,permission)
        elif route == "/login_page":
              page.views.pop()
              login_view.LoginPage(page)
        elif route == "/central_alunos":
              page.views.pop()
              central_aluno_view.CentralAlunos(page)


# Função que volta até a home
def go_home(page):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)