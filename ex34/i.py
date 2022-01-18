from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.checkbox import CheckBox 


class LoginScreen(GridLayout):

    def __init__(self, **kargs):
        super().__init__(**kargs)
        self.cols = 2

        # Label
        self.txt_input_nome = Label(text="Contador")
        self.add_widget(self.txt_input_nome)
    
        # Ckeckbox
        self.checkbox = CheckBox()
        self.add_widget(self.checkbox)

        # Caixa de texto
        self.txt_input_pw = TextInput(multiline=False, text="0")
        self.add_widget(self.txt_input_pw)
        
        # Botão
        self.btn = Button(text='Clique Aqui!')
        self.add_widget(self.btn)
        self.btn.bind(on_release=self.bt_release)
    def bt_release(self, value):
        if(self.checkbox.active == False):
            self.txt_input_pw.text = str(int(self.txt_input_pw.text) + 1)
        else:
            self.txt_input_pw.text = str(int(self.txt_input_pw.text) - 1)

class MyApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()