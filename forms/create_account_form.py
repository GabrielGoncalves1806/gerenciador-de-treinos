import flet as ft

class CreateAccountForm():
    def __init__(self):
        
        self.campo_nome = ft.TextField(label="Nome Completo")
        
        self.campo_email = ft.TextField(label="E-mail")
        
        self.campo_altura = ft.TextField(label="Altura")
        
        self.campo_peso = ft.TextField(label="Peso")
        
    def is_valid(self):
        pass
        
    def get_controls(self):
        return ft.Column(
            [
                self.campo_nome,
                self.campo_email,
                self.campo_altura,
                self.campo_peso,
                ft.ElevatedButton(
                    text="Salvar"
                )
            ]
        )