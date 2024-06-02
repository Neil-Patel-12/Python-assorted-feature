import requests
url = "http://icanhazdadjoke.com/search"
# same as "http://icanhazdadjoke.com/search?term=cat&limit=1"

response = requests.get(
	url, 
	headers={"Accept": "Application/json"}, 
	params={"term": "cat", "limit": 1}
	)

data = response.json()

print(data["results"])