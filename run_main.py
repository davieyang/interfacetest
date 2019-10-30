'''
@Time    : 2018/9/26 13:28
@Author  : 
@Email   : davieyang@qq.com
@File    : run_main.py
@Software: PyCharm
@Description:
'''
# encoding = utf-8
import os
import time
import unittest
import HTMLTestRunner

current_path = os.path.dirname(os.path.realpath(__file__))

def add_case(caseName = 'testcase', rule = 'test*.py'):
    case_path = os.path.join(current_path, caseName)
    if not os.path.exists(case_path):os.mkdir(case_path)
    print("test case path: %s" %case_path)
    discover = unittest.defaultTestLoader.discover(case_path, pattern=rule, top_level_dir=None)
    print(discover)
    return discover

def run_case(all_case, reportName = "report"):
    now = time.strftime("%Y_%m_%d_%H_%M_%S")
    report_path = os.path.join(current_path, reportName)
    if not os.path.exists(report_path):os.mkdir(report_path)
    report_abspath = os.path.join(report_path, now + "results.html")
    print("report path:%s" %report_path)
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream = fp, title = u'自动化测试报告，测试结果如下：', description = u'用例执行情况：')
