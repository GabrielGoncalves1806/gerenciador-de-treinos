import flet as ft
from views import home_view

def main(page:ft.Page):
    home_view.HomeView(page)

ft.app(main)