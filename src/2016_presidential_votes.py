import pandas as pd
import decimal
import requests
from bs4 import BeautifulSoup

page3 = requests.get('https://www.politico.com/mapdata-2016/2016-election/results/map/president/')

soup3 = BeautifulSoup(page3.text, "html.parser")
for body in soup3("body"):
    body.unwrap()

tables3 = pd.read_html(str(soup3), flavor="bs4")

pd.set_option('display.max_rows', len(tables3))

whoWon = []
percentages = []

for i in tables3:
	whoWon.append(str(i[0][0])[0])
	percentages.append(float(str(i[1][0])[:-1]))

for i in range(0, len(tables3)):
	if(whoWon[i] == "D"):
		print(str(tables3[i][1][1])[:-1])
	else:
		print(str(percentages[i]))