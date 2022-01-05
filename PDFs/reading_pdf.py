import PyPDF2

pdf_file_object = open('PDFs/meetingminutes.pdf', 'rb')  # read binary mode

pdf_reader = PyPDF2.PdfFileReader(pdf_file_object)

print(pdf_reader.numPages)

page_object = pdf_reader.getPage(0)
text = page_object.extractText()
print(text)

pdf_file_object.close()
