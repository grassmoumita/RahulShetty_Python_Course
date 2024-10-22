import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:/Users/moumitajoardar/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)


#chrome driver service
# driver = webdriver.Chrome()      # we can also this beyond use the above 2 lines, above two we wll use if we have any VPN issue or chrome version older
# driver = webdriver.Firefox()      #for firefox browser
# driver = webdriver.Edge()       #for edge browser


driver.get("https://www.flipkart.com/")
driver.maximize_window()    #maximixe the window
print(driver.title)       # title of any page
print(driver.current_url)       #for current url print






time.sleep(2)