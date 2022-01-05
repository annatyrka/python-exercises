import PyPDF2

minutes_file = open('PDFs/meetingminutes.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(minutes_file)
page = pdf_reader.getPage(0)
page.rotateClockwise(90)

pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.addPage(page)

result_file = open('PDFs/rotated.pdf', 'wb')
pdf_writer.write(result_file)

result_file.close()
minutes_file.close()
