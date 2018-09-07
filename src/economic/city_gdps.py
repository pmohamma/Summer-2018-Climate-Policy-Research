import collections
from collections import OrderedDict
import requests
import xlsxwriter
import xlrd

class City(object):
	cname = ""
	state = ""
	income2016 = ""

	def __init__(self, cname, gdp):#population, pop_growth):
		self.cname = cname
		#self.state = state
		self.gdp = gdp

book = xlrd.open_workbook("gdp_by_city.xlsx")
first_sheet = book.sheet_by_index(0)
city_list = []
workbook = xlsxwriter.Workbook("city_gdps12.xlsx")
worksheet = workbook.add_worksheet()
row_counter = 0

try:
	for i in range(12, 33235, 87):
		lst = first_sheet.row_values(i)
		cityN = lst[0]
		gdp = lst[4]
		for j in range(0, len(lst)):
			worksheet.write(row_counter, j, lst[j])
		row_counter+=1

except Exception as e:
	print("error error\n" + str(e))

workbook.close()
