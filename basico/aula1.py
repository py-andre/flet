import flet as ft


def aula1(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    page.vertical_alignment = ft.MainAxisAlignment.START
    # page.window_always_on_top = True
    # page.window_title_bar_hidden = False
    # page.window_frameless = True
    # page.window_center = True
    page.window_max_width = 400
    page.window_max_height = 700
    page.window_min_width = 200
    page.window_min_height = 300
    page.window_height = 700
    page.window_width = 400
    page.window_movable = False
    page.window_prevent_close = True
    # page.window_progress_bar = 30
    page.title = "Aula 1 - Flet"
    platform = page.platform
    print(platform)
    print(page.window_width, page.window_height)
    page.on_load = lambda e: print('carregou', page.window_width, page.window_height)
    page.on_resize = lambda e: print('tamannho', page.window_width, page.window_height)

    def window_event(e):
        match e.data:
            case 'move':
                print('Moveu a pagina')
            case 'resized':
                print('Redimensionou a pagina')
            case 'minimize':
                print('Minimizou a pagina')
            case _:
                print('Outra ação...')

    page.on_window_event = window_event
    page.add(
        ft.Container(ft.Text(value='Hello, World!', color=ft.colors.BLUE, size=30), bgcolor='yellow'),

        ft.Container(ft.Text(value='Bora Brasil', color=ft.colors.BLUE, size=30), bgcolor='green')

    )



ft.app(aula1)
