import collections
import xlrd
import xlsxwriter

book = xlrd.open_workbook("Untitled spreadsheet.xlsx")
first_sheet = book.sheet_by_index(0)

workbook = xlsxwriter.Workbook("whatCounty.xlsx")
