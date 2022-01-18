import requests

uri = "http://127.0.0.1:8080"

def getAll():
    print("---- GET ------------------------------------------")
    print("without ID")
    response = requests.get(uri + '/reading/')
    print(response.text)

def get(idReading: str):
    print("---- GET ------------------------------------------")
    print("with ID")
    response = requests.get(uri + '/reading/'+ idReading)
    print(response.text)

def post(idSensor: str ="5", tomestamp: str = "2213432", value: str = "33" ):
    print("---- POST ------------------------------------------")
    response = requests.post(uri+ '/reading/', json={
            'idSensor': idSensor,
            'tomestamp': tomestamp,
            'value': value
        })
    print(response.text)

def put(idReading: str, idSensor: str = "5", tomestamp: str = "2213432", value: str = "33"):
    print("---- PUT ------------------------------------------")
    response = requests.put(uri+ '/reading/'+ idReading, json={
            'idSensor': idSensor,
            'tomestamp': tomestamp,
            'value': value
        })
    try:
        print(response.text)
    except Exception as e:
        print(response.reason)

def delete(idReading: str):
    print("---- DELETE ------------------------------------------")
    response = requests.delete(uri + '/reading/' + idReading)
    print(response.text)

def menu():
    while True:
        print("1- GET ALL")
        print("2- GET ONE")
        print("3- POST")
        print("4- PUT")
        print("5- DELETE")
        print("0- SAIR")
        opcao = input("Opção: ")
        if(opcao.isdigit() == False):
            break
        opcao = int(opcao)
        if(opcao == 0):
            exit()
        elif(opcao == 1):
            getAll()
        elif(opcao == 2):
            get(input("idReading: "))
        elif(opcao == 3):
            post(input("idSensor: "), input("Timestamp: "), input("Value: "))
        elif(opcao == 4):
            put(input("idReading: "), input("idSensor: "), input("Timestamp: "), input("Value: "))
        elif(opcao == 5):
            delete(input("idReading: "))
        if(opcao != 0):
            input("pressione ENTER para continuar...")

while True:
    menu()
