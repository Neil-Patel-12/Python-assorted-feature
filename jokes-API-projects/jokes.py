import requests
from random import choice
import pyfiglet
import termcolor

header = pyfiglet.figlet_format("DAD JOKE 3000!")
header_color = termcolor.colored(header, color="magenta")
print(header_color)

user_input = input("What would you like to search for? ")

url = "https://icanhazdadjoke.com/search"

res = requests.get(
	url,
	headers={"Accept": "application/json"},
	params={"term":user_input}
).json()   # this is a python dictionary

num_jokes = res["total_jokes"]

if num_jokes > 1:
	print(f"I FOUND {num_jokes} JOKES ABOUT {user_input} HERE IS A RANDOM ONE!")
	the_joke = choice(res["results"])["joke"]
	print(the_joke)
elif num_jokes == 1:
	print(f"THERE IS ONE JOKE ABOUT {user_input}")
	print(res["results"][0]["joke"])
else:
	print(f"Sorry, couldn't find a joke with your term: {user_input}")