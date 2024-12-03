import flet as ft

class LoginForm():
    def __init__(self):
        self.username_field = ft.TextField(
            label="Nome de usuário",
            width=300,
            keyboard_type=ft.KeyboardType.TEXT,
            hint_text="Insira seu nome de usuário",
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
    
    @property
    def username(self):
        return self.username_field.value.strip()
    
    @property
    def password(self):
        return self.password_field.value.strip()
    
    @property
    def tipo_usuario(self):
        return self.tipo_usuario_group.value
    
    def is_valid(self):
        # Valida se todos os campos foram preenchidos
        if not self.username or not self.password or not self.tipo_usuario:
            self.error_msg.value = "Preencha todos os campos para prosseguir."
            self.error_msg.visible = True

            return False
        self.error_msg.visible = False
        return True
    
    def get_controls(self):
        # Retorna os controles para a tela
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
           
    