from kivy.uix.button import Button
from kivy.lang import Builder

kv="""
<RoundedButton@Button>:
    size_hint:1,None
    size:0,100
    background_color: 0,0,0,0 
    canvas.before:
        Color:
            rgba: fix.colorButtonBack if self.state=='normal' else (1,.7,.7,1)  # visual feedback of press
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [30,]

"""
class RoundedButton(Button):
    """Описывает отдельную кнопку возврата из Справочника в основное МЕНЮ"""
    Builder.load_string(kv)

