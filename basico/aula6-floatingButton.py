import flet as ft

def main(page: ft.Page):
    page.title = "Floating Button"
    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.ADD,
        bgcolor=ft.colors.SURFACE_VARIANT,
        mini=False,
        # text='Adicionar',
        on_click=lambda _: print('clicado...')



    )
    page.update()


ft.app(main)