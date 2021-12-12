# xpath => //tagname[@attribute='value']
# xpath => //tagName[contains(@attribute,'value')]

# css_selector => tagname[attribute='value']
# css_selector => tagName#id
# css_selector => tagname.classname
# css_selector => tagName[Atrribute*='value']

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\Users\\zahid\\Downloads\\chromedriver_win32\\chromedriver.exe")

driver.maximize_window()

driver.get("https://rahulshettyacademy.com/angularpractice/")

# shop
driver.find_element_by_xpath("//a[contains(text(),'Shop')]").click()

products = driver.find_elements_by_xpath("//div[@class='card h-100']")

for product in products:
    product_name = product.find_element_by_xpath("div/h4/a").text
    # rint(productName)
    if product_name == "Blackberry":
        product.find_element_by_xpath("div/button").click()

# Checkout
driver.find_element_by_css_selector("a[class*='btn-primary']").click()

# Click checkout button
driver.find_element_by_xpath("//button[@class='btn btn-success']").click()

# Autosuggestive
driver.find_element_by_xpath("//input[@id='country']").send_keys("United")

wait = WebDriverWait(driver, 8)

wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "United States of America")))

driver.find_element_by_link_text("United States of America").click()

driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()

driver.find_element_by_css_selector("[type='submit']").click()

success_Text = driver.find_element_by_class_name("alert-success").text

assert "Success! Thank you!" in success_Text

# get screenshot
driver.get_screenshot_as_file("screen.png")
