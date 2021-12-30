import requests

URL = "http://172.18.188.106:8080/hbnmsg/mgmt/health"

r = requests.get(url = URL)

data = r.json()

print(data)
