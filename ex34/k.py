from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.checkbox import CheckBox 
import random


class LoginScreen(GridLayout):

    def __init__(self, **kargs):
        super().__init__(**kargs)
        self.cols = 2
        self.numero = random.randint(1, 100)

        # Label
        self.lbl = Label(text="Adivinha o Numero")
        self.add_widget(self.lbl)

        # Caixa de texto
        self.txt_1 = TextInput(multiline=False, text=len(str(self.numero))* "*")
        self.add_widget(self.txt_1)

        # Caixa de texto
        self.txt_2 = TextInput(multiline=False, text="0")
        self.add_widget(self.txt_2)
        
        # Botão
        self.btn = Button(text='Verifica!')
        self.add_widget(self.btn)
        self.btn.bind(on_release=self.bt_release)
    def bt_release(self, value):
        if(self.txt_2.text.isdigit()):
            if(int(self.txt_2.text) > self.numero):
                self.lbl.text = "tenta um valor menor"
            elif(int(self.txt_2.text) < self.numero):
                self.lbl.text = "tenta um valor maior"
            elif(int(self.txt_2.text) == self.numero):
                self.lbl.text = "acertaste"
                self.txt_1.text = str(self.numero)

class MyApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()