import requests
from bs4 import BeautifulSoup
from kivy.app import App

url = 'https://rp5.ru/Погода_в_Волгограде'
# lst может принять'Сегодня ожидается +20..+17 °C°F, +68..+63 °C°F, cлабый дождь, легкий ветер. Завтра: +19..+16 °C°F, +66..+61 °C°F, cлабый дождь, свежий ветер.'
class WeatherApp(App):

    def statusWeather(self,*args):
        """Возвращает состояние осадков для дальнейшего вывода заднего фона кнопки погоды
        имя картинки равно статусу"""
        try:
            if self.status==200:
                return self.weathers().strip().split('\n')[2]
        except Exception:
            return 'connectError'


    def weathers(self, *args):
        global url
        global lst
        global status # для анимации иконки кнопки

        lst = []
        try:
            response = requests.get(url)
            self.status = response.status_code
            if self.status==200:
                bs = BeautifulSoup(response.text, 'lxml')
                temp = bs.find('span', class_="t_0")
                temp0=bs.find('b')

                for data in temp0.text.split(","):
                    lst.append(data)
                statusWeather = lst[2].strip()
                return f'Сейчас:{temp.text}\n{lst[0][:29]}\n{statusWeather}\n{lst[3].rsplit(".")[0].strip()}'
            return f'Неполадка: {status}'
        except requests.exceptions.ConnectionError:
            return 'Errors'









