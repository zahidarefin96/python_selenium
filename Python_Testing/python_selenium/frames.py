# xpath => //tagname[@attribute='value']
# xpath => //tagName[contains(@attribute,'value')]

# css_selector => tagname[attribute='value']
# css_selector => tagName#id
# css_selector => tagname.classname
# css_selector => tagName[Atrribute*='value']

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\zahid\\Downloads\\chromedriver_win32\\chromedriver.exe")

driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/iframe")

# frame name / frame set / index value
driver.switch_to.frame("mce_0_ifr")

driver.find_element_by_css_selector("#tinymce").clear()

driver.find_element_by_css_selector("#tinymce").send_keys("My name is Md Zahid Arefin")

driver.switch_to.default_content()

# iframe, frameset, frame
