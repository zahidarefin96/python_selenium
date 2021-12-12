# xpath => //tagname[@attribute='value']
# css_selector => tagname[attribute='value']

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\zahid\\Downloads\\chromedriver_win32\\chromedriver.exe")

driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element_by_xpath("//input[@id='name']").send_keys("md")

driver.find_element_by_xpath("//input[@id='alertbtn']").click()

alert = driver.switch_to.alert

print(alert.text)

alert.accept()  # selecting yes in pop-up

# alert.dismiss() #will select no in pop-up
