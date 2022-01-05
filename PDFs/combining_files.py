import PyPDF2
import os

pdf_files = []

for file_name in os.listdir('PDFs'):
    if file_name.endswith('.pdf'):
        pdf_files.append(file_name)
pdf_files.sort(key=str.lower)

pdf_writer = PyPDF2.PdfFileWriter()

for file_name in pdf_files:
    pdf_obj = open('PDFs/' + file_name, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_obj)
    if pdf_reader.isEncrypted:
        continue

    for pageNum in range(1, pdf_reader.numPages):
        page_obj = pdf_reader.getPage(pageNum)
        pdf_writer.addPage(page_obj)

combined_file = open('PDFs/combined_files.pdf', 'wb')
pdf_writer.write(combined_file)
combined_file.close()
