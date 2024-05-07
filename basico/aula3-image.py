import flet as ft


def main(page: ft.Page):

    image = ft.Image(
        src= 'assets/image/python-image.jpg',
        border_radius=ft.border_radius.only(top_left=20, top_right=10),
    )
    page.add(image)

ft.app(target=main, assets_dir='assets')