# xpath => //tagname[@attribute='value']
# xpath => //tagName[contains(@attribute,'value')]

# css_selector => tagname[attribute='value']
# css_selector => tagName#id
# css_selector => tagname.classname
# css_selector => tagName[Atrribute*='value']

from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(executable_path="C:\\Users\\zahid\\Downloads\\chromedriver_win32\\chromedriver.exe",
                          options=chrome_options)

driver.get("https://www.rahulshettyacademy.com/#/index")

print(driver.title)

# learn more ChromeOptions : https://www.programcreek.com/python/example/100025/selenium.webdriver.ChromeOptions
