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
	types = dextables[1].find_all("tr")[1].find("td", attrs={"class": "cen"})
	typelist = []
	for a in types.findChildren("a"):
		choice = a['href'].split("/")[2].split(".")[0]
		typelist.append(choice)
	pokemon_data["types"] = typelist
	abilities = []
	for a in dextables[2].find_all("tr")[0].text.split(":")[1].split(")")[0].split("-"):
		abilities.append(a.replace(" ", "").replace("(", "|").strip())
	pokemon_data["abilities"] = abilities 
	hastutmoves = "false"
	if(typelist.contains["dragon"] || typelist.contains["steel"] || pokemon_data["gal_num"] < 9 || (pokemon_data["gal_num"] < 380 && pokemon_data["gal_num"] >= 377)):
		hastutmoves = "true"
	stat_area = dextables[13].find_all("tr")[2].find_all("td")
	stats = {
		"tot": 100,
		"hp": 100,
		"def": 100,
		"atk": 100,
		"spa": 100,
		"spd": 100,
		"spe": 100 
	}
	stats["tot"] = int(stat_area[0].text.split(":")[1].strip())
	stats["hp"] = int(stat_area[1].text.strip())
	stats["atk"] = int(stat_area[2].text.strip())
	stats["def"] = int(stat_area[3].text.strip())
	stats["spa"] = int(stat_area[4].text.strip())
	stats["spd"] = int(stat_area[5].text.strip())
	stats["spe"] = int(stat_area[6].text.strip())
	pokemon_data["stats"] = stats
	#pokemon_data["types"][0] = dextables[1].find_all("tr")[1].find("td", attrs={"class": "cen"})
	print(pokemon_data)
	





def main():

	links = get_poke_url()
	scrape_page(links[394])


main()

