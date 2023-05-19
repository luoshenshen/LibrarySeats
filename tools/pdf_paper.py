from PyPDF2 import PdfReader, PdfWriter

readfile = r"C:\Users\ShenshenLuo\Documents\University Files\基于深度学习的农业病虫害检测系统设计与实现.pdf"
outfile = r"C:\Users\ShenshenLuo\Documents\基于深度学习的农业病虫害检测系统设计与实现.pdf"

pdfReader = PdfReader(open(readfile, 'rb'))
pdfFileWriter = PdfWriter()
numPages = len(pdfReader.pages)
pagelist = (1, 3, 5, 7,)
for index in range(0, numPages):
    if index not in pagelist:
        pageObj = pdfReader.pages[index]
        pdfFileWriter.add_page(pageObj)
pdfFileWriter.write(open(outfile, 'wb'))