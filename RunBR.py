import unittest
from BeautifulReport import BeautifulReport

if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.discover('testcase', pattern='test*.py')
    result = BeautifulReport(test_suite)
    result.report(filename='测试报告', description='测试报告', log_path='D:\\interfacetest\\logs')
