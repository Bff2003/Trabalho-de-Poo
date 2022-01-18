from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class LoginScreen(GridLayout):

    def __init__(self, **kargs):
        super().__init__(**kargs)
        self.cols = 1

        # 1, 1
        self.lbl = Label(text='')
        self.add_widget(self.lbl)

        # 1, 2
        self.txt_input_nome = TextInput(multiline=False)
        self.txt_input_nome.bind(text=self.valida)
        self.add_widget(self.txt_input_nome)

    
        # 2, 2
        self.txt_input_pw = TextInput(multiline=False)
        self.txt_input_pw.bind(text=self.valida)
        self.add_widget(self.txt_input_pw)
    def valida(self, instance, value):
        if self.txt_input_nome.text[::-1] == self.txt_input_pw.text:
            self.lbl.color = [0, 1, 0, 1] 
            self.lbl.text = "Textos inversos"
        else :
            self.lbl.text = "Textos não inversos"
            self.lbl.color = [1, 0, 0, 1]


class MyApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()