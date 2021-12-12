# xpath => //tagname[@attribute='value']
# css_selector => tagname[attribute='value']


from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\zahid\\Downloads\\chromedriver_win32\\chromedriver.exe")

driver.maximize_window()

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_name("name").send_keys("Md Zahid Arefin")

driver.find_element_by_xpath("//body/app-root[1]/form-comp[1]/div[1]/form[1]/div[2]/input[1]").send_keys(
    "zahidarefin96@gmail.com")

driver.find_element_by_css_selector("#exampleInputPassword1").send_keys("badda1212")

driver.find_element_by_id("exampleCheck1").click()

driver.find_element_by_css_selector("input[class='btn btn-success']").click()

print(driver.find_element_by_class_name("alert-success").text)
