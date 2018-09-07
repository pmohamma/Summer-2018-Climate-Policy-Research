import json
import collections
import requests
from bs4 import BeautifulSoup
import xlsxwriter

with open("json_drought_data_2017-2018.json") as f:
    data = json.load(f)

#print(type(data)) #list
#print(type(data[0])) #dict
workbook = xlsxwriter.Workbook("drought Data.xlsx")
worksheet = workbook.add_worksheet()
try:
	worksheet.write(0, 0, "County")
	for i in range(0, 53):
		worksheet.write(0, i+1, str(data[i].get('ValidStart')))
	column_counter = 1
	row_counter = -5
	for i in range(0, len(data)):
		if (i%53)==0:
			row_counter+=6
			worksheet.write(row_counter, 0, "D0 "+str(data[i].get("County"))+" "+str(data[i].get("State")))
			worksheet.write(row_counter+1, 0, "D1 "+str(data[i].get("County"))+" "+str(data[i].get("State")))
			worksheet.write(row_counter+2, 0, "D2 "+str(data[i].get("County"))+" "+str(data[i].get("State")))
			worksheet.write(row_counter+3, 0, "D3 "+str(data[i].get("County"))+" "+str(data[i].get("State")))
			worksheet.write(row_counter+4, 0, "D4 "+str(data[i].get("County"))+" "+str(data[i].get("State")))
			worksheet.write(row_counter+5, 0, "None "+str(data[i].get("County"))+" "+str(data[i].get("State")))
			column_counter = 1
		worksheet.write(row_counter, column_counter, data[i].get('D0'))
		worksheet.write(row_counter+1, column_counter, data[i].get('D1'))
		worksheet.write(row_counter+2, column_counter, data[i].get('D2'))
		worksheet.write(row_counter+3, column_counter, data[i].get('D3'))
		worksheet.write(row_counter+4, column_counter, data[i].get('D4'))
		worksheet.write(row_counter+5, column_counter, data[i].get('None'))
		column_counter+=1
except Exception as e:
	print("error error\n"+str(e))

workbook.close()