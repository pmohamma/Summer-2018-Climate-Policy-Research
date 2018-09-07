from pygeocoder import Geocoder
import xlsxwriter
import xlrd

book = xlrd.open_workbook("Untitled spreadsheet.xlsx")
sheet = book.sheet_by_index(0)
workbook = xlsxwriter.Workbook("LatitudesLongitudes7.xlsx")
worksheet = workbook.add_worksheet()

try:
	for i in range(3000, 3143):
		county = str(sheet.cell_value(i, 1))
		state = str(sheet.cell_value(i, 0))
		temp = county + ", " + state
		try:
			location = Geocoder.geocode(temp)
			worksheet.write(i-3000, 0, location.latitude)
			worksheet.write(i-3000, 1, location.longitude)
			worksheet.write(i-3000, 2, county[:7]+(state[:2]).upper())	
		except: 
			worksheet.write(i-3000, 0, "ERROR")
			worksheet.write(i-3000, 1, "ERROR")
			worksheet.write(i-3000, 2, county[:7]+(state[:2]).upper())

except Exception as e:
	print("error error\n" + str(e))

workbook.close()
