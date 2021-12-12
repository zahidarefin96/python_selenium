# xpath => //tagname[@attribute='value']
# xpath => //tagName[contains(@attribute,'value')]

# css_selector => tagname[attribute='value']
# css_selector => tagName#id
# css_selector => tagname.classname
# css_selector => tagName[Atrribute*='value']

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\\Users\\zahid\\Downloads\\chromedriver_win32\\chromedriver.exe")

driver.maximize_window()

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_name("name").send_keys("hello")

# using selenium
print(driver.find_element_by_name("name").get_attribute("value"))

# using javascript
print(driver.execute_script('return document.getElementsByName("name")[0].value'))
