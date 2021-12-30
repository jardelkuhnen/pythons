import requests

URL = "http://localhost:8081/hbnfe/input/{codigoEmpresa}/{cnpj}"

with open('nota.json', 'r') as nota:
    body = nota.read()

headers = {'Content-type': 'application/json'}

print(body)


x = range(1000)
for n in x:
  print('Request ' + str(n))
  response = requests.post(URL, data=body, headers=headers)
  print(response.json())
