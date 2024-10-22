import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:/Users/moumitajoardar/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"#name").send_keys("Moumita")
driver.find_element(By.ID,"alertbtn").click()

#to take the alert switch to alert mode
name="Moumita"
alert = driver.switch_to.alert
alert_text = alert.text   #to find the text of the alert pop up
print(alert_text)
assert name in alert_text
alert.accept()     #to click on OK on the alert
# alert.dismiss()     #to click on Cancel on the alert

time.sleep(2)