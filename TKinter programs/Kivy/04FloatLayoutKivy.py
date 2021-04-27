from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

class Float_layout_Demo(FloatLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        self.btn1 = Button(
            text = "Click Me",
            size_hint = (0.4,0.4),
            pos_hint = {"x":0.3,"y":0.2}
        )
        self.add_widget(self.btn1)

        self.btn2 = Button(
            text = "Button 2",
            size_hint = (0.2,0.1),
            pos_hint = {"x":0.7,"y":0.7} 
        )
        self.add_widget(self.btn2)


class DemoApp(App):
    def build(self):
        return Float_layout_Demo()

DemoApp().run()