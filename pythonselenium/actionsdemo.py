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

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

#mouse hover action
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()   #wgen use action always need to use  .perform()

#for double click
#action.double_click(#give the element).perform()

#for right click
#action.context_click(#give the element).perform()
# action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).perform()
#for drag and drop
#action.drag_and_drop().perform()