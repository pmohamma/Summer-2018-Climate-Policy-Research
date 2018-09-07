import collections
from collections import OrderedDict
import requests
from bs4 import BeautifulSoup
import xlsxwriter
import pandas as pd
import xlrd

states = ["", "alabama", "alaska","", "arizona", "arkansas", "california","", "colorado",
"connecticut", "delaware", "district of columbia","florida", "georgia", "","hawaii",
"idaho", "illinois", "indiana", "iowa", "kansas", "kentucky","", "louisiana", 
"maine", "maryland", "massachusetts", "michigan", "minnesota", "mississippi",
"missouri", "montana", "nebraska", "nevada", "new hampshire", "new jersey",
"new mexico", "new york", "north carolina", "north dakota", "ohio", "oklahoma",
"oregon","", "pennsylvania", "rhode island", "south carolina", "south dakota", 
"tennessee", "texas", "utah", "vermont", "","virginia", "washington", 
"west virginia", "wisconsin", "wyoming"]

bad_states_for_url = [3, 7,14,22,43,52] #wyoming is 56 so do range(2, 57)
workbook = xlsxwriter.Workbook('2000votes.xlsx')
worksheet = workbook.add_worksheet()

def get_results(state:int):
	global worksheet
	global sheet
	global spot_on_sheet
	
	dic = {}
	url = "https://uselectionatlas.org/RESULTS/datagraph.php?year=2000&fips="+str(state)+"&f=0&off=0&elect=0"
	page = requests.get(url)

	soup = BeautifulSoup(page.text, "html.parser")
	for body in soup("body"):
	    body.unwrap()

	tables = pd.read_html(str(soup), flavor="bs4")

	pd.set_option('display.max_rows', len(tables))

	for i in range(1, len(tables)):
		current_county = str(tables[i][0][0]).lower().strip()
		dic.update({current_county:[tables[i][2][0], tables[i][1][1]]}) #gore, then bush

	current_state = sheet.cell_value(spot_on_sheet, 0)
	print(current_state)
	while(sheet.cell_value(spot_on_sheet, 0) == current_state):
		county = str(sheet.cell_value(spot_on_sheet, 1)).lower()
		if "county" in county:
			county = county.replace("county","").strip()
		elif "city" in county:
			county = county.replace("city", "").strip()
		else:
			county = county.replace("parish", "").strip()
		worksheet.write(spot_on_sheet, 0, county)
		try:
			worksheet.write(spot_on_sheet, 1, dic.get(county)[0])
			worksheet.write(spot_on_sheet, 2, dic.get(county)[1])
		except:
			worksheet.write(spot_on_sheet, 1, "none")
			worksheet.write(spot_on_sheet, 2, "none")
		spot_on_sheet+=1

try:
	book = xlrd.open_workbook("Untitled spreadsheet.xlsx")
	sheet = book.sheet_by_index(0)
	gore_votes = []
	bush_votes = []
	spot_on_sheet = 1

	get_results(1)
	"""for i in range(4, 57):
		if i == 22:
			for i in range(1, 65):
				spot_on_sheet+=1
		elif i not in bad_states_for_url:
			get_results(i)"""
	
except Exception as e:
	print("error error\n" + str(e))

workbook.close()