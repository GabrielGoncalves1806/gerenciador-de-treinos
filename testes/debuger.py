
# self.page.on_keyboard_event = self.on_keyboard

#     def on_keyboard(self,e: ft.KeyboardEvent):
#         print(e)
#         if e.key == "S" and e.ctrl:
#             self.page.show_semantics_debugger = not self.page.show_semantics_debugger
#             self.page.update()

import flet as ft

def main(page: ft.Page):
    def open_form_dialog(e):
        # Criação do diálogo
        dialog = ft.AlertDialog(
            title=ft.Text("Adicionar Novo Aluno"),
            content=ft.Column(
                [
                    ft.TextField(label="Nome do Aluno"),
                    ft.TextField(label="Idade", keyboard_type="number"),
                    ft.TextField(label="Email"),
                ]
            ),
            actions=[
                ft.TextButton("Cancelar", on_click=lambda e: close_dialog()),
                ft.TextButton("Salvar", on_click=lambda e: save_form())
            ],
        )
        # Abrindo o diálogo
        page.dialog = dialog
        dialog.open = True
        page.update()

    def close_dialog():
        # Fechando o diálogo
        page.dialog.open = False
        page.update()

    def save_form():
        # Salvar os dados do formulário (adicione sua lógica aqui)
        print("Formulário salvo!")
        close_dialog()

    # Adicionando um botão para abrir o formulário
    page.add(
        ft.ElevatedButton("Adicionar Aluno", on_click=open_form_dialog)
    )

ft.app(target=main)