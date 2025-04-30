from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def open(self,url):
        self.driver.get(url)
        time.sleep(1)

class BaiduPage(BasePage):

    @property
    def search_input(self):
        return self.driver.find_element(By.ID, 'kw')

    @property
    def search_button(self):
        return self.driver.find_element(By.ID,'su')
        

class MailPage(BasePage):
    @property
    def account_page(self):
        pass



