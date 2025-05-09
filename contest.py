#!/usr/bin/env python
# -*- coding:utf-8 -*-
# created on May 9th,2025,unittest->pyest


import pytest
from selenium import webdriver


@pytest.fixture(scope = "session",autouse = True)
def webdriver():
    weburl = 'https://www.baidu.com'

    global driver

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(weburl)
    return driver

@pytest.fixture(scope="session",autouse = True)
def driver_close():
    yield driver
    driver.quit()






