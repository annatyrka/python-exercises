import PyPDF2

pdf_reader = PyPDF2.PdfFileReader(open('PDFs/encrypted.pdf', 'rb'))
print(pdf_reader.isEncrypted)
pdf_reader.decrypt('rosebud')

page_obj = pdf_reader.getPage(0)
print(page_obj.extractText())
