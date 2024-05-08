import flet as ft
import time
from datetime import datetime

def main(page: ft.Page):
    page.title = "Icon Button"

    def selected(e):
        e.control.selected = not e.control.selected
        e.control.update()

    btn1 = ft.IconButton(
        icon=ft.icons.PLAY_CIRCLE,
        icon_color=ft.colors.BLUE,
        icon_size=100,
        style=ft.ButtonStyle(
            color={
                ft.MaterialState.DEFAULT: ft.colors.BLUE,
                ft.MaterialState.SELECTED: ft.colors.RED,
            }
        ),
        selected=True,
        selected_icon=ft.icons.PAUSE_CIRCLE,
        on_click=selected
    )

    page.add(btn1)


ft.app(target=main)