from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.properties import ObjectProperty
from kivy.lang import Builder
import fixtures
from Setting.weater import *
from Setting.ScrollClass import ScrollScreenApp
from fixtures import *
from Setting.RoundButton import RoundedButton


# Цвет кнопок главного меню выбора


count_press_macrobutton = 0 # анимирует кнопку погоды
contaynerIcon = {'cлабый дождь':'Icon/lightrain.png','без осадков':'Icon/noprecipitation.png','connectError':'Icon/connectError.png'}
Builder.load_file('newtitlescreen.kv')
Builder.load_file('ballcalkulator.kv')
Builder.load_file('actualtemperature.kv')
Builder.load_file('wlipcalculator.kv')
Builder.load_file('imagekv.kv')
Builder.load_file('straightening.kv')
Builder.load_file('notacceleration.kv')
Builder.load_file('aboutprogram.kv')

class NewTitleScreen(Screen):
    """ГЛАВНЫЙ ЭКРАН!"""
    def __init__ (self, **kwargs):
        super().__init__(**kwargs)
        weather_city = WeatherApp()
        self.result_temp = weather_city.weathers()
        self.icon = weather_city.statusWeather()


    def press_macrobutton(self, *args):
        """Функция масштабирует кнопку погоды(macrobutton),
        меняет параметры кнопки,задний фон
        """
        global count_press_macrobutton
        global contaynerIcon
        count_press_macrobutton += 1
        if count_press_macrobutton >2:
            count_press_macrobutton = 1

        if count_press_macrobutton % 2 != 0:
            self.ids.fg.color_Button = (1,1,1,1)
            self.ids.fg.text = str(self.result_temp)
            self.ids.fg.color = colorWeatherText# Цвет текста
            self.ids.fg.size_hint = (0.8, 0.6)
            self.ids.fg.color = colorWeatherText
            if self.icon in contaynerIcon:
                self.ids.fg.btn_color_not_pressed = f"{contaynerIcon[self.icon]}"
        else:
            flagColor = True
            self.ids.fg.color_Button = colorWeatherButton
            self.ids.fg.btn_color_not_pressed =''
            self.ids.fg.text = f'{yellow}[b]Прогноз[/b]{rgbClose}'
            self.ids.fg.pos_hint={'right':0.9,'y':0.1}
            self.ids.fg.size_hint =None,None
            self.ids.fg.size=(self.ids.fg.texture_size[0]*2,self.ids.fg.texture_size[1]*2)



    # Кнопки выбора расчетов на главном экране-переводят пользователя в выбранный раздел
    def on_press_button_Ballcalculator(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'Ballcalculator'

    def on_press_button_ActualTemperature(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'ActualTemperature'

    def on_press_button_WlipCalculator(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'WlipCalculator'

    def on_press_button_Imagekv(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'Imagekv'

    def on_press_button_Straightening(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'Straightening'
    def on_press_button_NotAcceleration(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'NotAcceleration'

    def on_press_button_HandBook(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'HandBook'

    def on_press_button_AboutProgram(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'AboutProgram'

class Ballcalculator(Screen):
    """Класс выполняет расчет балловой оценки #### Текст для модулей KV в fixtures.kv"""

    #Блок функций

    def on_press_calculation(self, *args):
        """Расчет формулы и вызов функции <ubdate_label>"""
        self.ids.superScrollLabel.size_hint_y = 1#Текст по центру
        if self.otl.text and self.hor.text and self.udo.text and self.neud.text:
            if self.otl.text == self.hor.text == self.udo.text==self.neud.text =='0':
                self.superScrollLabel.text = '[color=f20707]Введите не нулевые\nзначения![/color]'
            else:
                line = round(float(self.otl.text) + float(self.hor.text) + float(self.udo.text) + float(self.neud.text))
                ball = round((float(self.otl.text) * 5 + (float(self.hor.text) * 4) + (float(self.udo.text) * 3) - (
                        int(self.neud.text) * 5))/line,2)
                estimation = [f'{lime}ОТЛИЧНО{rgbClose}', f'{blue}ХОРОШО{rgbClose}', f'{yellow}УДОВЛЕТВОРИТЕЛЬНО{rgbClose}', f'{red}НЕУДОВЛЕТВОРИТЕЛЬНО{rgbClose}'][
                    0 if ball > 4.5 else 1 if 3.8 < ball <= 4.5 else 2 if 3.0 < ball <= 3.8 else 3]  # Оценка
                self.superScrollLabel.text = f"{orange}Балловая оценка участка{rgbClose} = {lime}{ball}{rgbClose} балла\n" \
                               f"{orange}Протяженность{rgbClose} = {lime}{line}{rgbClose} км\n" \
                                             f"{orange}Оценка участка: {estimation}{rgbClose}"

        else:
            self.superScrollLabel.text= '[color=f20707]Введите данные![/color]'



    def add_cleer(self, *args):
        """Очистка поля ввода при нажатии клавиши Очистить"""
        self.ids.superScrollLabel.size_hint_y = None #Текст скроллится
        self.superScrollLabel.text = ballcalkulatorText
        self.otl.text = ''
        self.hor.text = ''
        self.udo.text = ''
        self.neud.text = ''
        ###

    def on_press_button_back(self, *args):
        """
        Выбор страницы. Обращается по имени,указанному в Родительском классе БИЛД
        """
        self.manager.transition.direction = 'right'
        self.manager.current = 'NewTitleScreen'
class ActualTemperature(Screen):
    """Расчет фактической температуры рельсовой плети. Распоряжение ОАО РЖД от 18.05.2010 N 1063р
    #### Текст для модулей KV в fixtures.kv"""

    def add_alpha(self,*args):
        """Возвращает коэффициент АЛЬФА в зависимости от длины участка(рекомендуемое не более 50м-альфа==0,6)"""
        if self.line.text:
            return int(self.line.text)*1000*0.0000118
        return 1

    def add_summ(self,*args):
        """В случае удлинения плети вычитает значения"""
        self.ids.superScrollLabel.size_hint_y = 1
        try:
            if self.actualtemperature.text and self.offset.text and self.line.text!='0':
                self.formula = f'{orange}Фактическая температура закрепления равна:{rgbClose}\n{lime}{str(round(int(self.actualtemperature.text)+(int(self.offset.text)/self.add_alpha())))}{rgbClose} {chr(176)}'
                self.superScrollLabel.text = self.formula
            else:
                self.formula = '[color=f20707]Введите данные![/color]'
            self.superScrollLabel.text = self.formula
            # size_hint_y: 1 #Центр текста
        except Exception:
            self.superScrollLabel.text = ErrorCalculate

    def add_difference(self,*args):
        """В случае укороченя плети складывает значения"""
        try:
            if self.actualtemperature.text and self.offset.text and self.line.text!='0':
                self.formula = f'{orange}Фактическая температура закрепления равна:{rgbClose}\n{lime}{str(round(int(self.actualtemperature.text)-(int(self.offset.text)/self.add_alpha())))}{rgbClose} {chr(176)}'
                self.superScrollLabel.text = self.formula
            else:
                self.formula = '[color=f20707]Введите данные![/color]'
            self.ids.superScrollLabel.size_hint_y = 1
            self.superScrollLabel.text = self.formula
        except Exception:
            self.superScrollLabel.text = ErrorCalculate



    def add_cleer(self,*args):
        """Очистка поля ввода при нажатии клавиши Очистить"""
        self.ids.superScrollLabel.size_hint_y = None
        self.superScrollLabel.text =actualtemperatureText
        self.actualtemperature.text = ''
        self.offset.text = ''
        self.line.text = '50'


    def on_press_button_back(self, *args):
        """
        Выбор страницы. Обращается по имени,указанному в Родительском классе БИЛД
        """
        self.manager.transition.direction = 'right'
        self.manager.current = 'NewTitleScreen'
class WlipCalculator(Screen):
    """Расчет подвижек рельсовой плети в зависимости от
    введенной длины, температуры закрепления и фактической темпратуры
    #### Текст для модулей KV в fixtures.kv"""
    # расчет значений
    def print_result(self):
        self.ids.superScrollLabel.size_hint_y = None  # Текст по центру
        self.superScrollLabel.text = ''
        for i in range(0,int(self.distanc.text)+1,50):
            self.superScrollLabel.text +=f'{yellow}сечение : {lime}{str(i)}{rgbClose} {rgbClose}смещение - ' \
                                         f'{lime}{round((int(self.optimal_temperature.text)-int(self.actual_temperature.text))*i*0.0118)}{rgbClose} мм\n'

        self.superScrollLabel.text +=f'\n{orange}Итоговое удлинение на {lime}{self.distanc.text} м{rgbClose}{rgbClose} ' \
                                     f'составит {red}{round((int(self.optimal_temperature.text)-int(self.actual_temperature.text))*int(self.distanc.text)*0.0118)}{rgbClose}{rgbClose} мм'

    def on_press_calculation(self,*args):

        """
        :param args: Обрабатывает нажатие клавиши Расчет. Принимает 3 числа.
        :return: True - передает в функцию print_result результат расчета формулы итоговое удлинение плети
        """
        try:
            if self.optimal_temperature.text and self.actual_temperature.text and self.distanc.text:
                self.print_result()
            else:
                self.superScrollLabel.text = '[color=f20707]Введите данные![/color]'
        except Exception:
            self.superScrollLabel.text = ErrorCalculate
    #end
    def add_cleer(self,*args):
        """Очистка поля ввода при нажатии клавиши Очистить"""
        self.ids.superScrollLabel.size_hint_y = 1  # Текст по центру
        self.superScrollLabel.text = wlipcalculatorText
        self.distanc.text = ''
        self.actual_temperature.text = ''
        self.optimal_temperature.text = ''


    def on_press_button_back(self, *args):
        """
        Выбор страницы. Обращается по имени,указанному в Родительском классе БИЛД
        """
        self.manager.transition.direction = 'right'
        self.manager.current = 'NewTitleScreen'
class Imagekv(Screen):
    """Расчет отвода возвышения переводной кривой
    Работает с imagekv.kv, подгружен через билдер.
    #### Текст для модулей KV в fixtures.kv"""
    def printText(self):
        self.ids.superScrollLabel.size_hint_y = 1
        return imageText
    # расчет значений
    def on_press_calculation(self,*args):
        self.superScrollLabel.text = ''
        SKM = self.startkm.text
        SM = self.startmeter.text
        FKM = self.finishkm.text
        FM = self.finishmeter.text
        lst = {} # для связки метража и возвышения
        data = [] # для добавления и реверса возвышений относительно метража
        try:
            if SKM and SM and FKM and FM:
                START = (int(SKM) * 1000 + int(SM))
                FINISH = (int(FKM) * 1000 + int(FM))
                reverseFlag = True
                if START > FINISH:  # вернет в FOR реверс если против хода километров
                    reverseFlag = False
                    START, FINISH = FINISH, START
                distance = FINISH - START
            #Блок проверки введенных значений
                if int(SKM) < 0 or int(SM) < 0 or int(FKM) < 0 or int(FM) < 0:
                    self.ids.superScrollLabel.size_hint_y = 1
                    self.superScrollLabel.text = f'{blueAzure}{sizeMax}Введите положительные значения'
                    return 0
                if int(SM) > 1000 or int(FM) > 1000:
                    self.ids.superScrollLabel.size_hint_y = 1
                    self.superScrollLabel.text = f'{orangeGeorgin}{sizeMax}В пикете 100 м!\n' \
                                                 f'В километре 10 пикетов, верно?'
                    return 0
                if distance > 1000 or int(self.elevation.text)<6:
                    self.ids.superScrollLabel.size_hint_y = 1
                    self.superScrollLabel.text = f'{aqua}{sizeMax}Может быть это прямая?'
                    return 0
                if int(self.elevation.text)>150:
                    self.ids.superScrollLabel.size_hint_y = 1
                    self.superScrollLabel.text = f'{red}{sizeMax}Эксплуатировать кривую с таким возвышением запрещено!'
                    return 0

            #END

            if self.elevation.text != 0 and self.graduation.text != 0:
                metr = START
                self.ids.superScrollLabel.size_hint_y = None
                self.dif = int(self.elevation.text)/int(distance)*int(self.graduation.text)
                self.formula = 0-self.dif
                self.superScrollLabel.text = f'{orange}Отвод возвышения равен: {lime}{round(self.dif/int(self.graduation.text),2)}{rgbClose} мм/м\n' \
                                             f'Длина переходной кривой: {redH}{distance}{rgbClose} метров.{rgbClose}\n\n'
                # Добавляем возвышение в список, который надо отсортировать в зависимости от положения начана Круговой кривой отностительно НПК
                for i in range(0,int(distance)+int(self.graduation.text), int(self.graduation.text)):
                    self.formula += self.dif
                    data.append(self.formula)

                for h in sorted(data,reverse=reverseFlag):
                    lst.setdefault(metr,int(h))
                    metr += int(self.graduation.text)

                for m,h in lst.items():
                    self.superScrollLabel.text += f'{yellow}{str(m)[:-3]} км {int(m)%1000} метр:{rgbClose} возвышение - {lime}{h}{rgbClose} мм\n'
        except Exception:
            self.ids.superScrollLabel.size_hint_y = 1
            self.superScrollLabel.text += ErrorCalculate


    def add_cleer(self, *args):
        """Очистка поля ввода при нажатии клавиши Очистить"""
        self.superScrollLabel.text = self.printText()
        self.startkm.hint_text = 'км'
        self.startkm.text = ''
        self.startmeter.text = ''
        self.startmeter.hint_text = 'м'
        self.finishkm.hint_text = 'км'
        self.finishmeter.hint_text = 'м'
        self.finishkm.text = ''
        self.finishmeter.text = ''
        self.graduation.text = ''
        self.elevation.text = ''

    def on_press_button_back(self, *args):
        """
        возврат в главное меню
        """
        self.manager.transition.direction = 'right'
        self.manager.current = 'NewTitleScreen'
class Straightening(Screen):
    """
    Расчет стрел изгиба в переводной и круговой кривой
    #### Текст для модулей KV в fixtures.kv
    """
    def printText(self):
        self.ids.superScrollLabel.size_hint_y = 1
        return straightening
    # расчет значений
    def print_result(self):
        self.superScrollLabel.text = ''
        SKM = self.startkm.text
        SM = self.startmeter.text
        FKM = self.finishkm.text
        FM = self.finishmeter.text

        graduation = self.graduation.text
        lst = {}  # для связки метража и возвышения
        data = []  # для добавления и реверса возвышений относительно метража
        try:
            if SKM and SM and FKM and FM:
                START = (int(SKM) * 1000 + int(SM))
                FINISH = (int(FKM) * 1000 + int(FM))
                reverseFlag = True
                if START > FINISH:  # вернет в FOR реверс если против хода километров
                    reverseFlag = False
                    START, FINISH = FINISH, START
                distance = FINISH - START
                metr = START
            if self.chord.text !=0 and self.radius.text!=0 and self.graduation.text!=0 and distance!=0:
                self.ids.superScrollLabel.size_hint_y = None
                self.arrowСircle = (1000*int(self.chord.text)**2)/(8*int(self.radius.text))# Стрела изгиба круговой кривой
                self.superScrollLabel.text = f'{orange}Расчетная стрела изгиба круговой кривой:{lime}\n{round(self.arrowСircle,2)}{rgbClose} мм\n' \
                                             f'Длина переходной кривой: {redH}{distance}{rgbClose} м\n' \
                                             f'Расчетные стрелы изгиба переходной кривой равны:{rgbClose}\n\n'
                self.formula = 0
                for i in range(0,int(distance)+int(graduation), int(graduation)):
                    self.formula = self.arrowСircle * i /int(distance)
                    data.append(self.formula)
                for h in sorted(data, reverse=reverseFlag):
                    lst.setdefault(metr, int(h))
                    metr += int(self.graduation.text)
                for m, h in lst.items():
                    self.superScrollLabel.text += f'{yellow}{str(m)[:-3]} км {int(m) % 1000} метр:{rgbClose} стрела изгиба- {lime}{h}{rgbClose} мм\n'
                    #self.superScrollLabel.text += f'{yellow}{str(i)} метр:{rgbClose} стрела изгиба- {lime}{int(self.formula)}{rgbClose} мм\n'
        except Exception:
            self.ids.superScrollLabel.size_hint_y = 1
            self.superScrollLabel.text = ErrorCalculate


    def on_press_calculation(self, *args):
        """

        :param args: Обрабатывает нажатие клавиши Расчет. Принимает 3 числа.
        :return: True - передает в функцию print_result результат расчета формулы итоговое удлинение плети
        """
        if self.chord.text and self.radius.text and self.graduation.text:
            self.print_result()
        else:
            self.superScrollLabel.text = f'{sizeA}{orange}Введите не нулевые значения{rgbClose}{sizeClose}'

    def add_cleer(self, *args):
        """Очистка поля ввода при нажатии клавиши Очистить"""
        self.superScrollLabel.text = self.printText()
        self.chord.text = '20' # хорда
        self.radius.text = '' # Радиус круговой кривой
        self.graduation.text = '' # Градация
        self.startkm.hint_text = 'км'
        self.startkm.text = ''
        self.startmeter.text = ''
        self.startmeter.hint_text = 'м'
        self.finishkm.hint_text = 'км'
        self.finishmeter.hint_text = 'м'
        self.finishkm.text = ''
        self.finishmeter.text = ''
        # Длина переходной кривой
    def on_press_button_back(self, *args):
        """
        возврат в главное меню
        """
        self.manager.transition.direction = 'right'
        self.manager.current = 'NewTitleScreen'
class NotAcceleration(Screen):
    """Расчет не погашенного ускорения в кривой"""
    def on_press_calculation(self,*args):
        self.ids.superScrollLabel.size_hint_y = 1
        try:
            if self.speed.text and self.radius.text and self.rise.text:
                self.formula = f'{orange}Величина поперечного непогашенного ускорения Анп: \n' \
                               f'{lime}{round(((int(self.speed.text)**2)/(13*int(self.radius.text)) - 0.0061*int(self.rise.text)),2)}{rgbClose} м/с²{rgbClose}'
                self.superScrollLabel.text = self.formula
                print(self.formula)
            else:
                self.formula = f'{red}Введите данные!{rgbClose}'
            self.superScrollLabel.text = self.formula
        except Exception:
            self.superScrollLabel.text = ErrorCalculate
    def add_cleer(self,*args):
        self.ids.superScrollLabel.size_hint_y = None
        self.superScrollLabel.text = notaccelerationText
        self.speed.text = ''
        self.radius.text = ''
        self.rise.text = ''
    def on_press_button_back(self, *args):
        """возврат в главное меню"""
        self.manager.transition.direction = 'right'
        self.manager.current = 'NewTitleScreen'

class HandBook(Screen):
    "справочник #### Текст для модулей KV в fixtures.kv"
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # подключен модуль ScrollClass + scrollscreen.kv!
        bx=BoxLayout(orientation = 'vertical')
        bx.add_widget(ScrollScreenApp().get_Screen())
        bx.add_widget(RoundedButton(on_release = self.on_press_button_bac,text = 'В главное меню'))
        self.add_widget(bx)

    def on_press_button_bac(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'NewTitleScreen'

class AboutProgram(Screen):
    """Выводит информацию о программе #### Текст для модулей KV в fixtures.kv"""

    def on_press_button_back(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'NewTitleScreen'

# Главный родительский класс
class PaswordingApp(App):
    """ГЛАВНЫЙ КОРНЕВОЙ КЛАСС"""
    def build(self):

        sm = ScreenManager()
        sm.add_widget(NewTitleScreen(name='NewTitleScreen'))
        sm.add_widget(Ballcalculator(name = 'Ballcalculator'))
        sm.add_widget(ActualTemperature(name ='ActualTemperature'))
        sm.add_widget(WlipCalculator(name='WlipCalculator'))
        sm.add_widget(Imagekv(name = 'Imagekv'))
        sm.add_widget(Straightening(name = 'Straightening'))
        sm.add_widget(NotAcceleration(name = 'NotAcceleration'))
        sm.add_widget(HandBook(name='HandBook'))
        sm.add_widget(AboutProgram(name='AboutProgram'))
        return sm


if __name__ == "__main__":
    PaswordingApp().run()

