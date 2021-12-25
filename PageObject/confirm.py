import pytest
from selenium.webdriver.common.by import By


class ConfirmPage:

    country = (By.ID,"country")
    enterIndia=(By.XPATH,"//a[text()='India']")
    checkBox=(By.XPATH,"//label[@for='checkbox2']")
    submit=(By.CSS_SELECTOR,"input[type='submit']")
    alert = (By.CSS_SELECTOR,"div[class*='alert-dismissible']")
    def __init__(self,driver):
        self.driver=driver
    def getContry(self):
        # self.driver.find_element_by_id("country")
        return self.driver.find_element(*ConfirmPage.country)
    def getIndia(self):
        # self.driver.find_element_by_xpath("//a[text()='India']")
        return self.driver.find_element(*ConfirmPage.enterIndia)
    def getCheckBox(self):
        # self.driver.find_element_by_xpath("//label[@for='checkbox2']")
        return self.driver.find_element(*ConfirmPage.checkBox)
    def getSubmit(self):
        # self.driver.find_element_by_css_selector("input[type='submit']")
        return self.driver.find_element(*ConfirmPage.submit)
    def getAlert(self):
        # self.driver.find_element_by_css_selector("div[class*='alert-dismissible']")
        return self.driver.find_element(*ConfirmPage.alert)

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)