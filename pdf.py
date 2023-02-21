from pdf2docx import Converter

pdf_file='pdf.pdf'
docx_file='cv.docx'
conv=Converter(pdf_file)
conv.convert(docx_file)
conv.close()