from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        bl = BoxLayout()
        btn1 = Button(text = "Aadesh")
        btn2 = Button(text = "Lokhande")
        bl.add_widget(btn1)
        bl.add_widget(btn2)
        return bl 

if __name__ == '__main__':
    MyApp().run()
    