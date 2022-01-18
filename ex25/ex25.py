class Exception (BaseException):

    def __init__(self, message) -> None:
        self.message = message

    def __repr__(self) -> str:
        return self.message
    
    pass

class AnoInvalido(Exception):
    def __init__(self, message, codigo = 0):
        self.message = message
        self.codigo = codigo
    def __repr__(self) -> str:
        # return super().__repr__()
        return (f"Erro: {self.message}\nCode: {self.codigo}")
class MesInvalido(Exception):
    def __init__(self, message, codigo = 0):
        self.message = message
        self.codigo = codigo
    def __repr__(self) -> str:
        return (f"Erro: {self.message}\nCode: {self.codigo}")
class DiaInvalido(Exception):
    def __init__(self, message, codigo = 0):
        self.message = message
        self.codigo = codigo
    def __repr__(self) -> str:
        # return super().__repr__()
        return (f"Erro: {self.message}\nCode: {self.codigo}")


class Data :
    """ classe que implementa o armazenamento de uma data .
    Se for instanciada com valores invalidos levanta uma excecao """
    def __init__ (self, a, m, d):
        Data.valida(a, m, d) # levanta excecao em caso de erro
        self.a, self.m, self.d = a, m, d
    def __repr__ (self):
        return f'{ self .a }/{ self .m }/{ self .d}'
    @staticmethod
    def valida (a, m, d):
        ''' devolve True se a data e a/m/d valida . Caso contrario levante uma excecao adequada
        raises :
        TypeError : se os valores a, m ou d nao forem inteiros , indicando qual
        AnoInvalido : Nao existe ano 0 ( xxx excecao a ser implementada pelo aluno xxxx )
        MesInvalido : se m < 1 ou m > 12
        DiaInvalido : o mes m nao tem dia d
        '''
        if(type(d) != int): raise DiaInvalido("O dia '{a}' não é um valor do tipo int")
        if(type(m) != int): raise MesInvalido(f"O mes '{a}' não é um valor do tipo int")
        if(type(a) != int): raise AnoInvalido(f"O ano '{a}' não é um valor do tipo int")

        if(a < 0): raise AnoInvalido(f"O ano {a} é invalido!")
        if (m < 1 or m > 12): raise MesInvalido(f"O mes {m} é invalido!")

        b = False

        # regra de https://pt.wikihow.com/Descobrir-se-um-Ano-%C3%A9-Bissexto
        if(a % 4 == 0 and a % 100 != 0): # bissexto (tem 366 dias)
            b = True
        elif(a % 4 == 0 and a % 100 == 0 and a % 400 == 0):
            b = True
        
        meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if(m == 2 and b == False):
            if not (d <= 28 and d >= 1): raise DiaInvalido("Esse mes tem apenas 28 dias")
        elif(m == 2 and b == True):
            if not (d <= 29 and d >= 1): raise DiaInvalido("Esse mes tem apenas 29 dias")
        else:
            if not (d <= meses[m-1] and d >= 0): raise DiaInvalido(f"Esse mes tem apenas {meses[m-1]} dias")
        
            

# data=Data("2000",1,1)
try:
    data=Data(2000,1,1)
    data=Data(2000,12,32)
except (DiaInvalido, MesInvalido, AnoInvalido) as e:
    print(e)
# data=Data("2000",1,1)