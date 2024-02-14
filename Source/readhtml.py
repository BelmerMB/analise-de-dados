import pandas

url = 'https://www.sump.org/notes/request/'
leitor = pandas.read_html(url)
print(leitor)