from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def scrappingDailyData(driver , heading , url):
 print(heading + " = " + url)
 
 daily_Data = []

 for day in range (1 , 10):
   perDayData(driver , f"{url}?day={day}" , day , daily_Data)

 print("Data Successfully Added")
 return daily_Data
        
def perDayData(driver , dayUrl , day , daily_Data):
   driver.get(dayUrl)
   wait = WebDriverWait(driver, 5 )

   temp_tag = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "temperature")))
   phrase_tag =  wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "phrase")))
   day_night_tag = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "title")))
   other_data = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "value")))

   print(f"Day {day}")
   #print(len(day_night_tag))

   if len(day_night_tag) == 6:  

            per_Day_Data = {
                    "day":{
                            "available" : 1,
                            "temp": temp_tag[0].text,
                            "max_uv_index":other_data[0].text,
                            "wind": other_data[1].text,
                            "wind_gust":other_data[2].text,
                            "probability_of_precipitation":other_data[3].text,
                            "probability_of_thunderstorms":other_data[4].text,
                            "Precipitation": other_data[5].text,
                            "cloud_cover": other_data[6].text,
                            "remark": phrase_tag[0].text,
                            },
                    "night":{
                            "temp": temp_tag[1].text,
                            "wind": other_data[7].text,
                            "wind_gust":other_data[8].text,
                            "probability_of_precipitation":other_data[9].text,
                            "probability_of_thunderstorms":other_data[10].text,
                            "Precipitation": other_data[11].text,
                            "cloud_cover": other_data[12].text,
                            "remark": phrase_tag[1].text,
                            }
                    }
   else:          
            per_Day_Data = {
                    "day":{
                             "available" : 0
                           },
                    "night":{
                            "temp": temp_tag[0].text,
                            "wind": other_data[0].text,
                            "wind_gust":other_data[1].text,
                            "Probability of Precipitation":other_data[2].text,
                            "Probability of Thunderstorms":other_data[3].text,
                            "Precipitation": other_data[4].text,
                            "cloud_cover": other_data[5].text,
                            "remark": phrase_tag[0].text
                            }
                    }
            
   dataAppend(day , per_Day_Data , daily_Data)
   
def dataAppend(day , per_Day_Data , daily_Data):
  
  per_Day_Data = {
            f"day {day}" : per_Day_Data
        }
     
  daily_Data.append(per_Day_Data)    
       
def flattenDailyDataJson(json_data):
    flattened_data = []
    for record in json_data:
        for key, value in record.items():
            day_number = key
            day = value['day']
            night = value['night']
            flattened_record = {
                'Days': day_number.capitalize(),
                'Day Temperature': day['temp'],
                'Max UV Index': day['max_uv_index'],
                'Day Wind': day['wind'],
                'Day Wind Gust': day['wind_gust'],
                'Day Probability of Precipitation': day['probability_of_precipitation'],
                'Day Probability of Thunderstorms': day['probability_of_thunderstorms'],
                'Day Precipitation': day['Precipitation'],
                'Day Cloud Cover': day['cloud_cover'],
                'Day Remark': day['remark'],
                'Night Temperature': night['temp'],
                'Night Wind': night['wind'],
                'Night Wind Gust': night['wind_gust'],
                'Night Probability of Precipitation': night['probability_of_precipitation'],
                'Night Probability of Thunderstorms': night['probability_of_thunderstorms'],
                'Night Precipitation': night['Precipitation'],
                'Night Cloud Cover': night['cloud_cover'],
                'Night Remark': night['remark']
            }
            flattened_data.append(flattened_record)
    return flattened_data 
    
  