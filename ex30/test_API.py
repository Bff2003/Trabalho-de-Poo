import requests

uri = 'http://localhost:8080/'+ 'reading/' 

print(20 * '*' + ' GET all')
response = requests.get(uri)
print(response.text)


print(20 * '*' + ' GET one')
response = requests.get(uri + '77')
print(response.text)


print(20 * '*' + ' POST')
response = requests.post(uri, json={
            'idSensor': 5,
            'tomestamp': 2222,
            'value': 22
        })
print(response.text)


print(20 * '*' + ' PUT')
response = requests.put(uri + '77', json={
            'idSensor': 5,
            'tomestamp': 2222,
            'value': 22
        })
print(response.text)

print(20 * '*' + ' GET all (again)')
response = requests.get(uri)
print(response.text)


print(20 * '*' + ' DELETE')
response = requests.delete(uri + '105')
print(response.text)

print(20 * '*' + ' GET all (again)')
response = requests.get(uri)
print(response.text)


