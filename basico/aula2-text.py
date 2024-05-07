import flet as ft


def main(page: ft.Page):

    t = ft.Text(
        value='Hello, Bem vindo ao curso de flet.', color=ft.colors.RED,
        font_family='NSimSun',
        italic=True
    )
    t2 = ft.Text(
        spans=[
            ft.TextSpan(text='google',url='https://google.com'),
            ft.TextSpan(text='flet', url='https://flet.dev'),
        ]
    )
    page.add(t, t2)
ft.app(target=main, assets_dir='assets')