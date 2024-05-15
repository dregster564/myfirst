'''для добавления новой шпаргалки 1*добавить данные в ScrollClass.py - ScreenMain(),
2*ScrollClass.py - ScrollScreenApp(),3*ScrollClass.py - Новый класс шпоры(),4*fixtures.py(переменная текст шпоры),
5*passwording.kv(Имя нового класса и переменная с текстом из fixtures.py, 6*создать кнопку в scrollscreen.kv с названием новой шпаргалки)
'''
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
Builder.load_file('scrollscreen.kv')

class ScreenMain(Screen):
    """Содержит функции вызова подклассов на главном экране СПРАВОЧНИКА scrollscreen.kv!!!!!"""

    def on_press_button_Ball(self, *args):
        """Балловая оценка"""
        self.manager.transition.direction = 'left'
        self.manager.current = 'Ball'
    def on_press_button_Rails(self, *args):
        """Рельсовое хозайство"""
        self.manager.transition.direction = 'left'
        self.manager.current = 'Rails'
    def on_press_button_Sleepers(self, *args):
        """Шпальное хозяйство"""
        self.manager.transition.direction = 'left'
        self.manager.current = 'Sleepers'
    def on_press_button_Ballast(self, *args):
        """Балласт, балластная призма, земляное полотно"""
        self.manager.transition.direction = 'left'
        self.manager.current = 'Ballast'
    def on_press_button_Overall_size(self, *args):
        """Габарит"""
        self.manager.transition.direction = 'left'
        self.manager.current = 'OverallSize'
    def on_press_button_Fence(self, *args):
        """Сигналы, сигнальные и путевые знаки, устройства путевого заграждения"""
        self.manager.transition.direction = 'left'
        self.manager.current = 'Fence'
    def on_press_button_Crossing(self, *args):
        """Сигналы, сигнальные и путевые знаки, устройства путевого заграждения"""
        self.manager.transition.direction = 'left'
        self.manager.current = 'Crossing'
    def on_press_button_Arrow_switches(self, *args):
        """Стрелочные переводы содержание"""
        self.manager.transition.direction = 'left'
        self.manager.current = 'ArrowSwitchese'

    def on_press_button_Pattern_switches(self, *args):
        """Стрелочные переводы нормы по ширине колеи"""
        self.manager.transition.direction = 'left'
        self.manager.current = 'PatternSwitchese'

    def on_press_button_Gutters_switches(self, *args):
        """Стрелочные переводы нормы по ширине колеи"""
        self.manager.transition.direction = 'left'
        self.manager.current = 'GuttersSwitchese'

    def on_press_button_Ordinates_switches(self, *args):
        """Стрелочные переводы нормы по ширине колеи"""
        self.manager.transition.direction = 'left'
        self.manager.current = 'OrdinatesSwitchese'

    def on_press_button_Polishing_wits(self, *args):
        """Шлифовка остряков"""
        self.manager.transition.direction = 'left'
        self.manager.current = 'PolishingWits'
    def on_press_button_Wear_switches(self, *args):
        """Стрелочные переводы износы"""
        self.manager.transition.direction = 'left'
        self.manager.current = 'WearSwitches'
    def on_press_button_Rail_chains(self, *args):
        """Рельсовые цепи"""
        self.manager.transition.direction = 'left'
        self.manager.current = 'RailChains'
class Ball(Screen):
    """
    ScrollClass.py + PASSWORDING.KV + scrollscreen.kv
    """
    def on_press_button_back(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'main_screen'
class Rails(Screen):
    """
    ScrollClass.py + PASSWORDING.KV + scrollscreen.kv
    """
    def on_press_button_back(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'main_screen'
class Sleepers(Screen):
    """
    ScrollClass.py + PASSWORDING.KV + scrollscreen.kv
    """
    def on_press_button_back(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'main_screen'
class Ballast(Screen):
    """
    ScrollClass.py + PASSWORDING.KV + scrollscreen.kv
    """
    def on_press_button_back(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'main_screen'
class OverallSize(Screen):
    """
    ScrollClass.py + PASSWORDING.KV + scrollscreen.kv
    """
    def on_press_button_back(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'main_screen'
class Fence(Screen):
    """
    ScrollClass.py + PASSWORDING.KV + scrollscreen.kv
    """
    def on_press_button_back(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'main_screen'

class Crossing(Screen):
    """Жд переезды"""

    def on_press_button_back(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'main_screen'
class ArrowSwitchese(Screen):
    """
    Стрелочные переводы содержание общие положения
    ScrollClass.py + PASSWORDING.KV + scrollscreen.kv
    """
    def on_press_button_back(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'main_screen'
class PatternSwitchese(Screen):
    """
    Стрелочные переводы содержание по ШАБЛОНУ
    ScrollClass.py + PASSWORDING.KV + scrollscreen.kv
    """
    def on_press_button_back(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'main_screen'
class GuttersSwitchese(Screen):
    """
    Стрелочные переводы содержание по ЖЕЛОБАМ
    ScrollClass.py + PASSWORDING.KV + scrollscreen.kv
    """
    def on_press_button_back(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'main_screen'
class OrdinatesSwitchese(Screen):
    """
    Стрелочные переводы содержание по ОРДИНАТАМ
    ScrollClass.py + PASSWORDING.KV + scrollscreen.kv
    """
    def on_press_button_back(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'main_screen'

class PolishingWits(Screen):
    """
    Шлифовка остряков
    ScrollClass.py + PASSWORDING.KV + scrollscreen.kv
    """
    def on_press_button_back(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'main_screen'
class WearSwitches(Screen):
    """
    Стрелочные переводы износы
    ScrollClass.py + PASSWORDING.KV + scrollscreen.kv
    """
    def on_press_button_back(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'main_screen'
class RailChains(Screen):
    """
    ScrollClass.py + PASSWORDING.KV + scrollscreen.kv
    """
    def on_press_button_back(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'main_screen'


class ScrollScreenApp(App):
    '''Содержание справочника (КНОПКИ ВЫЗОВА).
    для добавления новой шпаргалки 1*добавить данные в ScrollClass.py - ScreenMain(),
    2*ScrollClass.py - ScrollScreenApp(),3*ScrollClass.py - Новый класс шпоры(),4*fixtures.py(переменная текст шпоры),
    5*passwording.kv(Имя нового класса и переменная с текстом из fixtures.py, 6*создать кнопку в scrollscreen.kv с названием новой шпаргалки)
    '''
    def get_Screen(self):
        scr = ScreenManager()
        scr.add_widget(ScreenMain(name='main_screen'))
        scr.add_widget(Ball(name='Ball'))
        scr.add_widget(Rails(name='Rails'))
        scr.add_widget(Sleepers(name='Sleepers'))
        scr.add_widget(Ballast(name='Ballast'))
        scr.add_widget(OverallSize(name='OverallSize'))
        scr.add_widget(Fence(name='Fence'))
        scr.add_widget(Crossing(name='Crossing'))
        scr.add_widget(ArrowSwitchese(name='ArrowSwitchese'))
        scr.add_widget(PatternSwitchese(name='PatternSwitchese'))
        scr.add_widget(GuttersSwitchese(name='GuttersSwitchese'))
        scr.add_widget(OrdinatesSwitchese(name='OrdinatesSwitchese'))
        scr.add_widget(PolishingWits(name='PolishingWits'))
        scr.add_widget(WearSwitches(name='WearSwitches'))
        scr.add_widget(RailChains(name='RailChains'))
        return scr
