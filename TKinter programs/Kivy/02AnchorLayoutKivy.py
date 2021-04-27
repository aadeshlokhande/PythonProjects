from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button

class DemoApp(App):
    def build(self):
        layout = AnchorLayout(
            anchor_x = 'left', anchor_y = 'top'
        )
        btn1 = Button(
            text = "Anchor layout Demo",
            size_hint = (.2,.2),
            background_color = (0.0,25.32,0,1),
            color = (0,0,0,1)
        )
        layout.add_widget(btn1)
        return layout

DemoApp().run()