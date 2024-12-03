import flet as ft
from views import login_view

def main(page:ft.Page):
    login_view.LoginPage(page)

ft.app(main)