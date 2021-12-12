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

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

action = ActionChains(driver)

menu = driver.find_element_by_id("mousehover")

action.move_to_element(menu).perform()

reloadPage = driver.find_element_by_link_text("Reload")

action.move_to_element(reloadPage).click().perform()
