import flet as ft


def main(page: ft.Page):
    page.title = "Icon"

    icon1 = ft.Icon(ft.icons.SPA, color='blue')
    icon2 = ft.Icon(ft.icons.SPEAKER, color='green')
    icon3 = ft.Icon(ft.icons.SETTINGS, color='red', tooltip='Configurações')


    page.add(icon1, icon2, icon3)


ft.app(main)
