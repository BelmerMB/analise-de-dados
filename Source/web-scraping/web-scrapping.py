from bs4 import BeautifulSoup
import requests

url = 'https://www.climatempo.com.br/previsao-do-tempo/cidade/88/goiania-go'

r = requests.get(url)
#print(r.content)

if r.status_code == 200:
        soup = BeautifulSoup(r.content, 'html.parser')
        #print(soup.prettify())
        para = soup.find('div')
        print(para)