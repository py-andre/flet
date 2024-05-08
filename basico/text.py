import flet as ft
import datetime


def main(page: ft.Page):
    page.title = "Icon button with 'click' event"

    hora = datetime.datetime.now().strftime("%H:%M:%S")

    mytext = ft.Text(value=hora, color='blue', italic=True, size=20)

    def button_clicked(e):
        b.data = mytext.value
        t.value = f'hora certa: {b.data}'
        page.update()


    b = ft.IconButton(
        icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED,
        on_click=button_clicked,
        data='',
    )
    t = ft.Text()

    page.add(b, t)

ft.app(target=main)