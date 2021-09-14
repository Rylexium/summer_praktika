import kivy
kivy.require('1.0.7')

from kivy.app import App

class CaleApp(App):
    pass


class CaleApp2(App):
    def build(self):
        return CaleApp()

if __name__ == '__main__':
    CaleApp().run()