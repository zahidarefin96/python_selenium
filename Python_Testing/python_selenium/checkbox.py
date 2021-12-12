# xpath => //tagname[@attribute='value']
# css_selector => tagname[attribute='value']

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\zahid\\Downloads\\chromedriver_win32\\chromedriver.exe")

driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")

print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":  # selecting option 2
        checkbox.click()
        assert checkbox.is_selected()
