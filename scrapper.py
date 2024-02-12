import xlsxwriter # for handelling excel files
import requests
from bs4 import BeautifulSoup

URL = "https://www.accuweather.com/en/in/haldwani-cum-kathgodam/1-191344_1_al/weather-forecast/1-191344_1_al?city=haldwani"
URL2 = "https://www.accuweather.com/en/in/haldwani-cum-kathgodam/1-191344_1_al/daily-weather-forecast/1-191344_1_al"

req = requests.get(URL2, headers={'User-Agent':'Mozilla/5.0'})

soup = BeautifulSoup(req.content, 'html.parser')

title_name = soup.title.text # used to extract the title text

dates = soup.find_all('h2',class_='date')
highLowTemps = soup.find_all('div', class_="temp")
remark = soup.find_all('div',class_="phrase")
precip = soup.find_all('div',class_="precip")
wind = soup.find_all("div",class_="right")


details = []
weeks =[]
date = []
high_temprature =[]
low_temprature=[]

remarks = []
precipitations =[]

for index in range(len(dates)):
    weeks.append(dates[index].find('span',class_="dow").text)
    date.append(dates[index].find('span',class_="sub").text)
    high_temprature.append(highLowTemps[index].find('span',class_="high").text)
    str = highLowTemps[index].find('span',class_="low").text
    low_temprature.append(str[1:len(str)]) # removing backslach form the temprature eg: /24 --> 24
    str = precip[index].text  # Extracting the precipitation  from this type of result = \n\n\t\t0%\n\t
    precipitations.append(str[4:str.index("%")+1])
    remarks.append(remark[index].text)
    # print(dates)

    details.append({
        'index':index,
        'date':date[index],
        'week':weeks[index],
        'highest_temprature':high_temprature[index],
        'low_temprature':low_temprature[index],
        'precipitation':precipitations[index],
        'remarks':remarks[index]
    })

print(details )






   






# print(weeks)
# print(remarks)



for index in range(len(dates)) :
    details.append({
        'index':index,
        'date':dates[index],
        'week':weeks[index],
        'highest_temprature':high_temprature[index],
        'low_temprature':low_temprature[index],
        'precipitation':precipitations[index],
        'remarks':remarks[index]
    })

# print(details)
# for details in details:
#     print(details)



# print(details)

# extracting temprature
# temprature = soup.select("div.temp")
# temprature = soup.find('div.temp')
# temprature = soup.div.get("class")

# temprature = soup.find('div', class_='temp')
# daily_weather = soup.find('a',class_='daily-forecast-card')
# print(daily_weather)

# print(temprature)

# print(soup.prettify())
# print(name)



#  creating workbook
workbook = xlsxwriter.Workbook('data.xlsx')
worksheet = workbook.add_worksheet()

worksheet.set_column('A:A',20)
