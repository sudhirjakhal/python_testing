from camelot import read_pdf
file_name = input('Enter the file name:')
tables = read_pdf(file_name)
tables[0].df.to_excel('foo.xlsx')