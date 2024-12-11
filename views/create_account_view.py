import flet as ft
from controllers import route_control
from forms import create_account_form

class CreateAccount():
    def __init__(self,page:ft.Page):
        self.page = page
        
        self.create_account_form = create_account_form.CreateAccountForm()
        
        self.page.views.append(self.create_add_account_view())
        self.page.update()
        
    def create_add_account_view(self):
        return ft.View(
            route="/add_account",
            controls=[
                self.create_account_form.get_controls()
            ],
            appbar=ft.AppBar(
                title=ft.Text("Criar Conta"),
                leading=ft.IconButton(ft.Icons.ARROW_BACK,on_click=lambda e: route_control.go_to(self.page,"/login")),
                center_title=True
            )
            
        )
    
    