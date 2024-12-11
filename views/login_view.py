import flet as ft
from controllers import route_control
from models import login
from forms import login_form

class LoginPage():
    def __init__(self,page:ft.Page):
        self.page = page
        self.page.theme_mode = "dark"
        self.page.window.height = 667
        self.page.window.width = 375

        self.login_form = login_form.LoginForm()

        self.page.views.append(self.create_login_page())
        self.page.update()

    def login(self,e):
        # Caso o retorno do is_valid retorne True ele verifica no banco 
        # se as infomações recebidas correspondem 
        if self.login_form.is_valid():          
            permite_logar = login.validar_login(self.login_form.get_dados())

            # Se o validador de login do banco retorna True
            # significa que o usuário está apto a logar
            if permite_logar:
                
                if self.login_form.tipo_usuario_group.value == "professor":
                    route_control.go_to(page=self.page,route="/home",permission=True)
                
                elif self.login_form.tipo_usuario_group.value == "aluno":
                    route_control.go_to(self.page,"/home",permission=False)

            # Caso contrário exibe uma mensagem genérica
            else:
                self.login_form.error_msg.value = "Usuário ou senha incorretos!"
                self.login_form.error_msg.visible = True
                self.page.update()

        self.page.update()

    def create_login_page(self):
        return ft.View(
            route='/login',
        controls=[
            # Conteúdo principal
            ft.Column(
                controls=[

                    # Imagem/Icone com silhueta de user
                    ft.Container(
                        content=ft.Icon(name=ft.Icons.PERSON,size=100),
                        border=ft.border.all(1),
                        border_radius=150
                    ),
                    
                    ft.Text("Login", size=24, weight="bold", color="blue"),
                    
                    # Campos de texto exportados do form
                    
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
                spacing=20,
            ),
            # Rodapé
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text("Versão 1.0.0", size=12, weight="light"),
                        ft.Text("Contato: gabrielgoncalves1806@gmail.com", size=12, weight="light"),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=5
                ),
                alignment=ft.alignment.bottom_center,
                padding=10,
                
            ),
        ],
        appbar=ft.AppBar(
            title=ft.Text("Gestor de Treinos"),
            center_title=True,
            automatically_imply_leading=False


        ),
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )