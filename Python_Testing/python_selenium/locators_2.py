# xpath => //tagname[@attribute='value']
# css_selector => tagname[attribute='value']

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\zahid\\Downloads\\chromedriver_win32\\chromedriver.exe")

driver.maximize_window()

driver.get("https://login.salesforce.com/")

driver.find_element_by_xpath("//input[@id='username']").send_keys("zahidarefin96@gmail.com")

driver.find_element_by_css_selector("#password").send_keys("badda1212")

# driver.find_element_by_id("Login").click()

driver.find_element_by_link_text("Forgot Your Password?").click()

driver.find_element_by_xpath("//input[@name='cancel']").click()

# print(driver.find_element_by_xpath("//label[contains(text(),'Username')]").text)
#
# print(driver.find_element_by_xpath("//label[contains(text(),'Password')]").text)
