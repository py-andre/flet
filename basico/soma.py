import flet as ft


def main(page: ft.Page):
    page.title = 'contador'
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.bgcolor = ft.colors.BLACK

    textnumber = ft.TextField(value='0', width=100, text_align=ft.TextAlign.CENTER)

    def num_add(e):
        textnumber.value = str(int(textnumber.value) + 1)
        textnumber.update()

    def num_remove(e):
        textnumber.value = str(int(textnumber.value) - 1)
        textnumber.update()

    container = ft.Container(
        border_radius=ft.border_radius.all(15),
        width=400,
        height=800,
        bgcolor=ft.colors.WHITE,

        content=ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.IconButton(icon=ft.icons.REMOVE, on_click=num_remove),
                textnumber,
                ft.IconButton(icon=ft.icons.ADD, on_click=num_add),

            ]
        )
    )

    page.add(container)


ft.app(main)
