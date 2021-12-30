import requests


URL = "http://localhost:8081/hbnfe/mgmt/health"

response = requests.post(URL)

print(response.json())
