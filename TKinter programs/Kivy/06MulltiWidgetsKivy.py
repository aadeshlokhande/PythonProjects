from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput


class Kivy_UI(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.rows = 4

        self.img = Image(
            source = "python.png"
        )
        self.add_widget(self.img)


        self.lbl = Label(
            text = "Enter your name"
        )
        self.add_widget(self.lbl)

        self.txt = TextInput(
            text = "",
            font_size = 40
        )
        self.add_widget(self.txt)

        self.btn = Button(
            text = "Submit"

        )
        self.btn.bind(on_press = self.call_back)
        self.add_widget(self.btn)


        self.pop = Popup(
            title = "Aadesh lokhande",
            size_hint = (None,None),
            size = (400,400),
            content = Label(
                text = ""
            )
        )

    def call_back(self,elem):
        self.pop.content.text = self.txt.text
        self.pop.open()



class AadeshApp(App):
    def build(self):
        return Kivy_UI()

AadeshApp().run()
