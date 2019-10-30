# encoding = utf-8
import HTMLTestRunner
import unittest
import time


class StartTest(object):

    def __init__(self):
        print("generate test reports...")

    @staticmethod
    def starttest():
        test_suite = unittest.defaultTestLoader.discover( 'testcase', pattern='test*.py' )
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        filename = "D:\\interfacetest\\report\\Results-" + now + "results.html"
        print(filename)
        fp = open("D:\\interfacetest\\report\\Results-" + now + "results.html", 'wb')
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Result', description='Test_Report')
        runner.run(test_suite)
        print('Test reports generate finished')


if __name__ == '__main__':
    StartTest.starttest()


