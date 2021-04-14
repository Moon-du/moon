# _*_ coding: UTF-8 _*_
# @Time : 2020/11/12 10:01
# @Author : moon
# @Site : www.ysbzc.com
# @File : game_stats.py
# @Software : PyCharm

class GameStats():
    # 游戏统计信息

    def __init__(self, ai_settings):
        # """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_start()
        # 游戏一开始就是非活动状态
        self.game_active = False
        # 在任何情况下都不应重置最高得分
        self.high_score = 0

    def reset_start(self):
        # """初始化在游戏运行期间可能变化的统计信息"""
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
