from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label



class Grid_Layout_Demo(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rows = 2
        self.cols = 1

        self.l1 = Label(
            text = "click the Button"
        )
        self.add_widget(self.l1)

        self.btn1 = Button(
            text = "Click Me",
            background_color = (44,53,0,1),
            color = (0,0,0,1)
        )
        self.add_widget(self.btn1)


class DemoApp(App):
    def build(self):
        return Grid_Layout_Demo()

DemoApp().run()


