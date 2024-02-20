import pandas

url = 'https://www.sump.org/notes/refquest/'
leitor = pandas.read_html(url)
print(leitor)