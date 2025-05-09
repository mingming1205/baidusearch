import time
import pytest

if __name__ == "__main__":
    now = time.strftime("%Y%m%d_%H%M%S", time.localtime(time.time()))
    reportfile = './test_report/' + now + '_testreport.html'

    pytest.main(["-q", "--html", reportfile])

