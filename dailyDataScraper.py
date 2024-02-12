from automation import Automation
import requests
from bs4 import BeautifulSoup

automation = Automation()

URL2 = automation.findDailyReportURL()

req = requests.get(URL2, headers={'User-Agent':'Mozilla/5.0'})
soup = BeautifulSoup(req.content, 'html.parser')

title_name = soup.title.text

dates = soup.find_all('h2', class_='date')
highLowTemps = soup.find_all('div', class_="temp")
remark = soup.find_all('div', class_="phrase")
precip = soup.find_all('div', class_="precip")

details = [
    {
        'index': index,
        'date': date_elem.find('span', class_="sub").text,
        'week': date_elem.find('span', class_="dow").text,
        'highest_temperature': high_temp.find('span', class_="high").text,
        'low_temperature': high_temp.find('span', class_="low").text[1:],
        'precipitation': precip_elem.text[4:precip_elem.text.index("%") + 1],
        'remarks': remark_elem.text
    }
    for index, (date_elem, high_temp, precip_elem, remark_elem) in enumerate(zip(dates, highLowTemps, precip, remark))
]

print(details)
