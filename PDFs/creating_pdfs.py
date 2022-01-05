import PyPDF2

pdf_file1 = open('PDFs/meetingminutes.pdf', 'rb')   # file object
pdf_file2 = open('PDFs/meetingminutes2.pdf', 'rb')

pdf_reader1 = PyPDF2.PdfFileReader(pdf_file1)
pdf_reader2 = PyPDF2.PdfFileReader(pdf_file2)

# pdfFileWriter object - represents a PDF document in Python
pdf_writer = PyPDF2.PdfFileWriter()

for pageNum in range(pdf_reader1.numPages):
    page_obj = pdf_reader1.getPage(pageNum)
    pdf_writer.addPage(page_obj)

for pageNum in range(pdf_reader2.numPages):
    page_obj = pdf_reader2.getPage(pageNum)
    pdf_writer.addPage(page_obj)

pdf_output_file = open('PDFs/combined_minutes.pdf', 'wb')
pdf_writer.write(pdf_output_file)
pdf_output_file.close()
pdf_file1.close()
pdf_file2.close()
