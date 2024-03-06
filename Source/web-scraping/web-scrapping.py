'''
aprendendo webscrapping
learning source: freecodecamp | 
'''

import requests
from bs4 import BeautifulSoup
res = requests.get("https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")

if res.status_code == 200:
        soup = BeautifulSoup(res.content, 'html.parser')
        title = soup.text.title
        print(title)
        head = soup.__