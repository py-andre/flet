''' Flet Weather App '''
import flet
from flet import *
import requests
import datetime

api_key = 'ee6a896666fbdddfd920656aa97cf902'

_current = requests.get(
    f'http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={api_key}'
)
# Listas de dias da semana
day = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]


def main(page: Page):
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'

    # animation
    def _expand(e):
        if e.data == 'true':
            _c.content.controls[0].height = 560
            _c.content.controls[0].update()
        else:
            _c.content.controls[0].height = 660 * 0.40
            _c.content.controls[0].update()
        pass

    def _top():
        top = Container(
            width=310,
            height=660 * 0.40,
            gradient=LinearGradient(
                begin=alignment.bottom_left,
                end=alignment.top_right,
                colors=['lightblue600', 'lightblue900'],
            ),
            border_radius=border_radius.all(30),
            animate=animation.Animation(
                duration=500,
                curve=animation.AnimationCurve.DECELERATE,
            ),
            on_hover=lambda e: _expand(e),
            padding=10,
            content=Column(
                alignment='start',
                spacing=10,
                controls=[
                    Row(
                        alignment='center',
                        controls=[
                            Text('Toronto, CA', size=24, weight='bold', color=colors.WHITE),
                        ]
                    ),
                    Container(
                        padding=padding.only(bottom=5)
                    ),
                    Row(
                        alignment='center',
                        spacing=30,
                        controls=[
                            Column(
                                controls=[
                                    Container(
                                        width=90,
                                        height=90,
                                        image_src='images/cloudy.png',
                                    )
                                ]
                            )
                        ]
                    )
                ]
            )
        )
        return top

    _c = Container(
        width=310,
        height=660,
        border_radius=border_radius.all(30),
        bgcolor=colors.BLACK,
        padding=10,
        content=Stack(
            width=300,
            height=550,
            controls=[
                _top(),
            ]
        ),

    )
    page.add(_c)


if __name__ == '__main__':
    app(target=main, assets_dir='assets')
