from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty

class Demo(GridLayout):
    name = ObjectProperty(None)
    age = ObjectProperty(None)

    def on_click (self):
        print("My name is {} and I am {} year old".format(self.name.text,self.age.text))
        
        self.name.text = ""
        self.age.text = ""

class MyFirstApp(App):
    def build(self):
        return Demo()

MyFirstApp().run()