import sqlite3
import os
# from abc import abstractclassmethod, abstractproperty, abstractmethod, abstractstaticmethod
from tabulate import tabulate

def limparPasta(dir):
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))

def verde(texto):
    return("\033[1;32;40m"+texto+"\033[0;37;40m")

class Database():
    def __init__(self, database: str, AUTO_CONNECT : bool = True) -> None:
        self.database = database
        if(os.path.isfile(database) == False):
            raise FileNotFoundError("O arquivo não foi encontrado!")
        if(AUTO_CONNECT == True):
            self.conectar()

    def numberOfFilesInFolder(self, pasta):
        totalFiles = 0
        totalDir = 0

        for base, dirs, files in os.walk(pasta):
            for directories in dirs:
                totalDir += 1
            for Files in files:
                totalFiles += 1
        return totalFiles

    def conectar(self) -> None:
        try:
            self.conn = sqlite3.connect(self.database)
            self.cursor = self.conn.cursor()
        except:
            print("Nao possível ligar ao servidor sqlite")
            exit()
        print("Conectado!")
    
    def consulta_SELECT(self, query: str):
        self.cursor.execute(query)
        valores = self.cursor.fetchall()
        if(len(valores) == 0):
            # print("Não ha valores a mostrar!")
            print(verde("Query")+f": {query}\n"+verde("Resposta")+f": Não ha valores a mostrar!\n")
        else:
            tabela = tabulate(valores, showindex=True)
            l = self.numberOfFilesInFolder("./results/") + 1
            f = open("./results/"+str(l)+".txt", "w")
            f.writelines(tabela)
            f.close()
            print(verde("Query")+f": {query}\n"+verde("Resposta")+f": achados {len(valores)} linhas\n"+verde("Guardado")+f": {str(l)}.txt\n")
            return valores
    
    def consulta(self, query: str, data = None):
        if(data == None):
            self.cursor.execute(query)
        elif(data != None):
            self.cursor.execute(query, data)
        print(verde("Query")+f": {query}\n"+verde("Resposta")+f": Consulta executada com sucesso!\n")
        self.conn.commit()

    
db = Database("adamastor.db")

limparPasta("./results/")

# I
db.consulta_SELECT("Select CódigoDoProduto, NomeDoProduto from produtos order by PreçoUnitário")
# II
db.consulta_SELECT("Select CódigoDoProduto, NomeDoProduto from produtos where Existências < 10")
# V
db.consulta_SELECT("Select CódigoDoProduto, NomeDoProduto from produtos where Existências < 10 and UnidadesEncomendadas = 0")
# IX apresente uma listagem de produtos com os respetivos fornecedores.
db.consulta_SELECT("select NomeDoProduto, NomeDaEmpresa from  produtos inner join fornecedores on CódigoDoProduto = CódigoDoProduto;")
# XII apresente uma listagem das datas das encomendas efetuadas por “Hanari Carnes”.
db.consulta_SELECT("select DataDaEncomenda from encomendas inner join clientes on encomendas.CódigoDoCliente = clientes.CódigoDoCliente where NomeDaEmpresa = 'Hanari Carnes';")
# XIV apresente uma listagem dos empregados que trataram de encomendas feitas por “Hanari Carnes”.
db.consulta_SELECT("select Nome, Apelido from empregados inner join encomendas on empregados.CódigoDoEmpregado = encomendas.CódigoDoEmpregado inner join clientes on encomendas.CódigoDoCliente = clientes.CódigoDoCliente where NomeDaEmpresa = 'Hanari Carnes';")
# (xx) Alterar o número de unidades em stock para as existentes mais as encomendadas nos produtos do fornecedor com id 1 e colocar as encomendadas feitas a este a 0
db.consulta("UPDATE produtos SET Existências = UnidadesEncomendadas + Existências, UnidadesEncomendadas = 0 where CódigoDoFornecedor = 1")
# (xxiv) Inserir um novo funcionário (invente os dados necessários).
db.consulta('''INSERT INTO empregados 
            (Apelido, Nome, Cargo, TítuloDeCortesia, Endereço, Cidade, CódigoPostal, País, Telefone)
             VALUES ("Louis", "Joao", "Operario", "aa", "a", "a", "a", "a", "a")''')

# (xxxi) Quais as cidades que têm fornecedores (devolver o resultado todos em maiúsculas)?
db.consulta_SELECT("select UPPER(Cidade) from fornecedores where Cidade not null group by UPPER(Cidade) order by UPPER(Cidade);")
# (xxxv) Qual a maior encomenda em termos de número de itens?
db.consulta_SELECT("select CódigoDaEncomenda, SUM(Quantidade) from detalhes_da_encomenda group by CódigoDaEncomenda order by SUM(Quantidade) desc limit 1;")