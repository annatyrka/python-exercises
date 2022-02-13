import PyPDF2

minutes_file = open('PDFs/meetingminutes.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(minutes_file)

minutes_1st_page = pdf_reader.getPage(0)

pdf_watermark_reader = PyPDF2.PdfFileReader(open('PDFs/watermark.pdf', 'rb'))

minutes_1st_page.mergePage(pdf_watermark_reader.getPage(0))
pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.addPage(minutes_1st_page)

for pageNum in range(1, pdf_reader.numPages):
    page_obj = pdf_reader.getPage(pageNum)
    pdf_writer.addPage(page_obj)

result_file = open('PDFs/watermarked_cover.pdf', 'wb')
pdf_writer.write(result_file)

result_file.close()
minutes_file.close()
