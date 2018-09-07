import collections
import xlsxwriter
import xlrd

fname = "Untitled spreadsheet.xlsx"
book = xlrd.open_workbook(fname)
first_sheet = book.sheet_by_index(0)

workbook = xlsxwriter.Workbook("cleanerDSIRE.xlsx")
worksheet = workbook.add_worksheet()

try:
	worksheet.write(0, 0, "implementing Sector")
	for i in range(1, 3710):
		cellVal = (first_sheet.cell(i, 0).value)
		if (cellVal[-4:]).lower() == "(no)":
			firstLetter = (cellVal[:1]).lower()
			if  firstLetter == "u":
				worksheet.write(i, 0, (cellVal[:-4]))
				worksheet.write(i, 1, "private utility")
			elif firstLetter == "n":
				worksheet.write(i, 0, (cellVal[:-4]))
				worksheet.write(i, 1, "private non-profit")
			elif firstLetter == "o":
				worksheet.write(i, 0, (cellVal[:-4]))
				worksheet.write(i, 1, "private other")
		elif (cellVal[-22:]).lower() == "(utility run by gov't)":
			worksheet.write(i, 0, (cellVal[:-23][-5:]).lower())
			worksheet.write(i, 1, "Utility run by gov't")
		elif "/" in cellVal:
			worksheet.write(i, 0, cellVal)
			print(i)
		else:
			worksheet.write(i, 0, cellVal)

except Exception as e:
	print("error error\n" + str(e))

workbook.close()