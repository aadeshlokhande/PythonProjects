from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.uix.button import Button

class Page_Layout_Demo(PageLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.btn1 = Button(
            text = "Button 1"
        )
        self.add_widget(self.btn1)

        self.btn2 = Button(
            text = "Button 2"
        )
        self.add_widget(self.btn2)

        self.btn3 = Button(
            text = "Button 3"
        )
        self.add_widget(self.btn3)

class DemoApp(App):
    def build(self):
        return Page_Layout_Demo()

DemoApp().run()