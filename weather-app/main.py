''' Flet Weather App '''
import flet
from flet import *
import requests
import json
import datetime

api_key = 'ee6a896666fbdddfd920656aa97cf902'
city_name = 'Toronto,CA'
link = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&lang=pt_br'


_current = requests.get(link)
dados = _current.json()
temperatura = dados['main']['temp'] - 273.15
print(f'{temperatura:.2f}')

# Listas de dias da semana
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']


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

    # current temp
    '''def _current_temp():
        _current_temp = int(_current.json()['current']['temp'])
        return [_current_temp]'''

    def _top():
        #
        #_today = _current_temp()

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
                            ),
                            Column(
                                spacing=5,
                                horizontal_alignment='center',
                                controls=[
                                    Text(
                                        'Today',
                                        size=12,
                                        text_align='center',
                                    ),
                                    Row(
                                        vertical_alignment='center',
                                        spacing=0,
                                        controls=[
                                            Container(
                                                content=Text(
                                                    # from requests
                                                    #_today[0],
                                                    value=f'{temperatura:.2f}',
                                                    size=30,
                                                    color=colors.WHITE,


                                                ),
                                            )
                                        ]

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
