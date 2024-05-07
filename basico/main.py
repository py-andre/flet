import flet as ft


def main(page: ft.Page):
    page.bgcolor = ft.colors.ORANGE
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    layout = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(value="Hello, World!", color=ft.colors.WHITE, size=30),
                ft.Text(value="Hello, World!", color=ft.colors.WHITE, size=30),
            ]
        )
    )
    page.add(layout)
ft.app(main)
