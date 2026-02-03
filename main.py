from kivy.app import App
from kivy.uix.label import Label

class OrszemApp(App):
    def build(self):
        return Label(text='Az Orszem figyel!')

if __name__ == '__main__':
    OrszemApp().run()
  
