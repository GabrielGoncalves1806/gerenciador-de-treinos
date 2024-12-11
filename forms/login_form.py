import flet as ft
from models import database_control

# Formulario de login
class LoginForm():
    def __init__(self):

        # Criação dos campos necessários
        self.email_field = ft.TextField(
            label="E-mail",
            width=300,
            keyboard_type=ft.KeyboardType.TEXT,
            hint_text="Insira seu email de login",
        )
        self.password_field = ft.TextField(
            label="Senha",
            width=300,
            password=True,
            can_reveal_password=True,
            hint_text="Insira sua senha",
        )
        self.tipo_usuario_group = ft.RadioGroup(
            content=ft.Row([
                ft.Radio(label="Sou aluno", value="aluno"),
                ft.Radio(label="Sou professor", value="professor")
            ])
        )
        self.error_msg = ft.Text(value="", color=ft.Colors.RED, visible=False)

    def get_professor(self):
        professor = database_control.get_professor_id(self.username_field)
    
    # Retorna os dados dos campos preenchidos
    def get_dados(self):
        return {
            "tipo_usuario":self.tipo_usuario_group.value,
            "email":self.email_field.value,
            "password":self.password_field.value
        }
    
    # Valida se todos os campos foram preenchidos
    def is_valid(self):
        dados = self.get_dados()
        if not dados["email"] or not dados["password"] or not dados["tipo_usuario"]:
            self.error_msg.value = "Preencha todos os campos para prosseguir."
            self.error_msg.visible = True
            return False
        self.error_msg.visible = False
        return True
    
    # Retorna os controles para a tela
    def get_controls(self):
        return ft.Column(
            [
                self.email_field,
                self.password_field,
                self.error_msg,
                ft.Row(
                    controls=[self.tipo_usuario_group],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
           
    