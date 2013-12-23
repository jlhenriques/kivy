"""
Aprendendo Kivy

Seguindo o tutorial de Alexander Taylor no YouTube:
https://www.youtube.com/watch?v=F7UKmK9eQLY
"""

from kivy.app import App
from kivy.uix.button import Button

class OiApp(App):
	def build(self):
		return Button(text='Oi!',
					  background_color=(0, 0, 1, 1),
					  font_size=150)

if __name__=='__main__':
	OiApp().run()
