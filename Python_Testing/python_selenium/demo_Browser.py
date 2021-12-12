# xpath => //tagname[@attribute='value']
# xpath => //tagName[contains(@attribute,'value')]

# css_selector => tagname[attribute='value']
# css_selector => tagName#id
# css_selector => tagname.classname
# css_selector => tagName[Atrribute*='value']

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\zahid\\Downloads\\chromedriver_win32\\chromedriver.exe")

# driver = webdriver.Firefox(executable_path="")

# driver = webdriver.Ie(executable_path="")

driver.maximize_window()

driver.get("https://www.rahulshettyacademy.com/#/index")

print(driver.title)

print(driver.current_url)

driver.get("https://www.rahulshettyacademy.com/#/practice-project")

driver.back()

driver.refresh()

driver.close()
