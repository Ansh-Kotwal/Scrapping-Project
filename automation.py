import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # exceptional conditions class


class Automation:
    
    def getURL(location):
        try:

            browser = webdriver.Chrome()
            browser.get("https://www.accuweather.com/")

            wait = WebDriverWait(browser, 10 )

            searchbox = wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div/div[1]/div[3]/div/div[1]/div[1]/form/input")))
            time.sleep(1)
            searchbox.send_keys(location)
            searchbox.send_keys(Keys.ENTER)

            time.sleep(4)

            regionSelector = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[6]/div[1]/div[1]/div[2]/a[1]')))
            # regionSelector.send_keys(Keys.CONTROL,Keys.F12)
            regionSelector.click()


            daily = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[3]/div/div[3]/a[3]')))
            dailyURL = daily.get_attribute('href')
            print(dailyURL)


        except Exception as e:
            print("Error is :"+ e)

        finally:
            input("Press Enter to close browser")
            browser.close()
    
    