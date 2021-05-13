from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

Window.size = (500,700)



class Telas(ScreenManager):
    pass

class Menu(Screen):
    pass

class Op1(Screen):
   pass

class Op2(Screen):
    pass

class Op3(Screen):
    pass

class Op4(Screen):
    pass

class Op5(Screen):
    pass


class Final(Screen):
    pass


class Teste(App):
    def build(self):

        return Telas()


Teste().run()
