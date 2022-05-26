import xlsxwriter
from trainScraping2 import array

def writer(parametr):
	book = xlsxwriter.Workbook(r"data.xlsx")
	page = book.add_worksheet("Tovar")

	row = 0
	col = 0

	page.set_column("A:A",20)
	page.set_column("B:B",20)
	page.set_column("C:C",50)
	page.set_column("D:D",50)


	for i in parametr():
		page.write(row,col,i[0])
		page.write(row,col+1,i[1])
		page.write(row,col+2,i[2])
		page.write(row,col+3,i[3])
		row += 1

	book.close()

writer(array)