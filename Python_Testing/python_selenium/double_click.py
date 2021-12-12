# css_selector => tagname[attribute='value']
# css_selector => tagName#id
# css_selector => tagname.classname
# css_selector => tagName[Atrribute*='value']

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\\Users\\zahid\\Downloads\\chromedriver_win32\\chromedriver.exe")

driver.maximize_window()

driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")

action = ActionChains(driver)

action.double_click(driver.find_element_by_id("double-click")).perform()

alert = driver.switch_to.alert

assert "You double clicked me!!!, You got to be kidding me" == alert.text

alert.accept()
