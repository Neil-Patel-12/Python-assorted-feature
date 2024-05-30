import requests
url = "http://icanhazdadjoke.com/search"

response = requests.get(url, headers={"Accept": "Application/json"})

data = response.json()

