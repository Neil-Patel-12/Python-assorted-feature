# https://quotes.toscrape.com
import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice

all_quotes = []
base_url = "https://quotes.toscrape.com"
url = "/page/1"


while url:
	response = requests.get(f"{base_url}{url}")

	soup = BeautifulSoup(response.text, "html.parser")

	print(f"Now Scraping {base_url}{url}....")

	quotes = soup.find_all(class_="quote")

	for quote in quotes:
		all_quotes.append({
			"text": quote.find(class_="text").get_text(),
			"author": quote.find(class_="author").get_text(),
			"bio-link": quote.find("a")["href"]
		})

	next_btn = soup.find(class_="next")

	if next_btn:
		url = next_btn.find("a")["href"]
	else:
		url = None
	# sleep(2)

playing = True

while playing:
	quote = choice(all_quotes)
	print("\nHere is a quote: ")
	print(quote["text"])

	remaining_guesses = 4
	guess = ''
	while guess.lower() != quote["author"].lower() and remaining_guesses > 0:

		guess = input(f"\nWho said this quote? Guesses remaining: {remaining_guesses} ")

		if guess.lower() == quote["author"].lower() and remaining_guesses > 0:
			print("WOW, you are CORRECT!!!")
			break

		remaining_guesses -= 1

		if remaining_guesses == 3:
			res = requests.get(f"{base_url}{quote['bio-link']}")
			soup = BeautifulSoup(res.text, "html.parser")
			birth_date = soup.find(class_="author-born-date").get_text()
			birth_place = soup.find(class_="author-born-location").get_text()
			print(f"Here's a hint: The author was born on {birth_date} {birth_place}")

		elif remaining_guesses == 2:
			initial = quote["author"][0]
			print(f"Here's a hint: The authors first name starts with: {initial}")

		elif remaining_guesses == 1:
			arr = quote["author"].split()
			initial = arr[1][0]
			print(f"Here's a hint: The authors last name starts with: {initial}")
		else:
			print(f"Sorry you ran out of guesses. The answer was {quote["author"]}")

	play_again = input("Would you like to play again? (y/n) ")
	if play_again == 'y':
		continue
	if play_again == 'n':
		playing = False

print("\nThanks for Playing.\n")