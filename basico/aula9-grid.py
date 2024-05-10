import flet as ft


def main(page: ft.Page):
    page.title = "Grid"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = ft.colors.BLACK

    _c = ft.Container(
        width=600,
        height=900,
        bgcolor="black",
        border_radius=ft.border_radius.all(10),
        content=ft.GridView(

            runs_count=3,
            controls=[
              ft.Image(
                  border_radius=ft.border_radius.all(10),
                  src=f'https://picsum.photos/200/300?{num}',
                  fit=ft.ImageFit.COVER
              )for num in range(30)
            ]
        )

    )
    page.add(_c)


if __name__ == "__main__":
    ft.app(target=main)