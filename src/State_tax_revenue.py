import collections
import requests
from bs4 import BeautifulSoup
import xlsxwriter
import pandas as pd

workbook = xlsxwriter.Workbook("state_tax_revenue09.xlsx")
worksheet = workbook.add_worksheet()

try:
	row_counter = 1
	for year in range(2009, 2010):

		url = "https://www.taxadmin.org/" + str(year) + "-state-tax-revenue"
		page = requests.get(url)

		soup = BeautifulSoup(page.text, "html.parser")
		for body in soup("body"):
		    body.unwrap()

		tables = pd.read_html(str(soup), flavor="bs4")

		pd.set_option('display.max_rows', len(tables))

		total_taxes = tables[0][1]
		state = tables[0][0]

		for i in range(3,11):
			worksheet.write(i-3, row_counter, str(total_taxes[i]))
			worksheet.write(i-3, 0, str(state[i]))

		dc = len(total_taxes)-2
		worksheet.write(8, row_counter, str(total_taxes[dc]))
		worksheet.write(8, 0, str(state[dc]))

		for i in range(11, dc):
			worksheet.write(i-2, row_counter,str(total_taxes[i]))
			worksheet.write(i-2, 0, str(state[i]))

		row_counter += 1

except Exception as e:
	print("error error\n" + str(e))

workbook.close()


