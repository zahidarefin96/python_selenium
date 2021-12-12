# xpath => //tagname[@attribute='value']
# xpath => //tagName[contains(@attribute,'value')]

# css_selector => tagname[attribute='value']
# css_selector => tagName#id
# css_selector => tagname.classname
# css_selector => tagName[Atrribute*='value']
import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\zahid\\Downloads\\chromedriver_win32\\chromedriver.exe")

driver.maximize_window()

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element_by_xpath("//input[@class='search-keyword']").send_keys("ber")

time.sleep(2)

count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))

assert count == 3

buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")

for button in buttons:
    button.click()

driver.find_element_by_css_selector("img[alt='Cart']").click()

driver.find_element_by_xpath("//button[@text()='PROCEED TO CHECKOUT").click()