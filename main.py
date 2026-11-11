import flet as ft

def main(page: ft.Page):
    page.title = "Fada Iris"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#1a0b2e"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.padding = 20

    titulo = ft.Text(
        "✨ Fada Iris ✨",
        size=32,
        weight=ft.FontWeight.BOLD,
        color="#e9b8ff",
        text_align=ft.TextAlign.CENTER,
    )

    subtitulo = ft.Text(
        "Sua fadinha mágica chegou!",
        size=16,
        color="white70",
        text_align=ft.TextAlign.CENTER,
    )

    resposta = ft.Text(
        "",
        size=16,
        color="#ffd6ff",
        text_align=ft.TextAlign.CENTER,
    )

    def falar(e):
        resposta.value = "🧚‍♀️ Iris: Oi! Que bom te ver! O que você quer criar hoje?"
        page.update()

    botao = ft.ElevatedButton(
        "Falar com a Iris",
        bgcolor="#a855f7",
        color="white",
        on_click=falar,
        width=220,
        height=50,
    )

    page.add(
        ft.Column(
            [
                ft.Text("🧚‍♀️", size=100, text_align=ft.TextAlign.CENTER),
                titulo,
                subtitulo,
                ft.Container(height=20),
                botao,
                ft.Container(height=20),
                resposta,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
