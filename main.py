import flet as ft
from views import login_view,homeview

def main(page:ft.Page):
    #homeview.HomeView(page,True)
    login_view.LoginPage(page)

ft.app(main)