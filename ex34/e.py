from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class LoginScreen(GridLayout):

    def __init__(self, **kargs):
        super().__init__(**kargs)
        self.cols = 2

        # 1, 2
        self.txt_esquerda = TextInput(multiline=False)
        self.add_widget(self.txt_esquerda)
    
        # 2, 2
        self.txt_direita = TextInput(multiline=False)
        self.add_widget(self.txt_direita)

        # 1, 1
        self.btn = Button(text='Botão')
        self.add_widget(self.btn)

        self.btn.bind(on_release=self.bt_release)
    def bt_release(self, value):
        temp = self.txt_esquerda.text
        self.txt_esquerda.text = self.txt_direita.text
        self.txt_direita.text = temp

class MyApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()