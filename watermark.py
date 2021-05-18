import PyPDF2

template = PyPDF2.PdfFileReader(open('super.pdf','rb'))
watermark = PyPDF2.PdfFileReader(open('213_wtr.pdf','rb'))
output = PyPDF2.PdfFileWriter()

def pdf_watermark(pdf_list):
	for i in range(template.getNumPages()):
		page = template.getPage(i)
		page.mergePage(watermark.getPage(0))
		output.addPage(page)
		with open('super-wtr.pdf','wb') as file:
			output.write(file)

pdf_watermark(output)
