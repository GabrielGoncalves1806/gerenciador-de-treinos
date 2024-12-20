import views
import views.add_workout_view
import views.central_aluno_view
import views.create_account_view
import views.professor_pageview
import views.aluno_pageview
import views.login_view
import views.workout_sugestion_view

# Função de navegação entre rotas/janelas


def go_to(page, route, permission=None):
    print(route)
    for view in page.views:
        if route == view.route:
            page.views.pop()
            page.go(view.route)
            return
            
    if route == "/add_workout":
        views.add_workout_view.AddWorkoutView(page)
        
    elif route == "/workout_sugestion":
        views.workout_sugestion_view.WorkoutSugestionView(page)
        
    elif route == "/professor_page":
        views.professor_pageview.HomeView(page, permission)
        
    elif route == "/login_page":
        views.login_view.LoginPage(page)
        
    elif route == "/central_alunos":
        views.central_aluno_view.CentralAlunos(page)
        
    elif route == "/add_account":
        views.create_account_view.CreateAccount(page)
        
    elif route == "/aluno_page":
        views.aluno_pageview.AlunoPage(page)


# Função que volta até a home
def go_home(page):
    page.views.pop()
    top_view = page.views[-1]
    page.go(top_view.route)
