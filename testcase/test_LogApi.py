# coding=utf-8
"""
__title__ = ''
__author__ = 'davieyang'
__mtime__ = '2018/4/21'
"""
import time
from selenium import webdriver
import GetLog
import unittest




class TestLogApi(unittest.TestCase):
    my_logger = GetLog.Logger(logger='TestLogApi').getlog()
    def test_printlog(self):
        driver = webdriver.Chrome()
        TestLogApi.my_logger.info("打开浏览器")
        driver.maximize_window()
        TestLogApi.my_logger.info("最大化浏览器窗口。")
        driver.implicitly_wait(10)

        driver.get("https://www.baidu.com")
        TestLogApi.my_logger.info("打开百度首页。")
        time.sleep(3)
        TestLogApi.my_logger.info("暂停3秒。")
        driver.quit()
        TestLogApi.my_logger.info("关闭并退出浏览器。")

if __name__ == '__main__':
    unittest.main()


#  testlog = TestLogApi()
#  testlog.test_print_log()
