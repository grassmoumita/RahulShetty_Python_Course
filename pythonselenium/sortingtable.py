import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:/Users/moumitajoardar/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)
driver.implicitly_wait(5)      #wait globally for max 5 sec, implicit wait will not work for find_elements

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()


#click on column header
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()
#collect all vegie name - > veggielist
browsersortedveggies=[]
veggielist = driver.find_elements(By.XPATH,"//tr/td[1]")
for i in veggielist:
    browsersortedveggies.append(i.text)

originalbrowsersortedlist = browsersortedveggies.copy()
#sorted the veggielist ->newsortedlist

browsersortedveggies.sort()

#newsortedlist == veggielist

assert browsersortedveggies == originalbrowsersortedlist


