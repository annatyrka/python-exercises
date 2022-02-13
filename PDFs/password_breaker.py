import PyPDF2
# roated2_encrypted.pdf

dictionary = open('PDFs/dictionary.txt')
words_list = dictionary.readlines()
print(len(words_list))
# print(words_list.index('password'))
# print(words_list.index('ANNA\n'))
# print(words_list[1948][:-1])
pdfObj = open('PDFs/roated2_encrypted.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfObj)

for word in words_list:
    if pdfReader.decrypt(word[:-1].upper()) == 1:
        print(f"The password was {word}")
        pdfReader.decrypt(word)
        break
    if pdfReader.decrypt(word[:-1].lower()) == 1:
        print(f"The password was {word}")
        pdfReader.decrypt(word)
        break

pdfObj.close()
