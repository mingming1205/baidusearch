import time
import unittest
import yagmail
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
from baidu_page import BaiduPage


def send_email(report):
    yag = yagmail.SMTP(user="zhengchenhappy@163.com",
                       password="Zc_1527815170",
                       host='smtp.163.com')
    subject = "自动化测试报告"
    contents = "请查看附件"
    yag.send('zhengchenhappy@163.com', subject, contents, report)
    print("Email has sent out!")


# 在测试用例中没有元素定位，元素定位封装在baidu_page.py中

class TestBaidu(unittest.TestCase):

    def setUp(self):
        self.dr = webdriver.Chrome()
        # self.dr = webdriver.Edge()
        self.url = "https://www.baidu.com"
        self.dr.maximize_window()

    def tearDown(self):
        self.dr.quit()

    def test_search(self):

        # 拿到baidupage中的驱动dr
        page = BaiduPage(self.dr)

        page.open(self.url)

        # 拿到类对象的方法
        # 可把操作对象search_input()小括号去掉，由在baidu_page中加装饰器@property
        page.search_input.send_keys("page object")
        page.search_button.click()
        time.sleep(1)


if __name__ == '__main__':
    # unittest.main()

    # 定义测试用例目录为当前目录
    test_dir = './'
    suit = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')

    # 获取当前日期和时间
    now_time = time.strftime("%Y%m%d %H%M%S", time.localtime(time.time()))

    html_report = './test_report/' + now_time + 'report.html'
    fp = open(html_report, 'wb')

    runner = HTMLTestRunner(stream=fp,
                            title="测试报告",
                            description="运行环境：Windows11，Chrome浏览器"
                            )
    runner.run(suit)
    # 结果写入文件后关闭
    fp.close()

    send_email(html_report)


