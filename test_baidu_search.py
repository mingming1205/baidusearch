import time
import unittest
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
from baidu_page import BaiduPage


class TestBaidu(unittest.TestCase):

    def setUp(self):
        self.dr = webdriver.Chrome()
        # self.dr = webdriver.Edge()
        self.url = "https://www.baidu.com"
        self.dr.maximize_window()

    def tearDown(self):
        self.dr.quit()

    def test_search(self):
        page = BaiduPage(self.dr)

        page.open(self.url)

        page.search_input.send_keys("page object")
        page.search_button.click()
        time.sleep(1)


if __name__ == '__main__':
    test_dir = './'
    suit = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')

    # 获取当前日期和时间
    now_time = time.strftime("%Y%m%d_%H%M%S", time.localtime(time.time()))

    html_report = './test_report/' + now_time + 'report.html'
    fp = open(html_report, 'wb')

    runner = HTMLTestRunner(stream=fp,
                            title="HTMLReport",
                            description="运行环境：Windows11，Chrome浏览器"
                            )
    runner.run(suit)

    # 结果写入文件后关闭
    fp.close()


