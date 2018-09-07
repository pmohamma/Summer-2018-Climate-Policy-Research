import collections
from collections import OrderedDict
import requests
import xlsxwriter
import xlrd
from bs4 import BeautifulSoup
import pandas as pd

book = xlrd.open_workbook("Untitled spreadsheet.xlsx")
first_sheet = book.sheet_by_index(0)

workbook = xlsxwriter.Workbook('populationsOfCities.xlsx')
worksheet = workbook.add_worksheet()
row_counter = 0

cities = []
state = "AL"
state_cities = []
populations = []

try:
	for i in range(1, 700):
		row = first_sheet.row_values(i)
		if state != row[3]:
			page3 = requests.get("https://www.biggestuscities.com/"+str(state))
			soup3 = BeautifulSoup(page3.text, "html.parser")
			for body in soup3("body"):
			    body.unwrap()

			tables = pd.read_html(str(soup3), flavor="bs4")

			pd.set_option('display.max_rows', len(tables))


			for r in range(1, len(tables[0][1])):
				state_cities.append(tables[0][1][r])
				populations.append(tables[0][3][r])
			for k in range(1, len(tables[1][1])):
				try:
					state_cities.append((tables[1][1][k]).strip().lower())
					populations.append((tables[1][3][k]).strip().lower())
				except:
					pass
			for j in cities:
				try:
					spot = state_cities.index(j.strip().lower())
				except:
					spot = -1
				worksheet.write(row_counter, 0, str(j))
				if spot != -1:
					worksheet.write(row_counter, 1, str(populations[spot]))
				else:
					worksheet.write(row_counter, 1, "not found")
				row_counter+=1

			if state == "AL":
				for l in cities:
					print(l)
				for b in state_cities:
					print(b)
			state = row[3]
			cities = []
			state_cities = []
			populations = []

		cities.append(row[1])

except Exception as e:
	print("error error\n"+str(e))

workbook.close()

"""
page3 = requests.get("https://www.biggestuscities.com/ia")
soup3 = BeautifulSoup(page3.text, "html.parser")
for body in soup3("body"):
    body.unwrap()

tables = pd.read_html(str(soup3), flavor="bs4")

pd.set_option('display.max_rows', len(tables))

for row in range(1, len(tables[0][1])):
	print(tables[0][1][row])
	print(tables[0][3][row])
"""

"""
class City(object):
	cname = ""
	state = ""
	income2016 = ""
	income2015 = ""
	income2014 = ""
	income2013 = ""
	income2012 = ""
	income2011 = ""
	income2010 = ""
	income2009 = ""
	income2008 = ""
	income2007 = ""
	income2006 = ""
	income2005 = ""
	#population = ""
	#pop_growth = ""

	def __init__(self, cname, state, income):#population, pop_growth):
		self.cname = cname
		self.state = state
		self.income2016 = income2016
		self.income2015 = income2015
		self.income2014 = income2014
		self.income2013 = income2013
		self.income2012 = income2012
		self.income2011 = income2011
		self.income2010 = income2010
		self.income2009 = income2009
		self.income2008 = income2008
		self.income2007 = income2007
		self.income2006 = income2006
		self.income2005 = income2005
		
		#self.population = population
		#self.pop_growth = pop_growth
book = xlrd.open_workbook("county_income_and_poverty.xlsx")
first_sheet = book.sheet_by_index(0)

workbook = xlsxwriter.Workbook('IncomeUSCounties.xlsx')
worksheet = workbook.add_worksheet()
row_counter = 0

try:
	for i in range(1, 37706):
		row = first_sheet.row_values(i)
		if row[0] == 2005:
			for j in range(0, len(row)):
				worksheet.write(row_counter, j, row[j])
			row_counter+=1

except Exception as e:
	print("error error\n" + str(e))

workbook.close()
"""


"""
workbook = xlsxwriter.Workbook('PopulationUSCities.xlsx')
worksheet = workbook.add_worksheet()

try:
	url = "https://www.biggestuscities.com/"
	page = requests.get(url)

	soup = BeautifulSoup(page.text, "html.parser")
	for body in soup("body"):
	    body.unwrap()

	tables = pd.read_html(str(soup), flavor="bs4")

	pd.set_option('display.max_rows', len(tables))

	mainTable = tables[0]

	worksheet.write(0, 0, "city")
	worksheet.write(0, 1, "state")
	worksheet.write(0, 2, "population")
	worksheet.write(0, 3, "population growth: 2000-2017")

	city_list = []

	add_amount = len(mainTable[1])
	for i in range(1, add_amount):
		cityName = mainTable[1][i]
		stateName = mainTable[2][i]
		populationNumber = mainTable[3][i]
		growth_percentage = mainTable[4][i]
		city_list.append(City(cityName, stateName, populationNumber, growth_percentage))
		worksheet.write(i, 0, str(cityName))
		worksheet.write(i, 1, str(stateName))
		worksheet.write(i, 2, str(populationNumber))
		worksheet.write(i, 3, str(growth_percentage))

	mainTable = tables[1]
	for i in range(1, len(mainTable[1])):
		cityName = mainTable[1][i]
		stateName = mainTable[2][i]
		populationNumber = mainTable[3][i]
		growth_percentage = mainTable[4][i]
		city_list.append(City(cityName, stateName, populationNumber, growth_percentage))
		worksheet.write(i+add_amount, 0, str(cityName))
		worksheet.write(i+add_amount, 1, str(stateName))
		worksheet.write(i+add_amount, 2, str(populationNumber))
		worksheet.write(i+add_amount, 3, str(growth_percentage))

except Exception as e:
	print("error error\n" + str(e))

workbook.close()"""