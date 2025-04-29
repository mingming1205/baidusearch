from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def open(self,url):
        self.driver.get(url)

# 继承父类BasePage
class BaiduPage(BasePage):

    @property
    def search_input(self):
        return self.driver.find_element(By.ID, 'kw')

    @property
    def search_button(self):
        return self.driver.find_element(By.ID,'su')

# 另一个页面也需要用到初始化打开网页，则考虑用父类-BasePage
class MailPage(BasePage):

    def account_page(self):
        pass



