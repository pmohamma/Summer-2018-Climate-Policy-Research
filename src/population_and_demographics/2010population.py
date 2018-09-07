import xlrd
import collections
import pandas as pd
import requests
from bs4 import BeautifulSoup
import pyperclip

stateCodes = {"alabama":"al", "alaska": "ak", "arizona":"az", "arkansas":"ar", "california":"ca", "colorado":"co",
"connecticut":"ct", "delaware":"de", "florida":"fl", "district of columbia":"dc", "georgia":"ga", "hawaii":"hi",
"idaho":"id", "illinois":"il", "indiana":"in", "iowa":"ia", "kansas":"ks", "kentucky":"ky", "louisiana":"la",
"maine":"me", "maryland":"md", "massachusetts":"ma", "michigan":"mi", "minnesota":"mn", "mississippi":"ms",
"missouri":"mo", "montana":"mt", "nebraska":"ne", "nevada":"nv", "new hampshire":"nh", "new jersey":"nj",
"new mexico":"nm", "new york":"ny", "north carolina":"nc", "north dakota":"nd", "ohio":"oh", "oklahoma":"ok",
"oregon":"or", "pennsylvania":"pa", "rhode island":"ri", "south carolina":"sc", "south dakota":"sd", 
"tennessee":"tn", "texas":"tx", "utah":"ut", "vermont":"vt", "virginia":"va", "washington":"wa", 
"west virginia":"wv", "wisconsin":"wi", "wyoming":"wy"}

book = xlrd.open_workbook("Untitled spreadsheet.xlsx")
sheet = book.sheet_by_index(0)
cities = []
states = []
for i in range(1, 1820):
	cities.append(str(sheet.cell_value(i, 1)).lower().strip())
	states.append(str(sheet.cell_value(i, 0)).lower().strip())

current_state = ""
data = {}
copyStr = ""

for j in range(0, len(cities)-1):
	if current_state != states[j]:
		print(states[j])
		current_state = states[j]
		stateCode = stateCodes.get(current_state)
		url = "https://www.biggestuscities.com/"+stateCode+"/2010"
		page = requests.get(url)
		soup = BeautifulSoup(page.text, "html.parser")
		for body in soup("body"):
			body.unwrap()

		tables = pd.read_html(str(soup), flavor = "bs4")
		pd.set_option('display.max_rows', len(tables))
		data = {}

		for i in range(0, len(tables[0][1])-1):
			data.update({str(tables[0][1][i]).lower().strip():str(tables[0][3][i]).lower().strip()})
		try:
			for i in range(0, len(tables[1][1])-1):
				data.update({str(tables[1][1][i]).lower().strip():str(tables[1][3][i]).lower().strip()})
		except:
			print("no second table")
	temp = data.get(cities[j])
	copyStr = copyStr + str(temp) + "\n"

pyperclip.copy(copyStr)