import time
import pytest
import yagmail


# def send_email(report):
#     yag = yagmail.SMTP(user="zhengchenhappy@163.com",
#                        password="Zc_1527815170",
#                        host='smtp.163.com')
#     subject = "自动化测试报告"
#     contents = "请查看附件"
#     yag.send('zhengchenhappy@163.com', subject, contents, report)
#     print("Email has sent out!")

if __name__ == "__main__":
    now = time.strftime("%Y%m%d_%H%M%S", time.localtime(time.time()))
    reportfile = './test_report/' + now + '_testreport.html'

    pytest.main(["-q", "--html", reportfile])

    # pytest.main(["-q"])


    # send_email(reportfile)
