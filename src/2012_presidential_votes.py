import pandas as pd
import decimal
import requests
from bs4 import BeautifulSoup

page3 = requests.get('https://www.archives.gov/federal-register/electoral-college/2012/popular-vote.html')

soup3 = BeautifulSoup(page3.text, "html.parser")
for body in soup3("body"):
    body.unwrap()

tables3 = pd.read_html(str(soup3), flavor="bs4")

pd.set_option('display.max_rows', len(tables3))


demVotes = []
gopVotes = []
totalVotes = []
percentages = []

for i in range(1,len(tables3[1][1])-1):
	demVotes.append(int(str(tables3[1][1][i])))
for i in range(1,len(tables3[1][2])-1):
	gopVotes.append(int(str(tables3[1][2][i])))
for i in range(1,len(tables3[1][6])-1):
	totalVotes.append(int(str(tables3[1][6][i])))

demPercs = []
gopPercs = []
for i in range(0,len(totalVotes)):
	demPerc = 100*(demVotes[i]/float(totalVotes[i]))
	demPercs.append(str(demPerc)[:5])
	gopPerc = 100*(gopVotes[i]/float(totalVotes[i]))
	gopPercs.append(str(gopPerc)[:5])
	#print (str(gopPerc)[:5])

page = requests.get('http://www.governing.com/gov-data/state-census-population-migration-births-deaths-estimates.html')

soup = BeautifulSoup(page.text, "html.parser")
for body in soup("body"):
    body.unwrap()

tables = pd.read_html(str(soup), flavor="bs4")

pd.set_option('display.max_rows', len(tables))

populations = []
for i in tables[0]["2012 Estimate"]:
	populations.append(int(i))

for i in range(0, len(populations)):
	print(str(100*float(totalVotes[i])/populations[i])[:5])