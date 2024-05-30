import requests

url = "https://icanhazdadjoke.com/"

# by default, its going to get me html
response = requests.get(url, headers={"Accept": "application/json"})
# text/html
# text/plain
# application/json
# pass in a header to specify what format we want our data

print(response.text) # this is a string that we are getting back
print(response.json()) # take the json and turn it in to Python dictionary

data = response.json() # javeScript Object Notation

for key in data.keys():
	print(key, "->", data[key])