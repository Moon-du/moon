# _*_ coding: UTF-8 _*_
# @Time     : 2020/10/27 下午 02:16
# @Author   : Li Jie
# @Site     : http://www.cdtest.cn/
# @File     : run1.py
# @Software : PyCharm

import unittest
import HTMLTestRunner

# 运行文件
# 批量扫描文件夹添加，生成HTML测试报告

# 1.生成测试套件，添加测试用例类
suite = unittest.defaultTestLoader.discover(r'D:\pyworkspace\t63\selenium5', pattern='*_test.py')

# 2.生成运行器
file = open('./test_result.html', mode='wb')
runner = HTMLTestRunner.HTMLTestRunner(file, title='汇智动力测试报告', description='测试人员：李杰')

# 3.运行测试套件
runner.run(suite)

# 4.关闭文件
file.close()
