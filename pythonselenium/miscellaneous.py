import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")    #headless means without open the browser the automation will process

chrome_options.add_argument("--ignore-certificate-errors")  #to run the website where we need to click advance button for proceed

service_obj = Service("C:/Users/moumitajoardar/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service = service_obj,options=chrome_options)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

#to go to the down of the page by scroll
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")

# to take screenshorts
driver.get_screenshot_as_file("screen.png")