from selenium.webdriver.support import wait


class waitObject:

    def __init__(self, driver):
        self.driver = driver
        self.getWaitObj = wait.WebDriverWait(self.driver, 10)

    def getElement(self, name, key):
        return self.getWaitObj.until(lambda driver: self.driver.find_element(by=name, value=key))

    def getElements(self, name, key):
        return self.getWaitObj.until(lambda driver: self.driver.find_elements(by=name, value=key))
