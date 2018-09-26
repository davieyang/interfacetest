import unittest
import time
from BeautifulReport import BeautifulReport

if __name__ == '__main__':
    current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    test_suite = unittest.defaultTestLoader.discover('testcase', pattern='test*.py')
    result = BeautifulReport(test_suite)
    result.report(filename='测试报告' + '-' + current_time, description='测试报告', report_path='D:\\interfacetest\\report')
