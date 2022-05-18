from tkinter import Label

from kivy.app import App
from kivy.uix.recycleview import RecycleView
import kivy.app
import kivy.uix.label


class TestApp(kivy.app.App):
    def build(self):
        return kivy.uix.label.Label(text="Hello World")


app = TestApp(title="Hello")
app.run()


#class WeatherApp(App):
 #   pass


#if __name__ == '__main__':
 #   WeatherApp().run()


