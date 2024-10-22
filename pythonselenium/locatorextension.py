import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/moumitajoardar/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)

driver.get("https://rahulshettyacademy.com/client/")
driver.maximize_window()
# driver.find_element(By.LINK_TEXT,"Forgot password?").click()     #link text use for <a> tag and need to put the full link text name
driver.find_element(By.PARTIAL_LINK_TEXT,"Forgot password").click()   #partial link text use for <a> tag and need to put the partial or full link text name

#some other xpath formula - //form/div[1]/input
#//form/div[1]/input  -- form in which the input field is, then the div and the div number in which the input field is and after that the input field
driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("moumita@gmail.com")

#some other css selector formula - form div:nth-child(2) input
#form div:nth-child(2) input - same as above xpath, only remove the / and :nth-child(2) add this for mention the dic number
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys("Hello@@@123")

driver.find_element(By.CSS_SELECTOR,"#confirmPassword").send_keys("Hello@@@123")    #using #id method of css

#driver.find_element(By.XPATH,"//button[@type='submit']").click()

#Xpath by text, formula - //button[text()='Save New Password']
driver.find_element(By.XPATH,"//button[text()='Save New Password']").click()


time.sleep(5)