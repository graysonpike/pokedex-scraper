# Script to get list of Pokemon names from dropdown of Serebii website

import requests
from bs4 import BeautifulSoup


SEREBII_URL = "https://www.serebii.net/pokedex-swsh/"


def main():

	pokemon = []

	page = requests.get(SEREBII_URL)
	soup = BeautifulSoup(page.text, 'html.parser')
	dropdown = soup.find('form', attrs={'name': 'galar'})
	for option in dropdown.findChildren("option"):
		value = option.attrs['value']
		if 'pokedex' in value:
			print(value)


main()