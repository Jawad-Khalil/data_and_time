"""This is a simple Python code that returns the current Islamic and Gregorian date in Pakistan 
from the website https://hamariweb.com . The program is based on wep-scrapping.
"""

import requests
from bs4 import BeautifulSoup

url = "https://hamariweb.com/islam/today-islamic-date-in-pakistan.aspx"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

required_data = soup.find_all("div", class_="today_date")
required_data1 = required_data[0].find("p").text.strip()
required_data2 = required_data[1].find("p").text.strip()

print('Current Islamic Date in Pakistan=', required_data1)
print('Current Gregorian Date in Pakistan=', required_data2)

