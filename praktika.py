import kivy
from kivy.lang import Builder
kivy.require('1.0.7')

from kivy.app import App
kvfile = Builder.load_string("""
#:kivy 1.0

BoxLayout:
    orientation:'vertical'
    number:0

    Label:
        id:monitor
        font_size:60
        text: ""

    BoxLayout:
        orientation:'vertical'
        GridLayout:
            size_hint_y:0.2
            cols:2
            Button:
                text:"("
                on_release: monitor.text += self.text
            Button:
                text:")"
                on_release: monitor.text += self.text
        GridLayout:
            cols:4
            Button:
                text:"C"
                on_release: monitor.text = ""
            Button:
                text:"/"
                on_release: monitor.text += self.text
            Button:
                text:"*"
                on_release: monitor.text += self.text
            Button:
                text:"<-"
                on_release: monitor.text = monitor.text[:len(monitor.text)-1:]
            Button:
                text:"7"
                on_release: monitor.text += self.text
            Button:
                text:"8"
                on_release: monitor.text += self.text
            Button:
                text:"9"
                on_release: monitor.text += self.text
            Button:
                text:"-"
                on_release: monitor.text += self.text
            Button:
                text:"4"
                on_release: monitor.text += self.text
            Button:
                text:"5"
                on_release: monitor.text += self.text
            Button:
                text:"6"
                on_release: monitor.text += self.text
            Button:
                text:"+"
                on_release: monitor.text += self.text
            Button:
                text:"1"
                on_release: monitor.text += self.text
            Button:
                text: '2'
                on_release: monitor.text += self.text
            Button:
                text: '3'
                on_release: monitor.text += self.text
            Button:
                text: '='
                on_press:
                    try:monitor.text = str(eval(monitor.text))
                    except:pass
            Label:
                text:''
            Button:
                text:'0'
                on_release: monitor.text += self.text
            Button:
                text:'.'
                on_release: monitor.text += self.text
""")


class CaleApp2(App):
    def build(self):
        return kvfile

if __name__ == '__main__':
    CaleApp2().run()