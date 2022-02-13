import PyPDF2

file_obj = open('PDFs/meetingminutes.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(file_obj)
page = pdf_reader.getPage(0)

page.rotateCounterClockwise(90)

pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.addPage(page)
new_file = open('PDFs/roated2.pdf', 'wb')
pdf_writer.write(new_file)
new_file.close()
file_obj.close()
