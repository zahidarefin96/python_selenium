from selenium.webdriver.common.by import By

from page_objects.ConfirmPage import ConfirmPage


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    # driver.find_elements_by_xpath("//div[@class='card h-100']")
    productTitle = (By.XPATH, "//div[@class='card h-100']")

    # driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
    checkOut = (By.XPATH, "//button[@class='btn btn-success']")

    def getProductTitles(self):
        return self.driver.find_element(*CheckoutPage.productTitle)

    def checkoutItems(self):
        self.driver.find_element(*CheckoutPage.checkOut).click()

        confirmPage = ConfirmPage(self.driver)
        return confirmPage
