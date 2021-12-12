# xpath => //tagname[@attribute='value']
# css_selector => tagname[attribute='value']

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\Users\\zahid\\Downloads\\chromedriver_win32\\chromedriver.exe")

driver.maximize_window()

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_name("email").send_keys("zahidarefin96@gmail.com")

driver.find_element_by_xpath("//input[@id='exampleInputPassword1']").send_keys("badda1212")

# static dropDown code starts here

dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))

dropdown.select_by_visible_text("Female")

dropdown.select_by_index(0)  # selecting male

driver.find_element_by_xpath("//input[@type='submit']").click()

message = driver.find_element_by_class_name("alert-success").text

assert "success" in message
