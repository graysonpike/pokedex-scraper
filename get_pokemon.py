# Script obtains information from each pokemons individual webpage

import requests
from bs4 import BeautifulSoup


SEREBII_URL = "https://www.serebii.net"

def get_poke_url():
	links = []
	for line in open("data/pokemon_links.txt"):
		links.append(SEREBII_URL + line.strip())
	return links

def scrape_page(url):
	pokemon_data = {}
	request = requests.get(url)
	soup = BeautifulSoup(request.text, 'html.parser')
	dextab = soup.find("table", attrs={"class": "dextab"})
	dextables = soup.find_all("table", attrs={"class": "dextable"})

	
	pokemon_data["name"] = soup.find("h1").text.split(" ")[1]
	pokemon_data["nat_num"] = int(dextables[1].find_all("tr")[1].find_all("td", attrs={"class": "fooinfo"})[2].find_all("td")[1].text.replace("#", ""))
	pokemon_data["gal_num"] = int(dextables[1].find_all("tr")[1].find_all("td", attrs={"class": "fooinfo"})[2].find_all("td")[3].text.replace("#", ""))
	
	print(pokemon_data)



def main():

	links = get_poke_url()
	scrape_page(links[0])


main()

