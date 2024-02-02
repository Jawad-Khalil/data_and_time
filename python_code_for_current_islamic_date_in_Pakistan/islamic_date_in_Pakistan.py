"""This is a simple Python code that returns the current Islamic date in Pkistan 
from the website https://hamariweb.com . The program is based on wep-scrapping.
"""

import requests
from bs4 import BeautifulSoup

url = "https://hamariweb.com/islam/islamic-date-today.aspx"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
required_data = soup.find("div", class_="islamic_date").text
print('Current Islamic Date in Pakistan=', required_data)

