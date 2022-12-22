import requests

URL = "http://127.0.0.1:8000/stuinfo/7"

r = requests.get(url = URL)
print(r)
data = r.json()
print(data)