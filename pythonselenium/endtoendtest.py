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

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.LINK_TEXT,"Shop").click()
products = driver.find_elements(By.XPATH,"//div[@class='card h-100']")
for i in products:
    productname = i.find_element(By.XPATH,"div/h4/a").text
    if productname == "Blackberry":
        i.find_element(By.XPATH,"div/button").click()

driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()
driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
driver.find_element(By.ID,"country").send_keys("ind")

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))

driver.find_element(By.LINK_TEXT,"India").click()

driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
success_text = driver.find_element(By.CLASS_NAME,"alert-success").text

assert "Success! Thank you!" in success_text   #partial assertion


