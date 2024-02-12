from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class Automation:
    def findMainURL(self):
        try:
            browser = webdriver.Chrome()
            browser.get('https://www.accuweather.com/')

        
            input_field = WebDriverWait(browser, 5).until( # Wait until the search input field is clickable (max 5 seconds)
                EC.element_to_be_clickable((By.CLASS_NAME, 'search-input'))
            )

            city = input("Enter City Name: ")
            input_field.send_keys(city)
            input_field.send_keys(Keys.ENTER)
    
            # browser.implicitly_wait(2)
            print("Getting Location URL")
    
            try:
                first_option = WebDriverWait(browser, 5).until(  # adding delay to load the page
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[6]/div[1]/div[1]/div[2]/a[1]'))
                )
    
                href_value = first_option.get_attribute('href')
                first_option.click()
                print(href_value)
                return href_value
            except NoSuchElementException:
                print("No location found")
                exit()  # Exit the script if no location is found
            browser.quit()
        except TimeoutException as te:
            print(f"Timeout Exception: {te}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    
    


    def findDailyReportURL(self):
        try:
            URL = self.findMainURL()
            browser2 = webdriver.Chrome()
            browser2.get(URL)
            print("Getting " + " daily forecast URL")

            # continuing actions on second browser without waiting
            daily_forecast = browser2.find_element(By.XPATH, '/html/body/div/div[3]/div/div[3]/a[3]')
            daily_forecast_URL = daily_forecast.get_attribute('href')
            print(daily_forecast_URL)
            return daily_forecast_URL

        except TimeoutException as te:
            print(f"Timeout Exception: {te}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            try:
                browser2.quit()
            except NameError:
                pass  # Ignore if browser2 is not defined
            
