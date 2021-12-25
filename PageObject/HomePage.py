from selenium.webdriver.common.by import By

from PageObject.checkOutPage import CheckoutPage


class HomePage:
    shop = ((By.CSS_SELECTOR,"a[href*='shop']"))
    def __init__(self,driver):
        self.driver=driver
    def getShopButton(self):
        self.driver.find_element(*HomePage.shop).click()
        checkout = CheckoutPage(self.driver)
        return checkout

        # self.driver.find_element_by_css_selector("a[href*='shop']").click()