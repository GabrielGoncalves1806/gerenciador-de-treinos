from views import add_workout_view, homeview, login_view, workout_sugestion_view, central_aluno_view

# Função de navegação entre rotas/janelas


def go_to(page, route, permission=None):
    print(route)
    for view in page.views:
        if route == view.route:
            page.views.pop()
            page.go(view.route)
            return
            
    if route == "/add_workout":
        add_workout_view.AddWorkoutView(page)
    elif route == "/workout_sugestion":
        workout_sugestion_view.WorkoutSugestionView(page)
    elif route == "/home":
        homeview.HomeView(page, permission)
    elif route == "/login_page":
        login_view.LoginPage(page)
    elif route == "/central_alunos":
        central_aluno_view.CentralAlunos(page)


# Função que volta até a home
def go_home(page):
    page.views.pop()
    top_view = page.views[-1]
    page.go(top_view.route)
