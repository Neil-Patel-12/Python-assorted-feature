import requests

url = "http://www.google.com"
response = requests.get(url)

print(f"your request to {url} came back w/ status code")
print(f"{response.status_code}")