import flet as ft


def main(page: ft.Page):
    page.title = "Popup Button"

    pb = ft.PopupMenuButton(
        icon=ft.icons.MENU,
        items=[
            ft.PopupMenuItem(text="Menu", icon=ft.icons.MENU),
            ft.PopupMenuItem(
                content=ft.Column(
                    spacing=2,
                    controls=[
                        ft.Row(
                            controls=[
                                ft.IconButton(icon=ft.icons.ADD, icon_color=ft.colors.BLUE),
                                ft.Text(value='Adicionar', color=ft.colors.BLUE),
                            ]
                        ),
                        ft.Row(
                            controls=[
                                ft.IconButton(icon=ft.icons.EDIT, icon_color=ft.colors.GREEN),
                                ft.Text(value='Editar', color=ft.colors.GREEN),
                            ]
                        ),

                    ]
                )
            ),
            ft.PopupMenuItem(),
            ft.PopupMenuItem(
                content=ft.Column(
                    spacing=2,
                    controls=[
                        ft.Row(
                            controls=[
                                ft.IconButton(icon=ft.icons.DELETE, icon_color=ft.colors.RED),
                            ]
                        ),
                        ft.Row(
                            controls=[
                                ft.IconButton(icon=ft.icons.FAVORITE, icon_color=ft.colors.RED),
                            ]
                        )
                    ]
                )

            )

        ]
    )

    page.add(pb)


ft.app(target=main)
