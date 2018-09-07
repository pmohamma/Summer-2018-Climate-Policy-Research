import requests
import collections
from bs4 import BeautifulSoup
import pprint
from html.parser import HTMLParser
import xlrd
import xlsxwriter
"""
book = xlrd.open_workbook("Untitled spreadsheet.xlsx")
first_sheet = book.sheet_by_index(0)
cities_list = []
states_list = []
for j in range(1400, 1829):
	r = first_sheet.row_values(j)
	cities_list.append(str(r[1]))
	states_list.append(str(r[0]))

workbook = xlsxwriter.Workbook("whatCounty.xlsx")
worksheet = workbook.add_worksheet()
row_counter = 0

try:
	for i in range(0, len(cities_list)):
		city = cities_list[i]
		state = states_list[i]
		city = str(city).replace(" ","_")
		state = str(state).replace(" ", "_")

		url = "https://en.wikipedia.org/wiki/"+str(city)+",_"+str(state)
		page = requests.get(url)
		soup = BeautifulSoup(page.text, "html.parser")
		for body in soup("body"):
		    body.unwrap()
		imgCounter = False
		class MyHTMLParser(HTMLParser):
		    def handle_starttag(self, tag, attrs):
		    	global imgCounter
		    	if str(tag).strip() == "img":
		        	imgCounter = True

		    def handle_data(self, data):
		    	global imgCounter
		    	global worksheet
		    	global city
		    	if (imgCounter == True):
		    		if ("county" in str(data).lower()) & ("in" in str(data).lower()):
		    			worksheet.write(i, 0, city)
		    			inspot = str(data).lower().find("in ")
		    			countyspot = str(data).lower().find("county")
		    			sdata = str(data)[inspot+3:countyspot+8+len(state)]
		    			worksheet.write(i, 1, sdata)
		    		#else:
		    		#	row_counter+=1
		    		imgCounter=False

		parser = MyHTMLParser()
		parser.feed(str(soup.encode("utf-8")))
except Exception as e:
	print("error error\n"+str(e))

workbook.close()
"""
book = xlrd.open_workbook("Untitled spreadsheet.xlsx")
first_sheet = book.sheet_by_index(0)
cities_list = []
states_list = []
for j in range(1, 386):
	r = first_sheet.row_values(j)
	cities_list.append(str(r[1]))
	states_list.append(str(r[0]))

workbook = xlsxwriter.Workbook("whatCounty.xlsx")
worksheet = workbook.add_worksheet()
row_counter = 0
try:
	for i in range(0, len(cities_list)):
		city = cities_list[i]
		state = states_list[i]

		url = "https://www.google.com/search?ei=Y2haW4PFEM7YsAWl9oq4DQ&q=what+county+is+"+str(city)+"+"+str(state)+"+in&oq=what+county+is+"+str(city)+"+"+str(state)+"+in&gs_l=psy-ab.3..0.44582.45433..45580...0.0...96.426.7......0....1..gws-wiz.......0i71j0i7i30j0i8i30j0i13.JS6QDxMmMM0"
		page = requests.get(url)
		soup = BeautifulSoup(page.text, "html.parser")
		for body in soup("body"):
		    body.unwrap()
		imgCounter = 0
		class MyHTMLParser(HTMLParser):
		    def handle_starttag(self, tag, attrs):
		    	global imgCounter
		    	if str(tag).strip() == "img":
		        	imgCounter +=1

		    def handle_data(self, data):
		    	global imgCounter
		    	global row_counter
		    	global worksheet
		    	global city
		    	if imgCounter == 2:
		    		if "county" in str(data).lower():
		    			worksheet.write(row_counter, 0, city)
		    			worksheet.write(row_counter, 1, data)
		    			row_counter+=1
		    		else:
		    			row_counter+=1
		    		imgCounter+=1
		parser = MyHTMLParser()
		parser.feed(str(soup.encode("utf-8")))
except Exception as e:
	print("error error\n"+str(e))

workbook.close()