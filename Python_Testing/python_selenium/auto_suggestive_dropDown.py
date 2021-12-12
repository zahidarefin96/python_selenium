# xpath => //tagname[@attribute='value']
# css_selector => tagname[attribute='value']
import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\zahid\\Downloads\\chromedriver_win32\\chromedriver.exe")

driver.maximize_window()

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element_by_id("autosuggest").click()

driver.find_element_by_id("autosuggest").send_keys("ban")

time.sleep(2)

countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")

print(len(countries))

for country in countries:
    if country.text == "Bangladesh":
        country.click()
        break

print(driver.find_element_by_id("autosuggest").text)

assert driver.find_element_by_id("autosuggest").get_attribute("value") == "Bangladesh"
