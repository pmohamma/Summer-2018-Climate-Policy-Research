import json
import collections
from collections import OrderedDict
import pyperclip
import requests
from bs4 import BeautifulSoup
import xlsxwriter

class County(object):
	#averageTemp = ""
	countyN = ""
	value = ""

	#def __init__(self, averageTemp, countyN, value):
	def __init__(self, countyN, value):
		#self.averageTemp = averageTemp
		self.countyN = countyN
		self.value = value

#averageTemps = []
values = []
workbook = xlsxwriter.Workbook('Expenses05.xlsx')
worksheet = workbook.add_worksheet()
rowCounter = []

def getTemps(state:int, year:int, month: int):
	goodMonth = str(month)[-2:] 
	url = "https://www.ncdc.noaa.gov/cag/county/mapping/"+str(state)+"-tavg-" +str(year)+goodMonth+"-1.json"
	page = requests.get(url)

	soup = BeautifulSoup(page.text, "html.parser")
	for body in soup("body"):
	    body.unwrap()

	data = json.loads(str(soup))

	countyList = []
	if type(data) == dict:
		mainObj = data.get("data")
		for objs in mainObj.values():
			countyName = str(objs.get("location"))
			if "City" in countyName[-5:]:
				countyName = "zz" + countyName
			if countyName != "None":
				#countyList.append(County(objs.get("mean"), countyName, objs.get("value")))
				countyList.append(County(countyName, objs.get("value")))
			if countyName == "zzHopewell City":
				#countyList.append(County("", "zzHopewell Dity", ""))
				countyList.append(County("zzHopewell Dity", ""))

	countyList.sort(key = lambda x: x.countyN)
	for j in countyList:
		print(j.countyN)
		#averageTemps.append(str(j.averageTemp))
		values.append(str(j.value))
def singleMonth(year:int, month:int):
	getTemps(1, year, month)
	for i in range(1, 30): #ALASKA
		#averageTemps.append("")
		values.append("")
		print("")
	for i in range(2, 8):
		getTemps(i, year, month)
	getTemps(49, year, month)
	getTemps(8, year, month)
	getTemps(9, year, month)
	for i in range(1, 6):
		#averageTemps.append("")
		values.append("")
		print("")
	for i in range(10, 49):
		getTemps(i, year, month)
	for i in range(0, len(values)):
		worksheet.write(i, len(rowCounter), values[i])
	rowCounter.append(month)
"""getTemps(18)
for i in range(19, 49):
	getTemps(i)"""
#f = open("averageTemp.txt", "w+")
#f.write('\n'.join(str(p) for p in values))
#f.close()
#print(values)
#averageTempsStr = '\n'.join(str(p) for p in averageTemps)
#pyperclip.copy(averageTempsStr)
try:
	singleMonth(2010, 101)
	"""for j in range(112, 100, -1):
		singleMonth(2005, j)
		values = []"""
except Exception as e:
	print("Error error\n" + str(e))
#valuesStr = '\n'.join(str(p) for p in values)
#pyperclip.copy(valuesStr)
#col = 0
#worksheet.write(row, column, "thing to write")
workbook.close()
