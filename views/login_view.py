import flet as ft
from controllers import route_control
from models import login
from forms import login_form

class LoginPage():
    def __init__(self,page:ft.Page):
        self.page = page
        self.page.window.height = 667
        self.page.window.width = 375

        self.login_form = login_form.LoginForm()

        self.page.views.append(self.create_login_page())
        self.page.update()

    def login(self,e):
        if self.login_form.is_valid():          
            permite_logar = login.validar_login(
                tabela=self.login_form.tipo_usuario,
                username=self.login_form.username,
                senha=self.login_form.password
            )

            if permite_logar:
                route_control.go_to(self.page,"/home")

            else:
                self.login_form.error_msg.value = "Usuário ou senha incorretos!"
                self.login_form.error_msg.visible = True
                self.page.update()

        else:
            self.login_form.error_msg.value = "Preencha todos os campos para prosseguir",
            self.login_form.error_msg.visible = True
            self.page.update()

    def create_login_page(self):
        return ft.View(
        controls=[
            # Conteúdo principal
            ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Icon(name=ft.Icons.PERSON,size=100),
                        border=ft.border.all(1),
                        border_radius=150
                    ),
                    
                   
                    ft.Text("Login", size=24, weight="bold", color="blue"),
                    # Campos de texto
                    self.login_form.get_controls(),
                    # Botão de login
                    ft.ElevatedButton(
                        text="Entrar",
                        on_click=self.login,
                        width=300,
                        color="white",
                        bgcolor="blue"
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,  # Espaçamento entre elementos
            ),
            # Rodapé
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text("Versão 1.0.0", size=12, weight="light"),
                        ft.Text("Contato: suporte@exemplo.com", size=12, weight="light"),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=5
                ),
                alignment=ft.alignment.bottom_center,
                padding=10,
                
            ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )