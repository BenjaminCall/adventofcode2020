import requests
from bs4 import BeautifulSoup
import pandas as pd

allZips = [
"84302",	"84038",	"84201",	"84041",	"84124",	"84088",	"84065",
"84311",	"84319",	"84403",	"84037",	"84117",	"84081",	"84069",
"84337",	"84335",	"84067",	"84075",	"84121",	"84095",	"84074",
"84321",	"84403",	"84405",	"84014",	"84118",	"84009",	"84074",
"84341",	"84404",	"84089",	"84025",	"84123",	"84070",	"84005",
"84054",	"84103",	"84119",	"84105",	"84118",	"84094",	"84043",
"84087",	"84105",	"84128",	"84115",	"84107",	"84093",	"84045",
"84010",	"84044",	"84123",	"84106",	"84047",	"84092",	"84003",
"84116",	"84104",	"84101",	"84117",	"84084",	"84020",	"84004",
"84062",	"84097",	"84604",	"84663",	"84055",	"84021",	"84627",
"84057",	"84602",	"84653",	"84651",	"84032",	"84648",	"84701",
"84059",	"84606",	"84660",	"84040",	"84078",	"84624",	"84501",
"84720",	"84738",	"84737",	"84780",	"84770",	"84535",	"84513",
"84722"]	

pop, un, inc, age, validZips = [],[],[],[],[]

for zip in allZips:
	page = requests.get("https://www.bestplaces.net/zip-code/utah/ogden/" + zip)
	soup = BeautifulSoup(page.content, 'html.parser')

	for num, dataSection in enumerate(soup.findAll('div', attrs={'class': 'col-md-4'})[:3]):
		if num == 0:
			# get the population and unemployment
			pop.append(dataSection.find('p', attrs={'class': 'text-center py-0 my-0'}).get_text())
			un.append(dataSection.findAll('p', attrs={'class': 'text-center'})[-1].get_text())
		elif num == 1:
			# get the median income
			inc.append(dataSection.findAll('p', attrs={'class': 'text-center'})[1].get_text())
		elif num == 2:
			# get the age
			age.append(dataSection.findAll('p', attrs={'class': 'text-center'})[1].get_text())
			validZips.append(zip)
		else:
			continue 

df = pd.DataFrame({'Zip': validZips, 'Population': pop, 'Unemployment': un, 'Median Income': inc, 'Age': age}) 
df.to_csv('asdf.csv', index=True, encoding='utf-8')

