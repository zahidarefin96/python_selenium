# xpath => //tagname[@attribute='value']
# css_selector => tagname[attribute='value']

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\zahid\\Downloads\\chromedriver_win32\\chromedriver.exe")

driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

radioButton = driver.find_element_by_xpath("//input[@value='radio3']")

radioButton.click()

assert radioButton.is_selected()
