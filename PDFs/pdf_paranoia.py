# walk through directory and encrypt each PDF with a passowrd from a command line
# save each pdf with an _encrypted.pdf suffix
# have the program attempt to read and decrypt the file to enusre it was encrypted correctly

import PyPDF2
import os
import sys

password = sys.argv[1]
for folder_name, subfolders, file_names in os.walk('/Users/annatyrka/PythonPractice/PDFs'):
    print(f"Checking folder {folder_name}")

    for file_name in file_names:
        if file_name.endswith('.pdf'):
            print(f"Checking file {file_name}")
            fileObj = open('PDFs/'+file_name, 'rb')
            pdfReader = PyPDF2.PdfFileReader(fileObj)
            if pdfReader.isEncrypted:
                continue
            print(f"Opening {file_name}")
            pdfWriter = PyPDF2.PdfFileWriter()
            for page_num in range(pdfReader.numPages):
                pdfWriter.addPage(pdfReader.getPage(page_num))

            pdfWriter.encrypt(password)

            new_file = open('PDFs/' + file_name[:-4] + '_encrypted.pdf', 'wb')
            pdfWriter.write(new_file)
            fileObj.close()
            new_file.close()

for folder_name, subfolders, file_names in os.walk('/Users/annatyrka/PythonPractice/PDFs'):
    print(f"Checking folder {folder_name}")

    for file_name in file_names:
        if file_name.endswith('_encrypted.pdf'):
            fileObj = open('PDFs/'+file_name, 'rb')
            pdfReader = PyPDF2.PdfFileReader(fileObj)
            pdfReader.decrypt(password)
            print(f"file {file_name} decrypted")
            fileObj.close()

for folder_name, subfolders, file_names in os.walk('/Users/annatyrka/PythonPractice/PDFs'):
    print(f"Checking folder {folder_name}")

    for file_name in file_names:
        if file_name.endswith('_encrypted.pdf'):
            fileObj = open('PDFs/'+file_name, 'rb')
            pdfReader = PyPDF2.PdfFileReader(fileObj)
            pdfWriter = PyPDF2.PdfFileWriter()
            pdfReader.decrypt(password)

            for page_num in range(pdfReader.numPages):
                pdfWriter.addPage(pdfReader.getPage(page_num))
            pdfWriter.encrypt(password)
            new_copy = open('PDFs/'+file_name[0:-4] + 'backup.pdf', 'wb')
            pdfWriter.write(new_copy)
            fileObj.close()
            new_copy.close()
