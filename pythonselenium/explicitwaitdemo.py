import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:/Users/moumitajoardar/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)
driver.implicitly_wait(2)      #wait globally for max 5 sec, implicit wait will not work for find_elements

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2)
result = driver.find_elements(By.XPATH,"//div[@class='products']/div")
count = len(result)
print(count)
assert count > 0

# to add all the searched item in cart
for i in result:
    i.find_element(By.XPATH,"div/button").click()    #this is chaining, only writing div/button as we are finding in result

# time.sleep(2)

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
# time.sleep(5)

#Sum validation
price = driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
sum = 0
for i in price:
    sum = sum + int(i.text)
print(sum)
totalamount = int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)

assert sum == totalamount


#to check the promo code
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
# time.sleep(5)
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
# time.sleep(10)
#Explicit Wait - for a particular section when we need to wait more time
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)