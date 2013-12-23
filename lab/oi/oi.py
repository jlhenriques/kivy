# coding: utf-8

"""
Aprendendo Kivy

Seguindo o tutorial de Alexander Taylor no YouTube:
https://www.youtube.com/watch?v=F7UKmK9eQLY
"""

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout

class OiApp(App):
    def build(self):
        f = FloatLayout()
        s = Scatter()
        l = Label(text='Hello!',
                  font_size=150)
        f.add_widget(s)
        s.add_widget(l)
        return f

if __name__=='__main__':
    OiApp().run()
