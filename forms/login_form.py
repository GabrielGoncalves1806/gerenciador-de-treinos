import flet as ft

# Formulario de login
class LoginForm():
    def __init__(self):

        # Criação dos campos necessários
        self.username_field = ft.TextField(
            label="Nome de usuário",
            value="gabriel",
            width=300,
            keyboard_type=ft.KeyboardType.TEXT,
            hint_text="Insira seu nome de usuário",
        )
        self.password_field = ft.TextField(
            label="Senha",
            value="123456",
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
    
    # Retorna os dados dos campos preenchidos
    def get_dados(self):
        return {
            "tipo_usuario":self.tipo_usuario_group.value,
            "username":self.username_field.value,
            "password":self.password_field.value
        }
    
    # Valida se todos os campos foram preenchidos
    def is_valid(self):
        dados = self.get_dados()
        if not dados['username'] or not dados['password'] or not dados["tipo_usuario"]:
            self.error_msg.value = "Preencha todos os campos para prosseguir."
            self.error_msg.visible = True
            return False
        self.error_msg.visible = False
        return True
    
    # Retorna os controles para a tela
    def get_controls(self):
        return ft.Column(
            [
                self.username_field,
                self.password_field,
                self.error_msg,
                ft.Row(
                    controls=[self.tipo_usuario_group],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
           
    