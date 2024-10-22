import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:/Users/moumitajoardar/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

# ID, Xpath, CSSSelector, classname, name, linktext

driver.find_element(By.NAME, "email").send_keys("moumitajoardar95@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()

#  //tagname[@attribute='value']     formula xpath

# driver.find_element(By.CLASS_NAME,"btn-success").click()
driver.find_element(By.XPATH,"//input[@class='btn btn-success']").click()

#  CSS Selector formula   tagname[attribute='value'], also CSS can use this formula #id - #inlineRadio1 like this
# also CSS another formula  .classname
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Moumita")
driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()

message = driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)
assert "Success" in message      #assert use to check pass or fail

#(//input[@type='text'])[3]  this xpath we use when we have many input with same type, rhen need to mention the number last to select the particular input box
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("hello again")
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()    #to clear everythig from the input text


#static dropdown
#Select will use for static dropdown
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(1)
# dropdown.select_by_value()     # this is another method by select value







time.sleep(5)
driver.close()

