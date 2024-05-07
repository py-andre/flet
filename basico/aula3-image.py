import flet as ft


def main(page: ft.Page):
    page.title = 'Image'

    image = ft.Image(
        src='https://wallpapercave.com/wp/wp4850088.jpg',
        border_radius=ft.border_radius.only(top_left=20, top_right=10, bottom_left=10, bottom_right=20),
        width=300,
        height=1000,
        fit=ft.ImageFit.CONTAIN,
        repeat=ft.ImageRepeat.REPEAT_Y,

    )

    page.add(image)


ft.app(target=main, assets_dir='assets')
