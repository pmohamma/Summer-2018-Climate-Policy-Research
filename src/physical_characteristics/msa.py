#import pandas as pd
import decimal
import requests
from bs4 import BeautifulSoup
import xlrd
import xlsxwriter
import pyperclip

book = xlrd.open_workbook("MSA_Counties.xlsx")
msa_counties = book.sheet_by_index(0)
book1 = xlrd.open_workbook("tempMSA.xlsx")
temp_msa = book1.sheet_by_index(0)
#workbook = xlsxwriter.Workbook("hooligan.xlsx")
#worksheet = workbook.add_worksheet()
copyStr = ""
#try:	
cities = []
counties = []
msas = {}
for i in range(0, 57):
	counties.append(str(temp_msa.cell_value(i, 3)))
	cities.append(str(temp_msa.cell_value(i, 2)))
for j in range(0, 232):
	msas.update({str(msa_counties.cell_value(j, 0)): str(msa_counties.cell_value(j, 1))})
for k in range(0, len(counties)):
	copyStr = copyStr + str(msas.get(counties[k])) + "\n"
pyperclip.copy(copyStr)
#except Exception as e:
#	print("error error\n" + str(e))

#workbook.close()