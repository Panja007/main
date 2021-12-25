from selenium.webdriver.common.by import By

from PageObject.confirm import ConfirmPage


class CheckoutPage:
    products=((By.XPATH,"//div[@class='card h-100']"))
    iphoneX=((By.XPATH,"//a[text()='iphone X']"))
    checkButton=(By.CSS_SELECTOR,"a[class*='btn-primary']")
    checkButton2=(By.CSS_SELECTOR,"button[class*='btn-success']")
    def __init__(self,driver):
        self.driver = driver
    def getProducts(self):
        return self.driver.find_elements(*CheckoutPage.products)
        # self.driver.find_elements_by_xpath("//div[@class='card h-100']")
    def getiphoneName(self):
        return self.driver.find_element(*CheckoutPage.iphoneX)
        #self.driver.find_element_by_xpath("//a[text()='iphone X']")
    def getCheckButton(self):

        # self.driver.find_element_by_css_selector("a[class*='btn-primary']")
        return self.driver.find_element(*CheckoutPage.checkButton)

    def getCheckButton2(self):
        # self.driver.find_element_by_css_selector("button[class*='btn-success']")
        self.driver.find_element(*CheckoutPage.checkButton2).click()
        confirm = ConfirmPage(self.driver)
        return confirm
