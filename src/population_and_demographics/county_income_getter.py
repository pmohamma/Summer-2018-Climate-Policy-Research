import pandas as pd
import decimal
import requests
from bs4 import BeautifulSoup
import pyperclip

page3 = requests.get("https://public.tableau.com/vizql/w/WhatU_S_countieshavethelowestandthehighestmedianhouseholdincome/v/WhatU_S_countieshavethelowestandthehighestmedianhouseholdincome/viewData/sessions/E94696D0019D4DA889668A3761991BF9-0:0/views/5007290499824165213_18189014126542921238?maxrows=200&viz=%7B%22worksheet%22:%22Histogram%22,%22dashboard%22:%22What%20U.S.%20counties%20have%20the%20lowest%20and%20the%20highest%20median%20household%20income?%22%7D")

soup3 = BeautifulSoup(page3.text, "html.parser")
for body in soup3("body"):
    body.unwrap()

tables3 = pd.read_html(str(soup3), flavor="bs4")

pd.set_option('display.max_rows', len(tables3))

print(tables3)
"""class County(object):
	countyN = ""
	population = ""

	def __init__(self, countyN, population):
		self.countyN = countyN
		self.population = population

def makeCounty(countyN, population):
	county = County(countyN, population)
	return county"""

countyList = []
for i in range(1, len(tables3[0][1])-1):
	county = tables3[0][1][i]
	population = tables3[0][2][i]
	countyList.append(County(county, population))

countyList.sort(key = lambda x: x.countyN)

countyString = ""
#countyNames = ""
for i in countyList:
	countyString = countyString + str(i.population) + "\n"
	#countyNames = countyNames + str(i.countyN) + "\n"

pyperclip.copy(countyString)