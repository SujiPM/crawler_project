# Reading an excel file using Python
# import xlrd
import openpyxl

path = r"C:\\Users\\SUJI\\Desktop\\crawler_project\\dataminner\\dataminner\\spiders\\urls.xlsx"
wb_obj = openpyxl.load_workbook(path)
 
# Get workbook active sheet object
# from the active attribute
sheet_obj = wb_obj.active
 
# Cell objects also have a row, column,
# and coordinate attributes that provide
# location information for the cell.
 
# Note: The first row orcd 
# column integer is 1, not 0.
 
# Cell object is created by using
# sheet object's cell() method.
cell_obj = sheet_obj.cell(row = 1, column = 1)
 
# Print value of cell object
# using the value attribute
print(cell_obj.value)
 
# # Give the location of the file
# loc = ("path of file")
 
# # To open Workbook
# wb = xlrd.open_workbook("C:\Users\SUJI\Desktop\crawler_project\dataminner\dataminner\spiders\urls.xlsx")
# sheet = wb.sheet_by_index(0)
 
# # For row 0 and column 0
# print(sheet.cell_value(0, 0))