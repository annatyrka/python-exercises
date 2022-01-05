import PyPDF2

pdf_file = open('PDFs/meetingminutes.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file)
pdf_writer = PyPDF2.PdfFileWriter()

for pageNum in range(pdf_reader.numPages):
    pdf_writer.addPage(pdf_reader.getPage(pageNum))

pdf_writer.encrypt('thisispassword')

pdf_result = open('PDFs/encryptedminutes.pdf', 'wb')
pdf_writer.write(pdf_result)

pdf_result.close()
pdf_file.close()
