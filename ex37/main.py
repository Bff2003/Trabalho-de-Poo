from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
import random


class LoginScreen(GridLayout):

    def __init__(self, **kargs):
        super().__init__(**kargs)

        self.wins = [0, 0]
        self.i = 1

        self.jogo = [
            [Button(text=''), Button(text=''), Button(text='')],
            [Button(text=''), Button(text=''), Button(text='')],
            [Button(text=''), Button(text=''), Button(text='')]
        ]

        self.cols = 3

        # Label
        self.lbl_p1 = Label(text="Jogador 1: " + str(self.wins[0]))
        self.add_widget(self.lbl_p1)
        # Label
        self.lbl1 = Label(text="")
        self.add_widget(self.lbl1)
        # Label
        self.lbl_p2 = Label(text="Jogador 2: " + str(self.wins[1]))
        self.add_widget(self.lbl_p2)

        for linha in self.jogo:
            for casa in linha:
                self.add_widget(casa)
                casa.bind(on_release=self.bt_release)

        # Label
        self.lbl_f = Label(text="")
        self.add_widget(self.lbl_f)
        # Label
        self.lbl_f1 = Label(text="")
        self.add_widget(self.lbl_f1)
        # Label
        self.lbl_f2 = Label(text="")
        self.add_widget(self.lbl_f2)

    def bt_release(self, value):
        a_colocar = ""
        if(self.i % 2 == 0):
            a_colocar = "O"
        elif(self.i % 2 != 0):
            a_colocar = "X"
        if(value.text == ""):
            value.text = a_colocar
            self.i = self.i + 1
        self.valida()
        if(self.wins[0] == 3 or self.wins[1] == 3):
            if(self.wins[0] == 3):
                self.lbl_p1.color = [0, 1, 0, 1]
                self.lbl_p2.color = [1, 0, 0, 1]
            elif(self.wins[1] == 3):
                self.lbl_p2.color = [0, 1, 0, 1]
                self.lbl_p1.color = [1, 0, 0, 1]
            self.desativaButoes()

    def desativaButoes(self):
        for linha in self.jogo:
            for casa in linha:
                casa.set_disabled(True)

    def valida(self):  # valida casos todos
        try:
            # posicao 00
            self.verificaJogador(
                self.jogo[0][0].text, self.jogo[0][1].text, self.jogo[0][2].text)
            self.verificaJogador(
                self.jogo[0][0].text, self.jogo[1][0].text, self.jogo[2][0].text)
            self.verificaJogador(
                self.jogo[0][0].text, self.jogo[1][1].text, self.jogo[2][2].text)
            # posicao 02
            self.verificaJogador(
                self.jogo[0][2].text, self.jogo[1][2].text, self.jogo[2][2].text)
            self.verificaJogador(
                self.jogo[0][2].text, self.jogo[1][1].text, self.jogo[2][0].text)
            # posicao 20
            self.verificaJogador(
                self.jogo[2][0].text, self.jogo[2][1].text, self.jogo[2][2].text)

            # Meio
            self.verificaJogador(
                self.jogo[1][0].text, self.jogo[1][1].text, self.jogo[1][2].text)
            self.verificaJogador(
                self.jogo[0][1].text, self.jogo[1][1].text, self.jogo[2][1].text)

            if(self.contaPreenchidos() == 9):
                raise Exception("Nenhum Jogador Ganhou!")
        except Exception as e:
            if(e.args[0] == "X"):
                self.wins[0] = self.wins[0] + 1
                self.lbl_p1.text = "Jogador 1: " + str(self.wins[0])
            elif(e.args[0] == "O"):
                self.wins[1] = self.wins[1] + 1
                self.lbl_p2.text = "Jogador 2: " + str(self.wins[1])

            self.LimpaJogo()
            self.i = 1

        # verifica se ninguem ganhou
        pass

    def LimpaJogo(self):
        for linha in self.jogo:
            for casa in linha:
                casa.text = ""

    def verificaJogador(self, posicao1, posicao2, posicao3):  # retorna jogador que ganhou
        # if(posicao1 == posicao2 and posicao2 == posicao3 or posicao4 == posicao5 and posicao5 == posicao6):
        if(posicao1 == posicao2 and posicao2 == posicao3 and posicao1 != ""):
            raise Exception(str(posicao1))
        else:
            return 0

    def contaPreenchidos(self):  # conta todas as casa ja preenchidas
        i = 0
        for linha in self.jogo:
            for casa in linha:
                if(casa.text != ""):
                    i = i + 1
        return i


class MyApp(App):
    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()
