# _*_ coding: UTF-8 _*_
# @Time : 2020/11/12 10:05
# @Author : moon
# @Site : www.ysbzc.com
# @File : main.py
# @Software : PyCharm

import game_functions as gf
# 主程序文件
# 创建Pygame窗口响应以及用户输入
import pygame
from button import Button
from game_stats import GameStats
from pygame.sprite import Group
from scoreboard import Scoreboard
from settings import Settings
from ship import Ship


def run_game():
    # 初始化游戏并且创建一个屏幕对象
    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption("打飞机")

    # 创建play按钮
    play_button = Button(ai_settings, screen, "PLAY~")

    # 创建一个用户存储游戏统计信息的实例
    stats = GameStats(ai_settings)

    sb = Scoreboard(ai_settings, screen, stats)

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建一个用户存储子弹的编组
    bullets = Group()

    # 创建一个外星人
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏主循环
    while True:

        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()

            # 删除已消失的子弹
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)

            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

        # 让最近绘制的屏幕可见
        pygame.display.flip()


run_game()
