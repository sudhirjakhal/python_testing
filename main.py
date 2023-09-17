'''
from PyPDF2 import *

with open('table.pdf', 'rb')as f:
    pdf_reader = PdfReader(f)
    for page_number in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_number]
        print(page.extract_text)

print('Successful.')
'''
from camelot import read_pdf
file_name = input('Enter the file name:')
tables = read_pdf(file_name)
tables[0].df.to_excel('foo.xlsx')