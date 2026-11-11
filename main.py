import flet as ft

def main(page: ft.Page):
    page.title = "Teste Iris"
    page.bgcolor = "black"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def clicou(e):
        texto.value = "Deu certo! Flet tá pegando!"
        texto.color = "green"
        page.update()

    texto = ft.Text("Olá, Iris!", size=30, color="white")
    botao = ft.ElevatedButton("Clica aqui", on_click=clicou, bgcolor="green", color="white")

    page.add(texto, botao)

ft.app(target=main)
