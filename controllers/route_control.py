from views import add_workout

# Função de navegação entre rotas/janelas
def go_to(page,route):
        print(route)
        if route == '/add_workout':
            add_workout.AddWorkoutView(page)

# Função que volta até a home
def go_home(page):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)