# _*_ coding: UTF-8 _*_
# @Time     : 2020/10/28 下午 02:15
# @Author   : Li Jie
# @Site     : http://www.cdtest.cn/
# @File     : run.py
# @Software : PyCharm

import unittest
import HTMLTestRunner

# 运行文件
# 批量扫描文件夹添加，生成HTML测试报告

# 1.生成测试套件，添加测试用例类
suite = unittest.defaultTestLoader.discover(r'C:\Users\Aurora\Desktop\moon\po\case', pattern='*_test.py')

# 2.生成运行器
file = open(r'C:\Users\Aurora\Desktop\moon\po\log\test_result.html', mode='wb')
runner = HTMLTestRunner.HTMLTestRunner(file, title='汇智动力测试报告', description='测试人员：冯钰阳')

# 3.运行测试套件
runner.run(suite)

# 4.关闭文件
file.close()