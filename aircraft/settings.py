# _*_ coding: UTF-8 _*_
# @Time : 2020/11/12 9:58
# @Author : moon
# @Site : www.ysbzc.com
# @File : settings.py
# @Software : PyCharm

class Settings():
    # 存储游戏所有设置的类
    def __init__(self):
        # """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (135, 206, 235)  # 天蓝色

        # 飞船的设置
        self.ship_speed_factor = 1.5
        self.ship_limit = 1

        # 子弹设置
        self.bullet_speed_factor = 3
        self.bullet_width = 2  # 这里更改子弹的宽度
        self.bullet_height = 30
        self.bullet_color = 0, 255, 255
        self.bullets_allowed = 5  # 这里更改子弹的个数
        # 外星人设置

        self.fleet_drop_speed = 10  # 默认10

        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.5
        # 分数的提高速度
        self.score_scale = 1.5
        # 动态变化
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        # 初始化随游戏进行而变化的设置
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        # fleet_direction为1表示向右；为-1表示向左
        self.fleet_direction = 1

        # 积分
        self.alien_points = 100

    def increase_speed(self):
        # 提高速度设置
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
