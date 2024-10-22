import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:/Users/moumitajoardar/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

#select dynamic checkbox
checkbox = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(len(checkbox))

for i in checkbox:
    if i.get_attribute("value") == "option2":
        i.click()
        assert i.is_selected()     #to check it is selected or not
        break
time.sleep(2)


#Radio button select
radio = driver.find_elements(By.CSS_SELECTOR,".radioButton")
radio[2].click()     #will use this for static radio button, for dynamic will use the above lopp method
assert radio[2].is_selected()
time.sleep(2)


#display box
display = driver.find_element(By.ID,"displayed-text").is_displayed()
assert driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()
assert not driver.find_element(By.ID,"displayed-text").is_displayed()



driver.close()