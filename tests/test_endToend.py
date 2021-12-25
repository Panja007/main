import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObject.HomePage import HomePage
from PageObject.checkOutPage import CheckoutPage
from PageObject.confirm import ConfirmPage
from utilities.Base_Class import BaseClass


class TestOne(BaseClass):

    def test_eToe(self):
        log=self.getLogger()

        homePage=HomePage(self.driver)

        checkout=homePage.getShopButton()
        products = checkout.getProducts()
        log.info("getting all the product count")
        assert len(products) == 4

        productName = checkout.getiphoneName()

        log.info("selected item iPhone")

        productName.find_element_by_xpath("//a[text()='iphone X']/parent::h4/parent::div/parent::div/div[2]/button").click()

        checkout.getCheckButton().click()
        confirm=checkout.getCheckButton2()
        confirm.getContry().send_keys("ind")
        self.verifyLinkPresence("//a[text()='India']")
        confirm.getIndia().click()
        confirm.getCheckBox().click()
        confirm.getSubmit().click()
        successText = confirm.getAlert().text
        log.info("Text received from apllication is"+successText)
        assert "Success!" in successText

        #self.driver.get_screenshot_as_file("screen.png")