# Script obtains information from each pokemons individual webpage

import requests
from bs4 import BeautifulSoup


SEREBII_URL = "https://www.serebii.net"

def get_poke_url():
	links = []
	for line in open("data/pokemon_links.txt"):
		links.append(SEREBII_URL + line.strip())
	return links





def main():
	print(get_poke_url())


main()

