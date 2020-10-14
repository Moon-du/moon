# _*_ coding: UTF-8 _*_
# @Time     : 2020/10/12 下午 02:33
# @Author   : Moon-du
# @Site     : https://www.ysbzc.com/
# @File     : input_output.py
# @Software : PyCharm


# 输出:print()打印信息到屏幕
print('hello world!')
print("人生若只如初见，\n何事秋风悲画扇。\n等闲变却故人心，\n却道故人心易变。")  # \n:换行符，相当于按enter
print("人生若只如初见，\t何事秋风悲画扇。\t等闲变却故人心，\t却道故人心易变。")  # \t：制表符，相当于按tab
print('''人生若只如初见，
何事秋风悲画扇。
等闲变却故人心，
却道故人心易变。''')

print('---------------------------我是分割线--------------------------------')
# 输入：input()从键盘获取输入，输入以enter结束,返回的都是字符串类型
name = input('请输入您的名字:')
print('你好，' + name)
