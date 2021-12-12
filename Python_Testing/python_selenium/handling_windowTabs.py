# xpath => //tagname[@attribute='value']
# xpath => //tagName[contains(@attribute,'value')]

# css_selector => tagname[attribute='value']
# css_selector => tagName#id
# css_selector => tagname.classname
# css_selector => tagName[Atrribute*='value']

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\zahid\\Downloads\\chromedriver_win32\\chromedriver.exe")

driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/windows")

print(driver.find_element_by_xpath("//h3[contains(text(),'Opening a new window')]").text)

driver.find_element_by_xpath("//a[contains(text(),'Click Here')]").click()

childWindow = driver.window_handles[1]

driver.switch_to.window(childWindow)

print(driver.find_element_by_xpath("//h3[contains(text(),'New Window')]").text)

parentWindow = driver.window_handles[0]

driver.switch_to.window(parentWindow)
