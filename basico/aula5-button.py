import flet as ft


def main(page: ft.Page):
    page.title = "Button"
    page.spacing = 50

    btn1 = ft.ElevatedButton(text='Clique aqui')

    btn2 = ft.ElevatedButton(text='Botão inativo', disabled=True)

    btn3 = ft.ElevatedButton(text='Botão com icone', icon=ft.icons.FAVORITE, icon_color=ft.colors.PINK_700)

    btn4 = ft.ElevatedButton(
        text='Demais propriedades',
        bgcolor=ft.colors.AMBER_300,
        color=ft.colors.WHITE,
        icon=ft.icons.FAVORITE_BORDER,
        icon_color=ft.colors.WHITE,
        tooltip='Olá eu sou um botão',
        url='https://www.google.com.br/',
    )
    styles = ft.ButtonStyle(
        color={
            ft.MaterialState.DEFAULT: ft.colors.BLACK,
            ft.MaterialState.HOVERED: ft.colors.RED,
        },
        bgcolor={
            ft.MaterialState.DEFAULT: ft.colors.WHITE,
            ft.MaterialState.HOVERED: ft.colors.BLUE,
        },
        padding={
            ft.MaterialState.DEFAULT: 10,
            ft.MaterialState.HOVERED: 20,
        },
        side={
            ft.MaterialState.HOVERED: ft.BorderSide(width=3, color=ft.colors.BLUE),
            ft.MaterialState.DEFAULT: ft.BorderSide(width=1, color=ft.colors.BLACK),
        },
        shape={
            ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=30),
            ft.MaterialState.DEFAULT: ft.BeveledRectangleBorder(radius=1),

        },
        # elevation=5,,
        animation_duration=1000,

    )

    btn5 = ft.ElevatedButton(
        text='Botão com style personalizado.',
        style=styles,
    )

    def num(e):
        e.control.data += 1
        btn6.update()
        text.value = f'Botão clicado {btn6.data} vezes'
        text.update()

    btn6 = ft.ElevatedButton(
        text='Numeros',
        bgcolor=ft.colors.RED,
        on_click=num,
        data=0,
    )
    text = ft.Text()

    page.add(
        btn1, btn2, btn3, btn4, btn5, btn6, text
    )


ft.app(main)
