import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.mirea.ru/schedule/")
soup = BeautifulSoup(page.text, "html.parser")