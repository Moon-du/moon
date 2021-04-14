# _*_ coding: UTF-8 _*_
# @Time     : 2020/10/27 上午 11:55
# @Author   : Li Jie
# @Site     : http://www.cdtest.cn/
# @File     : run.py
# @Software : PyCharm

import unittest
from selenium5.unittest_test import JDTest

# 用例的运行文件
# 1.生成测试套件suite
suite = unittest.TestSuite()

# 2.将用例加入测试套件
# addTest(测试用例类名('方法名'))
suite.addTest(JDTest('test'))

# 3.生成运行器，运行测试套件
runner = unittest.TextTestRunner()
runner.run(suite)
