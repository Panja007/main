import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        logger = logging.getLogger(__name__)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        return logger
    def verifyLinkPresence(self,text):
        wait = WebDriverWait(self.driver,10)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH,text)))