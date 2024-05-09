import flet as ft
import string
import random


def letter_to_guess(letter):
    return ft.Container(
        bgcolor=ft.colors.AMBER_500,
        height=50,
        width=50,
        border_radius=ft.border_radius.all(5),
        content=ft.Text(
            value=letter,
            color=ft.colors.WHITE,
            size=30,
            text_align=ft.TextAlign.CENTER,
            weight=ft.FontWeight.BOLD,
        )
    )


def main(page: ft.Page):
    page.scroll = ft.ScrollMode.AUTO
    page.bgcolor = ft.colors.BROWN_600

    escolha_palavras = [
        'flet', 'python', 'kotlin', 'programador',
    ]
    choiced = random.choice(escolha_palavras).upper()

    def validate_letter(e):
        for pos, letter in enumerate(choiced):
            if e.control.content.value == letter:
                word.controls[pos] = letter_to_guess(letter=letter)
                word.update()
        if e.control.content.value not in choiced:
            victim.data += 1

            if victim.data > 7:
                page.dialog = ft.AlertDialog(
                    bgcolor=ft.colors.AMBER_300,
                    icon=ft.IconButton(icon=ft.icons.AIR),
                    title=ft.Text('Game Over'),
                    open=True
                )
                page.update()

            errors = victim.data
            victim.src = f'images/hangman_{errors}.png'
            victim.update()
        e.control.disabled = True
        e.control.gradient = ft.LinearGradient(
            colors=[ft.colors.GREY],
        )
        e.control.update()

    victim = ft.Image(
        data=0,
        src='images/hangman_0.png',
        repeat=ft.ImageRepeat.NO_REPEAT,
        height=300,
    )

    word = ft.Row(
        wrap=True,
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            letter_to_guess('_') for letter in choiced
        ]
    )

    game = ft.Container(
        col={'xs': 12, 'lg': 6},
        padding=ft.padding.all(50),
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                victim,
                word
            ]
        )
    )

    keyboard = ft.Container(
        col={'xs': 12, 'lg': 6},
        image_src='images/keyboard.png',
        image_repeat=ft.ImageRepeat.NO_REPEAT,
        image_fit=ft.ImageFit.FILL,
        padding=ft.padding.only(top=150, left=80, right=80, bottom=50),
        content=ft.Row(
            wrap=True,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    height=50,
                    width=50,
                    border_radius=ft.border_radius.all(5),
                    content=ft.Text(
                        value=letter,
                        color=ft.colors.WHITE,
                        size=30,
                        text_align=ft.TextAlign.CENTER,
                        weight=ft.FontWeight.BOLD,
                    ),
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.top_center,
                        end=ft.alignment.bottom_center,
                        colors=[ft.colors.AMBER, ft.colors.DEEP_ORANGE],
                    ),
                    on_click=validate_letter
                ) for letter in string.ascii_uppercase
            ]
        )
    )

    scene = ft.Image(col=12, src='images/scene.png')

    layout = ft.ResponsiveRow(
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        columns=12,
        controls=[
            scene,
            game,
            keyboard,
            scene
        ],
    )
    page.add(layout)


if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')
